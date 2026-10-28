// MAX WISE Studio – "Dung lượng" page: storage, API balances, cleanup.
// POST {}                                   -> stats (storage, DB, DeepSeek + TikHub balance/usage)
// POST {clean: "feed", days: 7|15|30}       -> delete media of scraped videos older than N days (keeps approved ones)
// POST {clean: "exports", days: 15|30}      -> delete exported videos older than N days
// POST {clean: "orphans"}                   -> delete files in `feed` no row points to
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

async function removeAll(db: any, bucket: string, paths: string[]) {
  let n = 0;
  for (let i = 0; i < paths.length; i += 100) {
    const { data, error } = await db.storage.from(bucket).remove(paths.slice(i, i + 100));
    if (error) throw error; n += data?.length ?? 0;
  }
  return n;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const user = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
  const { data: ok } = await user.rpc("is_member");
  if (!ok) return json({ error: "forbidden" }, 403);
  const db = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  let body: { clean?: string; days?: number } = {};
  try { body = await req.json(); } catch { /* empty */ }

  try {
    if (body.clean === "feed") {
      const days = [7, 15, 30].includes(Number(body.days)) ? Number(body.days) : 30;
      const before = new Date(Date.now() - days * 864e5).toISOString();
      const { data: rows } = await db.from("feed_items").select("id,status,cover_path,preview_path,subs_path").lt("scraped_at", before).neq("status", "approved")
        .or("cover_path.not.is.null,preview_path.not.is.null,subs_path.not.is.null").limit(2000);
      const paths = (rows ?? []).flatMap((r: any) => [r.cover_path, r.preview_path, r.subs_path]).filter(Boolean);
      const files = await removeAll(db, "feed", paths);
      const ids = (rows ?? []).map((r: any) => r.id);
      for (let i = 0; i < ids.length; i += 200) {
        await db.from("feed_items").update({ cover_path: null, preview_path: null, subs_path: null }).in("id", ids.slice(i, i + 200));
        await db.from("feed_items").update({ status: "skipped" }).in("id", ids.slice(i, i + 200)).eq("status", "new");
      }
      return json({ ok: true, videos: ids.length, files });
    }
    if (body.clean === "exports") {
      const days = [15, 30].includes(Number(body.days)) ? Number(body.days) : 30;
      const before = new Date(Date.now() - days * 864e5).toISOString();
      const { data: rows } = await db.from("exports").select("id,video_path,thumb_path").lt("created_at", before).limit(2000);
      const files = await removeAll(db, "exports", (rows ?? []).flatMap((r: any) => [r.video_path, r.thumb_path]).filter(Boolean));
      const ids = (rows ?? []).map((r: any) => r.id);
      if (ids.length) { await db.from("jobs").update({ export_id: null }).in("export_id", ids); await db.from("exports").delete().in("id", ids); }
      return json({ ok: true, videos: ids.length, files });
    }
    if (body.clean === "orphans") {
      const { data: names } = await db.rpc("orphan_files");
      const files = await removeAll(db, "feed", (names ?? []).map((x: any) => typeof x === "string" ? x : x.orphan_files));
      return json({ ok: true, files });
    }

    // stats
    const [{ data: st, error: se }, { data: keys }] = await Promise.all([user.rpc("storage_stats"), db.rpc("ext_keys")]);
    if (se) throw se;
    const out: Record<string, unknown> = { storage: st, limits: { storage: 1024 ** 3, db: 500 * 1024 ** 2, plan: "free" } };
    const ds = keys?.deepseek_key ? fetch("https://api.deepseek.com/user/balance", { headers: { Authorization: `Bearer ${keys.deepseek_key}` } }).then((r) => r.json()).catch(() => null) : null;
    const th = (p: string) => keys?.tikhub_token ? fetch("https://api.tikhub.io" + p, { headers: { Authorization: `Bearer ${keys.tikhub_token}` } }).then((r) => r.json()).catch(() => null) : null;
    const vn = (d: number) => new Date(Date.now() + 7 * 36e5 - d * 864e5).toISOString().slice(0, 10);
    const [dsb, thi, td, ty] = await Promise.all([ds, th("/api/v1/tikhub/user/get_user_info"), th(`/api/v1/tikhub/user/get_user_daily_usage?date=${vn(0)}`), th(`/api/v1/tikhub/user/get_user_daily_usage?date=${vn(1)}`)]);
    const bi = dsb?.balance_infos?.[0];
    out.deepseek = bi ? { balance: Number(bi.total_balance), currency: bi.currency, available: dsb.is_available } : null;
    out.tikhub = { balance: thi?.user_data?.balance ?? null, today: td?.data ? { usd: td.data.usage, req: td.data.total_request_per_day } : null, yesterday: ty?.data ? { usd: ty.data.usage, req: ty.data.total_request_per_day } : null };
    return json(out);
  } catch (e) {
    return json({ error: String((e as any)?.message ?? e) }, 500);
  }
});
