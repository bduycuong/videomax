// MAX WISE Studio – scrape the last 7 days of posts from watched channels via TikHub.
// Platforms: douyin, tiktok, xiaohongshu (RedNote), instagram, youtube.
// POST {channel_id?: string}  (Authorization: Bearer <member JWT>)
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const API = "https://api.tikhub.io";
const DAYS = 7;
const MAX_NEW_PER_CHANNEL = 12;
const MAX_PREVIEW_BYTES = 25 * 1024 * 1024;
const HEART_PLATFORMS = new Set(["douyin", "xiaohongshu"]); // ranked by hearts, not views
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

type Ch = {
  id: string; url: string; platform: string; name: string | null; sec_uid: string | null;
  min_views: number; min_sec: number; max_sec: number;
};
type Item = {
  id: string; caption: string; views: number; likes: number; dur: number; ts: number;
  share: string; covers: string[]; videos: string[]; embed?: string;
  author?: { name?: string; avatar?: string; followers?: number };
};

const REF: Record<string, string> = {
  douyin: "https://www.douyin.com/", tiktok: "https://www.tiktok.com/", xiaohongshu: "https://www.xiaohongshu.com/",
  instagram: "https://www.instagram.com/", youtube: "https://www.youtube.com/",
};

/* ---------- small helpers for loosely-typed responses ---------- */
const n = (v: unknown) => { const x = Number(v); return Number.isFinite(x) ? x : 0; };
function deepFind(o: any, pred: (k: string, v: any) => boolean, depth = 0): any {
  if (!o || typeof o !== "object" || depth > 7) return undefined;
  for (const [k, v] of Object.entries(o)) {
    if (pred(k, v)) return v;
    const r = deepFind(v, pred, depth + 1); if (r !== undefined) return r;
  }
  return undefined;
}
function deepList(o: any, keys: string[], depth = 0): any[] {
  if (!o || typeof o !== "object" || depth > 6) return [];
  for (const k of keys) if (Array.isArray(o[k]) && o[k].length && typeof o[k][0] === "object") return o[k];
  for (const v of Object.values(o)) { const r = deepList(v, keys, depth + 1); if (r.length) return r; }
  return [];
}
const urls = (o: any): string[] => {
  const out: string[] = [];
  const walk = (x: any, d = 0) => {
    if (d > 5 || !x) return;
    if (typeof x === "string") { if (x.startsWith("http")) out.push(x); return; }
    if (Array.isArray(x)) x.forEach((y) => walk(y, d + 1));
    else if (typeof x === "object") for (const [k, v] of Object.entries(x)) if (/url|src|master|backup/i.test(k) || Array.isArray(v) || typeof v === "object") walk(v, d + 1);
  };
  walk(o); return out;
};
function compact(s: string): number { // "1.2M views", "900K", "3,4 N", "12万"
  const m = String(s || "").replace(/,/g, ".").match(/([\d.]+)\s*([KkMmBb万亿]?)/);
  if (!m) return 0;
  const mult: Record<string, number> = { k: 1e3, m: 1e6, b: 1e9, "万": 1e4, "亿": 1e8 };
  return Math.round(parseFloat(m[1]) * (mult[m[2].toLowerCase()] || 1));
}
function relTime(s: string): number { // "6 days ago", "3 weeks ago", "2 hours ago"
  const m = String(s || "").match(/(\d+)\s*(second|minute|hour|day|week|month|year)/i);
  if (!m) return 0;
  const sec: Record<string, number> = { second: 1, minute: 60, hour: 3600, day: 86400, week: 604800, month: 2592000, year: 31536000 };
  return Date.now() / 1000 - Number(m[1]) * sec[m[2].toLowerCase()];
}
const hms = (s: string) => String(s || "").split(":").reduce((a, b) => a * 60 + n(b), 0);

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const anon = Deno.env.get("SUPABASE_ANON_KEY")!;
  const service = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const user = createClient(url, anon, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
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
    let last = "";
    for (let i = 0; i < 3; i++) {
      try {
        const r = await fetch(u, { headers: { Authorization: `Bearer ${token}` } });
        const d = await r.json();
        if (d.code === 200 && !(d.data && d.data.detail && Object.keys(d.data).length === 1)) return d.data ?? {};
        last = String(d.detail ?? d.message ?? r.status);
        if (r.status === 402 || /balance|credit|insufficient/i.test(last)) throw new Error("TikHub: hết tín dụng");
      } catch (e) {
        if (String(e).includes("hết tín dụng")) throw e;
        last = String(e);
      }
      await new Promise((s) => setTimeout(s, 1500));
    }
    throw new Error("TikHub lỗi: " + last.slice(0, 120));
  };

  /* ---------- platform adapters ---------- */
  async function fetchItems(ch: Ch): Promise<{ sid: string; items: Item[] }> {
    const link = ch.url;
    if (ch.platform === "douyin" || ch.platform === "tiktok") {
      let sid = ch.sec_uid ?? "";
      let params: Record<string, string | number> = { count: 20 };
      if (ch.platform === "tiktok" && !sid) {
        const h = link.match(/tiktok\.com\/@([\w.\-]+)/i)?.[1];
        if (h) { params.unique_id = h; sid = ""; }
      }
      if (!sid && !params.unique_id) {
        const m = ch.platform === "douyin" ? link.match(/\/user\/(MS4w[\w\-]+)/)?.[1] : undefined;
        if (m) sid = m;
        else {
          const d = await th(ch.platform === "douyin" ? "/api/v1/douyin/web/get_sec_user_id" : "/api/v1/tiktok/web/get_sec_user_id", { url: link });
          sid = typeof d === "string" ? d : (d.sec_user_id ?? d.sec_uid ?? "");
        }
        if (!sid) throw new Error("Không đọc được kênh từ link");
      }
      if (sid) params.sec_user_id = sid;
      const d = ch.platform === "douyin"
        ? await th("/api/v1/douyin/web/fetch_user_post_videos", params)
        : await th("/api/v1/tiktok/app/v3/fetch_user_post_videos", params);
      const list: any[] = d.aweme_list ?? [];
      if (!sid) sid = list[0]?.author?.sec_uid ?? "";
      return { sid, items: list.map((a) => {
        const st = a.statistics ?? {}; const v = a.video ?? {};
        const rates = [...(v.bit_rate ?? [])].sort((x: any, y: any) => (x.bit_rate ?? 0) - (y.bit_rate ?? 0));
        const uniq = a.author?.unique_id ?? "";
        return {
          id: String(a.aweme_id), caption: a.desc ?? "", views: n(st.play_count), likes: n(st.digg_count),
          dur: Math.round(n(a.duration ?? v.duration) / 1000), ts: n(a.create_time),
          share: ch.platform === "douyin" ? `https://www.douyin.com/video/${a.aweme_id}` : `https://www.tiktok.com/@${uniq}/video/${a.aweme_id}`,
          covers: [v.origin_cover, v.cover, v.dynamic_cover].flatMap((c: any) => c?.url_list ?? []),
          videos: [...rates.flatMap((b: any) => b.play_addr?.url_list ?? []), ...(v.play_addr?.url_list ?? []), ...(v.download_addr?.url_list ?? [])],
          author: { name: a.author?.nickname, avatar: a.author?.avatar_thumb?.url_list?.[0] ?? a.author?.avatar_medium?.url_list?.[0], followers: n(a.author?.follower_count) },
        } as Item;
      }) };
    }
    if (ch.platform === "instagram") {
      const username = ch.sec_uid || link.match(/instagram\.com\/(?!reel|p\/|stories)([\w.]+)/i)?.[1] || link.replace(/^@/, "").trim();
      if (!username) throw new Error("Không đọc được tên tài khoản Instagram");
      const d = await th("/api/v1/instagram/v2/fetch_user_reels", { username });
      const list: any[] = d?.data?.items ?? deepList(d, ["items"]);
      return { sid: username, items: list.map((x) => { const m = x.media ?? x; return {
        id: String(m.code ?? m.id), caption: m.caption?.text ?? "", views: n(m.play_count ?? m.ig_play_count ?? m.view_count), likes: n(m.like_count),
        dur: Math.round(n(m.video_duration)), ts: n(m.taken_at), share: `https://www.instagram.com/reel/${m.code}/`,
        covers: [m.thumbnail_url, ...(m.image_versions2?.candidates ?? m.image_versions?.items ?? []).map((c: any) => c.url), m.image_versions?.additional_items?.first_frame?.url].filter(Boolean),
        videos: [...(m.video_versions ?? [])].sort((p: any, q: any) => (p.width ?? 0) - (q.width ?? 0)).map((v: any) => v.url).concat(m.video_url ? [m.video_url] : []),
        author: { name: m.user?.full_name || m.user?.username, avatar: m.user?.profile_pic_url },
      } as Item; }) };
    }
    if (ch.platform === "youtube") {
      let cid = ch.sec_uid || link.match(/\/channel\/(UC[\w\-]{20,})/)?.[1] || "";
      if (!cid) { const d = await th("/api/v1/youtube/web_v2/get_channel_id", { channel_url: link }); cid = d.channel_id ?? ""; }
      if (!cid) throw new Error("Không đọc được kênh YouTube");
      const d = await th("/api/v1/youtube/web_v2/get_channel_videos", { channel_id: cid, language_code: "en", country_code: "US" });
      const chn = d.channel ?? {};
      return { sid: cid, items: (d.videos ?? []).map((v: any) => ({
        id: String(v.video_id), caption: v.title ?? "", views: compact(v.view_count), likes: 0, dur: hms(v.duration),
        ts: relTime(v.published_time), share: `https://www.youtube.com/watch?v=${v.video_id}`,
        covers: [v.thumbnail, ...(v.thumbnails ?? []).map((t: any) => t.url)].filter(Boolean), videos: [],
        embed: `https://www.youtube-nocookie.com/embed/${v.video_id}?autoplay=1&mute=1&playsinline=1&loop=1&playlist=${v.video_id}&controls=0&modestbranding=1`,
        author: { name: chn.name, avatar: chn.avatar },
      } as Item)) };
    }
    if (ch.platform === "xiaohongshu") {
      const uid = ch.sec_uid || link.match(/user\/profile\/([0-9a-f]{24})/i)?.[1] || "";
      const d = await th("/api/v1/xiaohongshu/app_v2/get_user_posted_notes", uid ? { user_id: uid } : { share_text: link });
      const list = deepList(d, ["notes", "items", "note_list", "data"]);
      const first = list[0] ?? {};
      const author = first.user ?? deepFind(d, (k, v) => k === "user" && v && typeof v === "object") ?? {};
      return { sid: uid || author.userid || author.user_id || author.id || "", items: list.filter((x) => {
        const t = String(x.type ?? x.note_type ?? x.model_type ?? "");
        return /video/i.test(t) || !!(x.video_info_v2 || x.video_info || x.video);
      }).map((x) => {
        const info = x.interact_info ?? {};
        const likes = n(x.likes ?? x.liked_count ?? x.like_count ?? info.liked_count ?? deepFind(x, (k) => /^(liked_count|likes)$/.test(k)));
        const vid = x.video_info_v2 ?? x.video_info ?? x.video ?? {};
        const vurls = urls(deepFind(vid, (k) => /^(h264|h265|stream|media)$/.test(k)) ?? vid).filter((u) => /\.mp4|sns-video|xhscdn/i.test(u));
        const id = String(x.note_id ?? x.id);
        return {
          id, caption: [x.display_title ?? x.title, x.desc].filter(Boolean).join(" · "), views: n(x.view_count ?? info.view_count), likes,
          dur: Math.round(n(deepFind(vid, (k) => k === "duration") ?? 0) > 1000 ? n(deepFind(vid, (k) => k === "duration")) / 1000 : n(deepFind(vid, (k) => k === "duration"))),
          ts: (() => { const t = n(x.time ?? x.create_time ?? x.timestamp ?? x.last_update_time); return t > 1e12 ? t / 1000 : t; })(),
          share: `https://www.xiaohongshu.com/explore/${id}`,
          covers: urls(x.cover ?? x.images_list?.[0] ?? x.image_list?.[0] ?? {}).slice(0, 3), videos: vurls.slice(0, 4),
          author: { name: (x.user ?? author).nickname ?? (x.user ?? author).name, avatar: (x.user ?? author).images ?? (x.user ?? author).avatar },
        } as Item;
      }) };
    }
    throw new Error("Nền tảng chưa hỗ trợ");
  }

  const media: Promise<unknown>[] = [];
  const report: Record<string, unknown>[] = [];
  const cutoff = Date.now() / 1000 - DAYS * 86400;

  for (const ch of (chans ?? []) as Ch[]) {
    try {
      const { sid, items } = await fetchItems(ch);
      const au = items.find((i) => i.author?.name)?.author ?? {};
      const patch: Record<string, unknown> = { sec_uid: sid || ch.sec_uid, last_scraped_at: new Date().toISOString(), last_error: null };
      if (!ch.name && au.name) patch.name = au.name;
      if (au.avatar) {
        const b = await grab(String(au.avatar), ch.platform, 2 * 1024 * 1024);
        if (b) {
          const ap = `avatars/${ch.id}.jpg`;
          const { error: ue } = await db.storage.from("feed").upload(ap, b, { contentType: "image/jpeg", upsert: true });
          if (!ue) patch.avatar_url = "sb:" + ap;
        }
      }
      if (au.followers) patch.followers = au.followers;
      await db.from("channels").update(patch).eq("id", ch.id);

      const hearts = HEART_PLATFORMS.has(ch.platform);
      const score = (i: Item) => hearts ? i.likes : (i.views || i.likes * 20);
      const rows = items.filter((i) => i.id && (!i.ts || i.ts >= cutoff))
        .filter((i) => !i.dur || (i.dur >= ch.min_sec && i.dur <= ch.max_sec))
        .filter((i) => { const s = hearts ? i.likes : i.views; return !s || s >= ch.min_views; })
        .sort((a, b) => score(b) - score(a)).slice(0, MAX_NEW_PER_CHANNEL);

      const { data: existing } = await db.from("feed_items").select("aweme_id")
        .eq("platform", ch.platform).in("aweme_id", rows.map((r) => r.id));
      const have = new Set((existing ?? []).map((e: any) => e.aweme_id));
      let added = 0;
      for (const it of rows) {
        if (have.has(it.id)) {
          await db.from("feed_items").update({ views: it.views, likes: it.likes }).eq("platform", ch.platform).eq("aweme_id", it.id);
          continue;
        }
        const { data: ins } = await db.from("feed_items").insert({
          channel_id: ch.id, platform: ch.platform, aweme_id: it.id, caption_orig: it.caption, views: it.views, likes: it.likes,
          duration_sec: it.dur || null, posted_at: new Date((it.ts || Date.now() / 1000) * 1000).toISOString(),
          share_url: it.share, embed_url: it.embed ?? null,
        }).select("id").single();
        if (!ins) continue;
        added++;
        media.push(saveMedia(db, ins.id, ch.platform, it));
      }
      report.push({ channel: patch.name ?? ch.name ?? ch.url, found: items.length, added });
    } catch (e) {
      await db.from("channels").update({ last_error: String(e).replace(/^Error:\s*/, "").slice(0, 300), last_scraped_at: new Date().toISOString() }).eq("id", ch.id);
      report.push({ channel: ch.name ?? ch.url, error: String(e).replace(/^Error:\s*/, "") });
    }
  }
  // @ts-ignore EdgeRuntime is provided by Supabase
  EdgeRuntime.waitUntil(Promise.allSettled(media));
  return json({ ok: true, channels: report });
});

async function grab(u: string, platform: string, limit: number): Promise<Uint8Array | null> {
  try {
    const r = await fetch(u, { headers: { "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15", Referer: REF[platform] ?? "" } });
    if (!r.ok) return null;
    const len = Number(r.headers.get("content-length") ?? 0);
    if (len && len > limit) return null;
    const b = new Uint8Array(await r.arrayBuffer());
    return b.byteLength > limit || b.byteLength < 1000 ? null : b;
  } catch { return null; }
}

async function saveMedia(db: any, id: string, platform: string, it: Item) {
  const patch: Record<string, string> = {};
  const key = `${platform}/${it.id.replace(/[^\w\-]/g, "_")}`;
  for (const c of it.covers.filter((u) => u?.startsWith("http")).slice(0, 3)) {
    const b = await grab(c, platform, 3 * 1024 * 1024);
    if (b) { const { error } = await db.storage.from("feed").upload(`${key}.jpg`, b, { contentType: "image/jpeg", upsert: true }); if (!error) { patch.cover_path = `${key}.jpg`; break; } }
  }
  for (const u of it.videos.filter((u) => u?.startsWith("http")).slice(0, 4)) {
    const b = await grab(u, platform, MAX_PREVIEW_BYTES);
    if (b) { const { error } = await db.storage.from("feed").upload(`${key}.mp4`, b, { contentType: "video/mp4", upsert: true }); if (!error) { patch.preview_path = `${key}.mp4`; break; } }
  }
  if (Object.keys(patch).length) await db.from("feed_items").update(patch).eq("id", id);
}
