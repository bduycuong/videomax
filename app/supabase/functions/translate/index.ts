// MAX WISE Studio – translate to Vietnamese with DeepSeek.
// POST {}                 -> translate pending feed captions (caption_vi is null), up to 40
// POST {ids: uuid[]}      -> translate those feed captions
// POST {texts: string[]}  -> return {vi: string[]} (subtitle lines for the video engine)
// Authorization: Bearer <member JWT>
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json" } });

const SYS_CAPTION = "You translate short-video captions into natural, concise Vietnamese. Keep the meaning and tone; drop hashtags, @mentions, sponsor/brand campaign tags and emojis. Keep numbers. Return only JSON.";
const SYS_SUBS = "You translate video subtitle lines into natural spoken Vietnamese. Translate each line on its own, keep it short enough to read on screen, keep numbers and names, never merge or split lines. Return only JSON.";

async function deepseek(key: string, sys: string, lines: string[]): Promise<string[]> {
  const user = `Translate each item of this JSON array into Vietnamese. Answer with {"vi": [...]} containing exactly ${lines.length} strings in the same order.\n${JSON.stringify(lines)}`;
  for (let i = 0; i < 3; i++) {
    const r = await fetch("https://api.deepseek.com/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${key}` },
      body: JSON.stringify({ model: "deepseek-chat", temperature: 0.2, response_format: { type: "json_object" },
        messages: [{ role: "system", content: sys }, { role: "user", content: user }] }),
    });
    if (r.status === 401) throw new Error("DeepSeek: API key không hợp lệ");
    if (r.status === 402) throw new Error("DeepSeek: hết tiền trong tài khoản");
    if (r.ok) {
      const d = await r.json();
      try {
        const out = JSON.parse(d.choices?.[0]?.message?.content ?? "{}").vi;
        if (Array.isArray(out) && out.length === lines.length) return out.map((x: unknown) => String(x ?? "").trim());
      } catch { /* retry */ }
    }
    await new Promise((s) => setTimeout(s, 1200));
  }
  throw new Error("DeepSeek: không dịch được");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const url = Deno.env.get("SUPABASE_URL")!;
  const user = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
  const { data: ok } = await user.rpc("is_member");
  if (!ok) return json({ error: "not a member" }, 403);
  const db = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: key } = await db.rpc("deepseek_key");
  if (!key) return json({ error: "Chưa có DeepSeek API key" }, 400);

  let body: { ids?: string[]; texts?: string[] } = {};
  try { body = await req.json(); } catch { /* empty */ }

  try {
    if (Array.isArray(body.texts)) {
      const texts = body.texts.map((t) => String(t ?? ""));
      const vi: string[] = [];
      for (let i = 0; i < texts.length; i += 60) vi.push(...await deepseek(key, SYS_SUBS, texts.slice(i, i + 60)));
      return json({ vi });
    }
    let q = db.from("feed_items").select("id,caption_orig").is("caption_vi", null).neq("caption_orig", "");
    q = body.ids?.length ? q.in("id", body.ids.slice(0, 60)) : q.eq("status", "new").order("scraped_at", { ascending: false }).limit(40);
    const { data: rows, error } = await q;
    if (error) return json({ error: error.message }, 500);
    const list = (rows ?? []).filter((r: any) => (r.caption_orig ?? "").trim());
    if (!list.length) return json({ translated: 0, items: [] });
    const vi = await deepseek(key, SYS_CAPTION, list.map((r: any) => r.caption_orig.slice(0, 600)));
    const items = list.map((r: any, i: number) => ({ id: r.id, caption_vi: vi[i] })).filter((x) => x.caption_vi);
    await Promise.all(items.map((x) => db.from("feed_items").update({ caption_vi: x.caption_vi }).eq("id", x.id)));
    return json({ translated: items.length, items });
  } catch (e) {
    return json({ error: String(e).replace(/^Error:\s*/, "") }, 502);
  }
});
