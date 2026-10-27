// MAX WISE Studio – Web Push to every subscribed phone when a job finishes.
// Called by the DB trigger private.job_done_notify (header x-notify-secret) with {job_id},
// or by a member with {test: true} to send a test notification.
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";
import webpush from "npm:web-push@3.6.7";

const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const db = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: cfg } = await db.rpc("push_config");
  if (!cfg?.vapid_private) return json({ error: "push not configured" }, 500);
  let body: { job_id?: string; test?: boolean } = {};
  try { body = await req.json(); } catch { /* empty */ }

  if (req.headers.get("x-notify-secret") !== cfg.notify_secret) {
    const user = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
    const { data: ok } = await user.rpc("is_member");
    if (!ok) return json({ error: "forbidden" }, 403);
  }

  let msg = { title: "MAX WISE", body: "Thông báo đã bật ✓", url: "#/home", tag: "test" };
  if (body.job_id) {
    const { data: j } = await db.from("jobs").select("id,status,topic,error,kind,feed_items(caption_vi,caption_orig)").eq("id", body.job_id).single();
    if (!j) return json({ error: "job not found" }, 404);
    const name = (j.topic || j.feed_items?.caption_vi || j.feed_items?.caption_orig || "Video").slice(0, 120);
    msg = j.status === "ready"
      ? { title: "✓ Video đã xong", body: name, url: "#/library", tag: j.id }
      : { title: "✗ Video bị lỗi", body: `${name}${j.error ? " — " + j.error : ""}`.slice(0, 180), url: "#/bst?t=done", tag: j.id };
  }

  webpush.setVapidDetails("mailto:cuong@vienchibao.com", cfg.vapid_public, cfg.vapid_private);
  const { data: subs } = await db.from("push_subs").select("endpoint,sub");
  let sent = 0;
  await Promise.all((subs ?? []).map(async (s: any) => {
    try { await webpush.sendNotification(s.sub, JSON.stringify(msg), { TTL: 86400, urgency: "high" }); sent++; }
    catch (e: any) { if (e?.statusCode === 404 || e?.statusCode === 410) await db.from("push_subs").delete().eq("endpoint", s.endpoint); else console.error("push fail", e?.statusCode, e?.body); }
  }));
  return json({ ok: true, sent, subs: subs?.length ?? 0 });
});
