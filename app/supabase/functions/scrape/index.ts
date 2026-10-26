// MAX WISE Studio – scrape the last 7 days of posts from watched channels via TikHub.
// POST {channel_id?: string}  (Authorization: Bearer <member JWT>)
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const API = "https://api.tikhub.io";
const DAYS = 7;
const MAX_NEW_PER_CHANNEL = 12;
const MAX_PREVIEW_BYTES = 25 * 1024 * 1024;
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

type Ch = {
  id: string; url: string; platform: "douyin" | "tiktok"; name: string | null; sec_uid: string | null;
  min_views: number; min_sec: number; max_sec: number;
};

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const anon = Deno.env.get("SUPABASE_ANON_KEY")!;
  const service = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const auth = req.headers.get("Authorization") ?? "";
  const user = createClient(url, anon, { global: { headers: { Authorization: auth } } });
  const { data: ok } = await user.rpc("is_member");
  if (!ok) return json({ error: "not a member" }, 403);

  const db = createClient(url, service);
  const { data: token } = await db.rpc("tikhub_token");
  if (!token) return json({ error: "TikHub token missing" }, 500);

  let body: { channel_id?: string } = {};
  try { body = await req.json(); } catch { /* empty */ }
  let q = db.from("channels").select("*").eq("active", true);
  q = body.channel_id ? q.eq("id", body.channel_id) : q.eq("auto_scrape", true);
  const { data: chans, error } = await q;
  if (error) return json({ error: error.message }, 500);

  const th = async (path: string, params: Record<string, string | number>) => {
    const u = new URL(API + path);
    for (const [k, v] of Object.entries(params)) if (v !== "" && v != null) u.searchParams.set(k, String(v));
    for (let i = 0; i < 3; i++) {
      try {
        const r = await fetch(u, { headers: { Authorization: `Bearer ${token}` } });
        const d = await r.json();
        if (d.code === 200) return d.data ?? {};
        if (r.status === 402 || /balance|credit/i.test(String(d.detail ?? d.message ?? ""))) throw new Error("TikHub: hết tín dụng");
      } catch (e) {
        if (String(e).includes("hết tín dụng")) throw e;
      }
      await new Promise((s) => setTimeout(s, 1500));
    }
    return {};
  };

  const media: Promise<unknown>[] = [];
  const report: Record<string, unknown>[] = [];
  const cutoff = Date.now() / 1000 - DAYS * 86400;

  for (const ch of (chans ?? []) as Ch[]) {
    try {
      let sid = ch.sec_uid;
      if (!sid) {
        const p = ch.platform === "douyin" ? "/api/v1/douyin/web/get_sec_user_id" : "/api/v1/tiktok/web/get_sec_user_id";
        const d = await th(p, { url: ch.url });
        sid = typeof d === "string" ? d : (d.sec_user_id ?? d.sec_uid ?? "");
        if (!sid) throw new Error("Không đọc được ID kênh từ link");
      }
      const d = ch.platform === "douyin"
        ? await th("/api/v1/douyin/web/fetch_user_post_videos", { sec_user_id: sid, count: 20 })
        : await th("/api/v1/tiktok/app/v3/fetch_user_post_videos", { sec_user_id: sid, count: 20 });
      const list: any[] = d.aweme_list ?? [];
      const author = list[0]?.author ?? {};
      const patch: Record<string, unknown> = { sec_uid: sid, last_scraped_at: new Date().toISOString(), last_error: null };
      if (!ch.name && author.nickname) patch.name = author.nickname;
      const av = author.avatar_thumb?.url_list?.[0] ?? author.avatar_medium?.url_list?.[0];
      if (av) patch.avatar_url = av;
      if (author.follower_count) patch.followers = author.follower_count;
      await db.from("channels").update(patch).eq("id", ch.id);

      const rows: any[] = [];
      for (const a of list) {
        if (!a.aweme_id || (a.create_time ?? 0) < cutoff) continue;
        const st = a.statistics ?? {};
        const dur = Math.round(((a.duration ?? a.video?.duration ?? 0) as number) / 1000);
        if (dur && (dur < ch.min_sec || dur > ch.max_sec)) continue;
        const views = Number(st.play_count ?? 0);
        if (views > 0 && views < ch.min_views) continue;
        const uniq = a.author?.unique_id ?? "";
        rows.push({
          channel_id: ch.id, platform: ch.platform, aweme_id: String(a.aweme_id),
          caption_orig: a.desc ?? "", views, likes: Number(st.digg_count ?? 0), duration_sec: dur || null,
          posted_at: new Date((a.create_time ?? 0) * 1000).toISOString(),
          share_url: a.share_url || (ch.platform === "douyin"
            ? `https://www.douyin.com/video/${a.aweme_id}` : `https://www.tiktok.com/@${uniq}/video/${a.aweme_id}`),
          _a: a,
        });
      }
      rows.sort((x, y) => (y.views || y.likes * 20) - (x.views || x.likes * 20));
      const top = rows.slice(0, MAX_NEW_PER_CHANNEL);
      const { data: existing } = await db.from("feed_items").select("aweme_id")
        .eq("platform", ch.platform).in("aweme_id", top.map((r) => r.aweme_id));
      const have = new Set((existing ?? []).map((e: any) => e.aweme_id));
      let added = 0;
      for (const r of top) {
        const a = r._a; delete r._a;
        if (have.has(r.aweme_id)) {
          await db.from("feed_items").update({ views: r.views, likes: r.likes })
            .eq("platform", r.platform).eq("aweme_id", r.aweme_id);
          continue;
        }
        const { data: ins } = await db.from("feed_items").insert(r).select("id").single();
        if (!ins) continue;
        added++;
        media.push(saveMedia(db, ins.id, ch.platform, r.aweme_id, a));
      }
      report.push({ channel: patch.name ?? ch.name ?? ch.url, found: rows.length, added });
    } catch (e) {
      await db.from("channels").update({ last_error: String(e).slice(0, 300), last_scraped_at: new Date().toISOString() }).eq("id", ch.id);
      report.push({ channel: ch.name ?? ch.url, error: String(e) });
    }
  }
  // covers + previews keep downloading after we answer
  // @ts-ignore EdgeRuntime is provided by Supabase
  EdgeRuntime.waitUntil(Promise.allSettled(media));
  return json({ ok: true, channels: report });
});

async function grab(u: string, platform: string, limit: number): Promise<Uint8Array | null> {
  try {
    const r = await fetch(u, {
      headers: {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
        Referer: platform === "douyin" ? "https://www.douyin.com/" : "https://www.tiktok.com/",
      },
    });
    if (!r.ok) return null;
    const len = Number(r.headers.get("content-length") ?? 0);
    if (len && len > limit) return null;
    const b = new Uint8Array(await r.arrayBuffer());
    return b.byteLength > limit ? null : b;
  } catch { return null; }
}

function previewUrls(a: any): string[] {
  const v = a.video ?? {};
  const out: string[] = [];
  const rates = [...(v.bit_rate ?? [])].sort((x: any, y: any) => (x.bit_rate ?? 0) - (y.bit_rate ?? 0));
  for (const br of rates) out.push(...(br.play_addr?.url_list ?? []));
  for (const k of ["play_addr", "play_addr_h264", "download_addr"]) out.push(...(v[k]?.url_list ?? []));
  return out.filter((u) => typeof u === "string" && u.startsWith("http")).slice(0, 4);
}

async function saveMedia(db: any, id: string, platform: string, aid: string, a: any) {
  const patch: Record<string, string> = {};
  const covers = [a.video?.origin_cover, a.video?.cover, a.video?.dynamic_cover]
    .flatMap((c: any) => c?.url_list ?? []).filter((u: string) => u?.startsWith("http"));
  for (const c of covers.slice(0, 3)) {
    const b = await grab(c, platform, 3 * 1024 * 1024);
    if (b) {
      const p = `${platform}/${aid}.jpg`;
      const { error } = await db.storage.from("feed").upload(p, b, { contentType: "image/jpeg", upsert: true });
      if (!error) { patch.cover_path = p; break; }
    }
  }
  for (const u of previewUrls(a)) {
    const b = await grab(u, platform, MAX_PREVIEW_BYTES);
    if (b) {
      const p = `${platform}/${aid}.mp4`;
      const { error } = await db.storage.from("feed").upload(p, b, { contentType: "video/mp4", upsert: true });
      if (!error) { patch.preview_path = p; break; }
    }
  }
  if (Object.keys(patch).length) await db.from("feed_items").update(patch).eq("id", id);
}
