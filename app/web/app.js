/* MAX WISE Studio – iPhone web app (vanilla JS + Supabase) */
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm";

const SUPA_URL = "https://tygucovkjqfzbxftyvny.supabase.co";
const SUPA_KEY = "sb_publishable_ozl1RjUe3LtgO6PYXg2crQ_66Ws_NPD";
const sb = createClient(SUPA_URL, SUPA_KEY, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } });

const $app = document.getElementById("app");
const S = { session: null, member: false, channels: [], chMap: {} };

/* ---------- helpers ---------- */
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const num = (n) => { n = Number(n || 0); if (n >= 1e6) return (n / 1e6).toFixed(1).replace(".", ",").replace(",0", "") + " tr"; if (n >= 1e3) return Math.round(n / 1e3) + " N"; return String(n); };
const dur = (s) => s ? `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}` : "";
const ago = (t) => { const d = (Date.now() - new Date(t)) / 864e5; if (d < 1) { const h = Math.max(1, Math.round(d * 24)); return `${h} giờ trước`; } return `${Math.floor(d)} ngày trước`; };
const tz = "Asia/Ho_Chi_Minh";
const vnDate = (d = new Date()) => new Intl.DateTimeFormat("en-CA", { timeZone: tz }).format(d); // YYYY-MM-DD
const vnTime = (t) => new Intl.DateTimeFormat("vi-VN", { timeZone: tz, hour: "2-digit", minute: "2-digit" }).format(new Date(t));
const dayStart = (ymd) => new Date(`${ymd}T00:00:00+07:00`).toISOString();
const addDays = (ymd, n) => { const d = new Date(`${ymd}T12:00:00+07:00`); d.setUTCDate(d.getUTCDate() + n); return vnDate(d); };
const weekday = ["CN", "T2", "T3", "T4", "T5", "T6", "T7"];
const toast = (m, ms = 2600) => { const t = document.createElement("div"); t.className = "toast"; t.textContent = m; document.body.appendChild(t); setTimeout(() => t.remove(), ms); };
const grad = (seed) => { const hues = [28, 200, 150, 350, 265, 45, 190, 10]; let h = 0; for (const c of String(seed)) h = (h * 31 + c.charCodeAt(0)) >>> 0; const a = hues[h % hues.length]; return `linear-gradient(160deg,hsl(${a} 35% 62%),hsl(${a} 40% 24%))`; };

const signedCache = new Map();
async function signed(bucket, paths, opts) {
  const need = paths.filter((p) => p && !signedCache.has(bucket + p));
  if (need.length) {
    const { data } = await sb.storage.from(bucket).createSignedUrls(need, 3600, opts);
    (data || []).forEach((d) => d.signedUrl && signedCache.set(bucket + d.path, d.signedUrl));
  }
  const out = {}; paths.forEach((p) => { if (p) out[p] = signedCache.get(bucket + p); }); return out;
}

const I = {
  home: '<path d="M3 10.5 12 4l9 6.5V20H3z"/><path d="M9.5 20v-6h5v6"/>',
  ch: '<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="M10 9v6l5-3z"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  bst: '<path d="M6 3h12v18l-6-4-6 4z"/>',
  dl: '<path d="M12 3v12M7 10l5 5 5-5M4 20h16"/>',
  back: '<path d="M15 5l-7 7 7 7"/>',
  cal: '<rect x="3" y="5" width="18" height="16" rx="1.5"/><path d="M3 10h18M8 3v4M16 3v4"/>',
  check: '<path d="M5 12l5 5L20 7"/>',
  x: '<path d="M6 6l12 12M18 6L6 18"/>',
  ext: '<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
  share: '<path d="M12 15V3M7 8l5-5 5 5"/><path d="M5 12v8h14v-8"/>',
  refresh: '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
  chev: '<path d="M9 6l6 6-6 6"/>',
  sound: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6"/>',
  mute: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M17 9l4 6M21 9l-4 6"/>',
  out: '<path d="M15 4h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-4"/><path d="M10 16l-4-4 4-4M6 12h10"/>',
};
const ic = (n, s = 22, w = 2) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${I[n]}</svg>`;

function nav(on) {
  const it = (h, k, icon, label) => `<a href="#/${h}" class="${on === k ? "on" : ""}" ${on === k ? 'aria-current="page"' : ""}>${ic(icon)}${label}</a>`;
  return `<nav class="nav" aria-label="Điều hướng chính">${it("home", "home", "home", "Hôm nay")}${it("channels", "channels", "ch", "Kênh")}
  <a href="#/produce" class="fab ${on === "produce" ? "on" : ""}" aria-label="Lệnh sản xuất">${ic("plus", 24, 2.4)}</a>
  ${it("bst", "bst", "bst", "BST")}${it("library", "library", "dl", "Kho")}</nav>`;
}
function page({ top, body, navOn, dark = false }) {
  $app.className = dark ? "dark" : "";
  $app.innerHTML = `${top || ""}${body}${navOn === null ? "" : nav(navOn)}`;
}
const backTop = (title, href, right = "") => `<header class="top"><div class="row"><a href="${href}" class="icon" aria-label="Quay lại">${ic("back", 18, 2.4)}</a><h1 class="h2">${esc(title)}</h1>${right}</div></header>`;

async function loadChannels() {
  const { data } = await sb.from("channels").select("*").order("created_at");
  S.channels = data || []; S.chMap = Object.fromEntries(S.channels.map((c) => [c.id, c]));
}

/* ---------- auth ---------- */
function viewLogin(mode = "in", msg = "") {
  page({
    navOn: null, body: `<main class="main" style="padding:calc(env(safe-area-inset-top) + 64px) 24px 32px;background:#FFF;gap:24px">
    <div style="display:flex;flex-direction:column;gap:14px">
      <img src="icon.svg" width="56" height="56" alt="Max" style="border-radius:10px">
      <div><h1 class="h1" style="font-size:28px">MAX WISE Studio</h1>
      <p class="sub" style="font-size:15px;margin-top:6px">${mode === "up" ? "Tạo mật khẩu cho tài khoản đã được mời." : "Đăng nhập để quản lý kênh, lệnh sản xuất và video."}</p></div>
    </div>
    <form id="f" style="display:flex;flex-direction:column;gap:16px">
      <label class="lbl" style="display:flex;flex-direction:column;gap:6px">Email<input class="inp" type="email" name="email" autocomplete="username" required placeholder="ban@vienchibao.com"></label>
      <label class="lbl" style="display:flex;flex-direction:column;gap:6px">Mật khẩu<input class="inp" type="password" name="pw" autocomplete="${mode === "up" ? "new-password" : "current-password"}" required minlength="8" placeholder="Ít nhất 8 ký tự"></label>
      ${msg ? `<p style="margin:0;color:#B91C1C;font-size:13px;font-weight:600">${esc(msg)}</p>` : ""}
      <button class="btn btn-full" id="go">${mode === "up" ? "Tạo mật khẩu và vào" : "Đăng nhập"}</button>
      <button type="button" class="lk" id="sw" style="align-self:center">${mode === "up" ? "Đã có mật khẩu? Đăng nhập" : "Lần đầu dùng? Tạo mật khẩu"}</button>
    </form>
    <p class="sub" style="margin-top:auto;text-align:center;font-size:12px;color:#A1A1AA">iPhone sẽ hỏi lưu mật khẩu, lần sau đăng nhập bằng Face ID.<br>Chỉ tài khoản được mời mới truy cập được.</p>
  </main>`,
  });
  document.getElementById("sw").onclick = () => viewLogin(mode === "up" ? "in" : "up");
  document.getElementById("f").onsubmit = async (e) => {
    e.preventDefault();
    const f = new FormData(e.target); const email = f.get("email").trim().toLowerCase(); const password = f.get("pw");
    const b = document.getElementById("go"); b.disabled = true; b.innerHTML = '<span class="spin"></span>';
    if (mode === "up") {
      const { error } = await sb.auth.signUp({ email, password });
      if (error && !/registered/i.test(error.message)) return viewLogin("up", error.message);
    }
    const { error } = await sb.auth.signInWithPassword({ email, password });
    if (error) return viewLogin(mode, /Invalid login/i.test(error.message) ? "Sai email hoặc mật khẩu." : error.message);
  };
}

/* ---------- home ---------- */
async function viewHome() {
  page({ navOn: "home", top: `<header class="top"><div class="row between" style="align-items:flex-end"><div><p class="sub">${weekday[new Date().getDay()]}, ${new Intl.DateTimeFormat("vi-VN", { timeZone: tz, day: "2-digit", month: "2-digit" }).format(new Date())}</p><h1 class="h1">Chào ${esc((S.session.user.email || "").split("@")[0].replace(/^./, (c) => c.toUpperCase()))}</h1></div>
    <div class="row" style="gap:8px"><a href="#/schedule" class="icon" aria-label="Lịch chạy">${ic("cal", 18)}</a><button class="icon" id="lo" aria-label="Đăng xuất">${ic("out", 18)}</button></div></div></header>`,
    body: `<main class="main" id="m"><div class="empty"><span class="spin" style="display:inline-block"></span></div></main>` });
  document.getElementById("lo").onclick = async () => { if (confirm("Đăng xuất khỏi MAX WISE Studio?")) await sb.auth.signOut(); };
  const since = new Date(Date.now() - 7 * 864e5).toISOString();
  const today = vnDate();
  const [nNew, nWait, nProc, ex, hot] = await Promise.all([
    sb.from("feed_items").select("id", { count: "exact", head: true }).gte("scraped_at", since),
    sb.from("feed_items").select("id", { count: "exact", head: true }).eq("status", "new").gte("posted_at", since),
    sb.from("jobs").select("id", { count: "exact", head: true }).in("status", ["queued", "downloading", "editing", "rendering"]),
    sb.from("exports").select("*").gte("created_at", dayStart(today)).order("created_at"),
    sb.rpc("feed_today", { p_limit: 3 }),
  ]);
  const exs = ex.data || []; const hots = hot.data || [];
  const th = await signed("exports", exs.map((e) => e.thumb_path));
  const cov = await signed("feed", hots.map((h) => h.cover_path));
  const m = document.getElementById("m"); if (!m) return;
  m.innerHTML = `
  <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px">
    <a href="#/channels" class="card stat"><b>${nNew.count ?? 0}</b><small>Video mới từ kênh · 7 ngày</small></a>
    <a href="#/feed" class="card stat" style="border-color:#18181B"><b>${nWait.count ?? 0}</b><small>Chờ bạn duyệt</small></a>
    <a href="#/bst" class="card stat"><b>${nProc.count ?? 0}</b><small>Trong BST đang xử lý</small></a>
  </div>
  <section class="card"><div class="hd"><span class="ht">Video xuất hôm nay</span>${exs.length ? `<span class="tag ok">✓ ${exs.length} video</span>` : `<span class="tag">Chưa có</span>`}</div>
    ${exs.length ? `<div style="padding:12px 14px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px">${exs.slice(0, 3).map((e) => `<a href="#/library" style="display:flex;flex-direction:column;gap:6px"><div class="th" style="aspect-ratio:9/16;background-image:url('${th[e.thumb_path] || ""}'),${grad(e.id)}"><span>${dur(e.duration_sec)}</span></div><span style="font-size:12px;font-weight:600;line-height:1.3">${esc(e.title)}</span></a>`).join("")}</div>`
      : `<div class="empty">Sáng mai Max sẽ làm và gửi lúc 7:55.</div>`}
  </section>
  <section class="card"><div class="hd"><span class="ht">Video hot chờ duyệt</span><a href="#/feed" class="lk">Lướt tất cả</a></div>
    ${hots.length ? hots.map((h) => `<div class="row" style="padding:10px 14px;border-bottom:1px solid #F4F4F5;gap:12px" data-id="${h.id}">
      <div class="th" style="width:44px;height:78px;background-image:url('${cov[h.cover_path] || ""}'),${grad(h.id)}"></div>
      <div style="flex:1;min-width:0"><div style="font-size:14px;font-weight:600;line-height:1.3;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical">${esc(h.caption_vi || h.caption_orig || "(không có caption)")}</div>
      <div class="vm">${esc(S.chMap[h.channel_id]?.name || "")} · <b style="color:#18181B">${h.views ? num(h.views) + " view" : num(h.likes) + " thích"}</b></div></div>
      <button class="btn btn-y sm" data-ap="${h.id}">Duyệt</button></div>`).join("")
      : `<div class="empty">${S.channels.length ? "Chưa có video mới. Kéo sang tab Kênh để cào ngay." : "Chưa có kênh nào. <a href='#/add' class='lk'>Thêm kênh đầu tiên</a>"}</div>`}
  </section>`;
  m.querySelectorAll("[data-ap]").forEach((b) => b.onclick = async () => { b.disabled = true; await approve(hots.find((x) => x.id === b.dataset.ap)); b.closest("[data-id]").remove(); });
}

/* ---------- approve / skip ---------- */
async function approve(item) {
  const ch = S.chMap[item.channel_id] || {};
  const kind = ch.use_original ? "footage" : "idea";
  const { error } = await sb.from("feed_items").update({ status: "approved", approved_at: new Date().toISOString() }).eq("id", item.id);
  if (error) return toast("Lỗi: " + error.message);
  await sb.from("jobs").insert({ kind, feed_item_id: item.id, topic: item.caption_vi || item.caption_orig, run_when: "next_morning" });
  toast(kind === "footage" ? "Đã thêm vào BST · Max sẽ tải về và sửa" : "Đã thêm vào BST · Max sẽ làm doodle từ ý tưởng này");
}
const skip = (item) => sb.from("feed_items").update({ status: "skipped" }).eq("id", item.id);

/* ---------- channels ---------- */
async function viewChannels() {
  page({ navOn: "channels", top: `<header class="top"><div class="row between"><h1 class="h1">Kênh nguồn</h1><a href="#/add" class="btn sm">${ic("plus", 16, 2.4)}Thêm kênh</a></div></header>`,
    body: `<main class="main" id="m"><div class="empty"><span class="spin" style="display:inline-block"></span></div></main>` });
  await loadChannels();
  const since = new Date(Date.now() - 7 * 864e5).toISOString();
  const { data: items } = await sb.from("feed_items").select("channel_id,status,views,likes").gte("posted_at", since);
  const agg = {}; (items || []).forEach((i) => { const a = (agg[i.channel_id] ||= { n: 0, wait: 0, top: 0 }); a.n++; if (i.status === "new") a.wait++; a.top = Math.max(a.top, i.views || 0); });
  const last = S.channels.map((c) => c.last_scraped_at).filter(Boolean).sort().pop();
  const m = document.getElementById("m"); if (!m) return;
  m.innerHTML = `
  <div class="card row" style="padding:12px 14px;gap:12px">${ic("refresh", 22)}<div style="flex:1"><div style="font-size:14px;font-weight:700">Tự cào mỗi sáng 5:30</div><div class="vm">Lấy video 7 ngày gần nhất${last ? " · lần cuối " + vnTime(last) + " " + new Intl.DateTimeFormat("vi-VN", { timeZone: tz, day: "2-digit", month: "2-digit" }).format(new Date(last)) : ""}</div></div>
  <button class="btn btn-o sm" id="sc" ${S.channels.length ? "" : "disabled"}>Cào ngay</button></div>
  <div class="row between" style="padding:0 2px"><span class="sec">${S.channels.length} kênh · ${(items || []).length} video / 7 ngày</span><a href="#/feed" class="lk">Lướt video →</a></div>
  <section class="card" style="overflow:hidden">${S.channels.length ? S.channels.map((c) => {
    const a = agg[c.id] || { n: 0, wait: 0, top: 0 };
    return `<div class="ch" data-c="${c.id}"><div class="av" style="${c.avatar_url ? `background-image:url('${esc(c.avatar_url)}')` : `background:${grad(c.id)}`}">${c.avatar_url ? "" : esc((c.name || c.platform)[0].toUpperCase())}</div>
    <div style="flex:1;min-width:0"><div style="font-size:15px;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(c.name || c.url)}</div>
    <div class="vm">${c.platform === "douyin" ? "Douyin" : "TikTok"} · ${a.n} video / 7 ngày${a.top ? " · top " + num(a.top) : ""}</div>
    <div class="row" style="gap:6px;margin-top:6px;flex-wrap:wrap">${c.use_original ? '<span class="tag ok">Dùng video gốc</span>' : '<span class="tag">Lấy ý tưởng → doodle</span>'}${a.wait ? `<span class="tag yl">${a.wait} chờ duyệt</span>` : ""}${c.last_error ? '<span class="tag bad">Lỗi lần cào trước</span>' : ""}${c.active ? "" : '<span class="tag">Đang tắt</span>'}</div></div>
    <span style="color:#A1A1AA">${ic("chev", 18, 2.2)}</span></div>`;
  }).join("") : `<div class="empty">Chưa có kênh nào.<br><br><a href="#/add" class="btn sm">Thêm kênh đầu tiên</a></div>`}</section>`;
  document.getElementById("sc").onclick = () => runScrape();
  m.querySelectorAll("[data-c]").forEach((el) => el.onclick = () => channelSheet(S.chMap[el.dataset.c]));
}

async function runScrape(channel_id) {
  toast("Đang cào… có thể mất 10–40 giây", 4000);
  const { data, error } = await sb.functions.invoke("scrape", { body: channel_id ? { channel_id } : {} });
  if (error) { toast("Cào lỗi: " + (error.message || error)); return null; }
  const added = (data.channels || []).reduce((s, c) => s + (c.added || 0), 0);
  const errs = (data.channels || []).filter((c) => c.error);
  toast(errs.length ? `Thêm ${added} video · ${errs.length} kênh lỗi: ${errs[0].error}` : `Đã thêm ${added} video mới. Ảnh và video xem trước đang tải…`, 4500);
  if (location.hash.startsWith("#/channels")) viewChannels();
  return data;
}

function channelSheet(c) {
  const el = document.createElement("div"); el.className = "sheet";
  el.innerHTML = `<div><div class="row" style="margin-bottom:14px"><div style="flex:1;min-width:0"><div style="font-size:17px;font-weight:800">${esc(c.name || "Kênh")}</div><div class="vm" style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(c.url)}</div></div><button class="icon" data-x aria-label="Đóng">${ic("x", 18)}</button></div>
  ${c.last_error ? `<p class="tag bad" style="height:auto;padding:6px 8px;white-space:normal;margin:0 0 12px">${esc(c.last_error)}</p>` : ""}
  <div class="card" style="margin-bottom:12px">
    <label class="li"><span>Dùng video gốc để sửa<small>Kênh của bạn hoặc chủ kênh đã đồng ý</small></span><input type="checkbox" class="sw" data-k="use_original" ${c.use_original ? "checked" : ""}></label>
    <label class="li"><span>Tự cào mỗi sáng</span><input type="checkbox" class="sw" data-k="auto_scrape" ${c.auto_scrape ? "checked" : ""}></label>
    <label class="li"><span>Kênh đang bật</span><input type="checkbox" class="sw" data-k="active" ${c.active ? "checked" : ""}></label>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
    <a class="btn" href="#/feed?ch=${c.id}">Lướt video kênh</a><button class="btn btn-o" data-s>Cào ngay</button>
    <a class="btn btn-o" href="${esc(c.url)}" target="_blank" rel="noopener">Mở kênh gốc</a><button class="btn btn-o" data-del style="color:#B91C1C">Xoá kênh</button>
  </div></div>`;
  document.body.appendChild(el);
  const close = () => el.remove();
  el.onclick = (e) => { if (e.target === el || e.target.closest("[data-x]") || e.target.closest("a")) close(); };
  el.querySelectorAll("[data-k]").forEach((i) => i.onchange = async () => { await sb.from("channels").update({ [i.dataset.k]: i.checked }).eq("id", c.id); c[i.dataset.k] = i.checked; toast("Đã lưu"); });
  el.querySelector("[data-s]").onclick = () => { close(); runScrape(c.id); };
  el.querySelector("[data-del]").onclick = async () => { if (!confirm("Xoá kênh này và các video đã cào của kênh?")) return; await sb.from("channels").delete().eq("id", c.id); close(); viewChannels(); };
  el.addEventListener("change", () => { if (location.hash.startsWith("#/channels")) setTimeout(viewChannels, 50); });
}

/* ---------- add channel ---------- */
function viewAdd() {
  page({ navOn: "channels", top: backTop("Thêm kênh", "#/channels"), body: `<main class="main"><form id="f" style="display:flex;flex-direction:column;gap:10px">
    <div class="card" style="padding:12px 14px;display:flex;flex-direction:column;gap:10px">
      <label class="lbl" style="display:flex;flex-direction:column;gap:6px">Link kênh<input class="inp" name="url" type="url" required placeholder="https://www.douyin.com/user/…" inputmode="url" autocapitalize="off"></label>
      <div class="seg" role="radiogroup" aria-label="Nền tảng" id="pf"><button type="button" data-v="douyin" class="on">Douyin</button><button type="button" data-v="tiktok">TikTok</button></div>
      <label class="lbl" style="display:flex;flex-direction:column;gap:6px">Tên gợi nhớ <span style="font-weight:500;color:#71717A">(tuỳ chọn, để trống sẽ lấy tên kênh)</span><input class="inp" name="name" type="text"></label>
    </div>
    <span class="sec">Cào tự động</span>
    <div class="card">
      <label class="li"><span>Tự cào video mới<small>Mỗi sáng 5:30, quét 7 ngày gần nhất</small></span><input type="checkbox" class="sw" name="auto" checked></label>
      <label class="li"><span>Chỉ lấy video từ</span><select name="minv"><option value="0">Mọi lượt view</option><option value="100000" selected>100 N view</option><option value="500000">500 N view</option><option value="1000000">1 tr view</option></select></label>
      <label class="li"><span>Độ dài video</span><select name="dur"><option value="20-300" selected>20 giây – 5 phút</option><option value="10-60">Dưới 60 giây</option><option value="20-600">Đến 10 phút</option></select></label>
      <label class="li"><span>Tối đa đưa vào BST</span><select name="mpw"><option>2</option><option selected>3</option><option>5</option><option>7</option></select></label>
    </div>
    <span class="sec">Cách dùng</span>
    <div class="card">
      <label class="li"><span>Dùng video gốc để sửa<small>Kênh của bạn hoặc chủ kênh đã đồng ý</small></span><input type="checkbox" class="sw" name="orig"></label>
      <div style="padding:10px 14px 12px;display:flex;flex-direction:column;gap:8px"><span class="vm" style="margin:0;line-height:1.4">Tắt: Max chỉ lấy ý tưởng từ video hot rồi làm doodle mới bằng lời của Max.</span>
      <input class="inp" name="credit" type="text" placeholder="Ghi công trong caption (tuỳ chọn)" aria-label="Ghi công"></div>
    </div>
    <button class="btn btn-full" id="go" style="margin-top:6px">Lưu và cào 7 ngày ngay</button>
  </form></main>` });
  let pf = "douyin";
  const segs = [...document.querySelectorAll("#pf button")];
  const setPf = (v) => { pf = v; segs.forEach((b) => b.classList.toggle("on", b.dataset.v === v)); };
  segs.forEach((b) => b.onclick = () => setPf(b.dataset.v));
  const f = document.getElementById("f");
  f.url.oninput = () => { const u = f.url.value; if (/tiktok\.com/i.test(u)) setPf("tiktok"); else if (/douyin\.com|iesdouyin/i.test(u)) setPf("douyin"); };
  f.onsubmit = async (e) => {
    e.preventDefault();
    const url = (f.url.value.match(/https?:\/\/\S+/) || [f.url.value])[0].trim();
    const [a, b] = f.dur.value.split("-").map(Number);
    const go = document.getElementById("go"); go.disabled = true; go.innerHTML = '<span class="spin" style="border-top-color:#FFF"></span>';
    const { data, error } = await sb.from("channels").insert({ url, platform: pf, name: f.name.value.trim() || null, auto_scrape: f.auto.checked,
      min_views: Number(f.minv.value), min_sec: a, max_sec: b, max_per_week: Number(f.mpw.value), use_original: f.orig.checked, credit: f.credit.value.trim() || null }).select().single();
    if (error) { go.disabled = false; go.textContent = "Lưu và cào 7 ngày ngay"; return toast("Lỗi: " + error.message); }
    await loadChannels();
    location.hash = "#/channels";
    runScrape(data.id);
  };
}

/* ---------- feed (Douyin-style) ---------- */
let feedObs = null;
async function viewFeed(params) {
  const chId = params.get("ch") || "";
  page({ navOn: "channels", dark: true, body: `<div style="flex:1;position:relative;display:flex;flex-direction:column;min-height:0;background:#000">
    <div class="ftop"><a href="#/channels" class="pill" aria-label="Kênh">${ic("ch", 18)}</a>
      <div class="row" style="gap:18px"><button class="ftab ${chId ? "" : "on"}" data-t="">Hôm nay</button><button class="ftab ${chId ? "on" : ""}" data-t="ch">Theo kênh</button></div>
      <span class="pill" id="cnt">…</span></div>
    <div class="fhint" id="hint">Đang tải…</div>
    <div class="feed" id="feed"></div></div>` });
  await loadChannels();
  document.querySelectorAll(".ftab").forEach((b) => b.onclick = () => {
    if (!b.dataset.t) { location.hash = "#/feed"; return; }
    pickChannel((id) => (location.hash = "#/feed?ch=" + id));
  });
  const [{ data: items, error }, hidden] = await Promise.all([
    sb.rpc("feed_today", { p_channel: chId || null, p_limit: 200 }),
    sb.from("feed_items").select("id", { count: "exact", head: true }).neq("status", "new").gte("posted_at", new Date(Date.now() - 7 * 864e5).toISOString()),
  ]);
  const feed = document.getElementById("feed"); if (!feed) return;
  if (error) { feed.innerHTML = `<div class="fdone">${esc(error.message)}</div>`; return; }
  const list = items || [];
  document.getElementById("hint").textContent = `${chId ? esc(S.chMap[chId]?.name || "Kênh") + " · " : ""}Thứ tự trộn mới mỗi ngày · đã ẩn ${hidden.count || 0} video đã làm/bỏ qua`;
  const cnt = document.getElementById("cnt");
  if (!list.length) { feed.innerHTML = `<div class="fdone">${ic("check", 40)}<div>Hết video chờ duyệt rồi.</div><div style="font-size:12px">Video mới sẽ có sau lượt cào 5:30 sáng mai, hoặc vào Kênh → Cào ngay.</div></div>`; cnt.textContent = "0 / 0"; return; }
  let rendered = 0, muted = true, done = 0;
  const total = list.length;
  const cardHTML = (it, i) => {
    const ch = S.chMap[it.channel_id] || {};
    const vi = it.caption_vi;
    return `<section class="fi" data-i="${i}" data-id="${it.id}" style="background-image:${grad(it.id)}">
      <video playsinline muted loop preload="none" data-src="${esc(it.preview_path || "")}" data-poster="${esc(it.cover_path || "")}"></video>
      <div class="shade"></div>
      <div class="rail">
        <button class="rb ok" data-a="ap"><i>${ic("check", 24, 2.8)}</i>Duyệt</button>
        <button class="rb" data-a="sk"><i>${ic("x", 22, 2.4)}</i>Bỏ qua</button>
        <button class="rb" data-a="lang"><i>${vi ? "VI" : "中"}</i>${vi ? "Xem gốc" : "Chưa dịch"}</button>
        <button class="rb" data-a="snd"><i>${ic("mute", 22)}</i>Âm thanh</button>
        <a class="rb" href="${esc(it.share_url || ch.url || "#")}" target="_blank" rel="noopener"><i>${ic("ext", 22)}</i>Mở gốc</a>
      </div>
      <div class="info">
        <div class="row" style="gap:8px"><span class="av" style="width:28px;height:28px;font-size:12px;border-radius:4px;${ch.avatar_url ? `background-image:url('${esc(ch.avatar_url)}')` : `background:${grad(ch.id)}`}">${ch.avatar_url ? "" : esc((ch.name || "?")[0])}</span>
          <span style="font-size:15px;font-weight:800;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:150px">${esc(ch.name || "Kênh")}</span>
          ${ch.use_original ? '<span class="tag" style="background:rgba(255,212,59,.2);color:#FFD43B">Dùng video gốc</span>' : '<span class="tag" style="background:rgba(255,255,255,.15);color:#FFF">Lấy ý tưởng</span>'}</div>
        <p data-cap>${esc(vi || it.caption_orig || "(không có caption)")}</p>
        ${vi ? `<p class="orig" data-orig hidden>Gốc: ${esc(it.caption_orig)}</p>` : `<p class="orig">Caption sẽ được dịch trong lượt chạy sáng.</p>`}
        <div class="meta"><span>▶ ${it.views ? num(it.views) : "—"}</span><span>♥ ${num(it.likes)}</span>${it.duration_sec ? `<span>${dur(it.duration_sec)}</span>` : ""}<span>${ago(it.posted_at)}</span></div>
      </div></section>`;
  };
  const media = async (from, to) => {
    const slice = list.slice(from, to);
    const [pv, cv] = await Promise.all([signed("feed", slice.map((x) => x.preview_path)), signed("feed", slice.map((x) => x.cover_path))]);
    slice.forEach((x, k) => {
      const sec = feed.querySelector(`[data-i="${from + k}"]`); if (!sec) return;
      if (cv[x.cover_path]) sec.style.backgroundImage = `url('${cv[x.cover_path]}'),${grad(x.id)}`;
      const v = sec.querySelector("video");
      if (pv[x.preview_path]) v.dataset.url = pv[x.preview_path];
      if (cv[x.cover_path]) v.poster = cv[x.cover_path];
    });
  };
  const more = async () => {
    if (rendered >= total) return;
    const to = Math.min(total, rendered + 8);
    feed.insertAdjacentHTML("beforeend", list.slice(rendered, to).map((it, k) => cardHTML(it, rendered + k)).join(""));
    const from = rendered; rendered = to;
    if (rendered >= total) feed.insertAdjacentHTML("beforeend", `<div class="fdone">${ic("check", 40)}<div>Đã xem hết ${total} video hôm nay.</div><a class="btn btn-y sm" href="#/bst">Xem bộ sưu tập</a></div>`);
    feed.querySelectorAll(`.fi:not([data-obs])`).forEach((s) => { s.dataset.obs = 1; feedObs.observe(s); });
    await media(from, to);
  };
  if (feedObs) feedObs.disconnect();
  feedObs = new IntersectionObserver((ents) => {
    ents.forEach((en) => {
      const v = en.target.querySelector("video"); if (!v) return;
      if (en.isIntersecting && en.intersectionRatio > 0.6) {
        const i = Number(en.target.dataset.i);
        cnt.textContent = `${[...feed.querySelectorAll(".fi")].indexOf(en.target) + 1} / ${total - done}`;
        if (v.dataset.url && !v.src) v.src = v.dataset.url;
        v.muted = muted; v.play().catch(() => {});
        if (i >= rendered - 3) more();
      } else { v.pause(); }
    });
  }, { root: feed, threshold: [0, 0.6, 1] });
  await more();
  feed.onclick = async (e) => {
    const sec = e.target.closest(".fi"); if (!sec) return;
    const it = list[Number(sec.dataset.i)];
    const btn = e.target.closest("[data-a]");
    if (!btn) { const v = sec.querySelector("video"); if (v.src) { v.paused ? v.play() : v.pause(); } return; }
    const a = btn.dataset.a;
    if (a === "lang") { const p = sec.querySelector("[data-cap]"), o = sec.querySelector("[data-orig]"); if (!o) return toast("Caption gốc chưa dịch"); const showO = o.hidden; o.hidden = !showO; p.textContent = showO ? it.caption_orig : it.caption_vi; btn.lastChild.textContent = showO ? "Xem dịch" : "Xem gốc"; return; }
    if (a === "snd") { muted = !muted; feed.querySelectorAll("video").forEach((v) => (v.muted = muted)); feed.querySelectorAll('[data-a="snd"] i').forEach((i) => (i.innerHTML = ic(muted ? "mute" : "sound", 22))); return; }
    btn.disabled = true;
    (a === "ap" ? approve(it) : skip(it).then(() => toast("Đã bỏ qua")));
    const v = sec.querySelector("video"); if (v) { v.pause(); v.removeAttribute("src"); v.load(); }
    const top = sec.offsetTop; feedObs.unobserve(sec); sec.remove(); done++;
    feed.scrollTop = top;
    const left = total - done; cnt.textContent = left ? `còn ${left}` : "0";
    const cur = [...feed.querySelectorAll(".fi")].find((s) => s.offsetTop === top);
    if (cur) { const cv = cur.querySelector("video"); if (cv.dataset.url && !cv.src) cv.src = cv.dataset.url; cv.muted = muted; cv.play().catch(() => {}); }
  };
}

function pickChannel(cb) {
  const el = document.createElement("div"); el.className = "sheet";
  el.innerHTML = `<div><div class="row between" style="margin-bottom:12px"><b style="font-size:17px">Chọn kênh</b><button class="icon" data-x aria-label="Đóng">${ic("x", 18)}</button></div>
  <div class="card">${S.channels.map((c) => `<button class="li" style="width:100%;background:none;border:0;border-bottom:1px solid #F4F4F5;text-align:left;cursor:pointer" data-c="${c.id}"><span>${esc(c.name || c.url)}</span>${ic("chev", 16)}</button>`).join("") || '<div class="empty">Chưa có kênh</div>'}</div></div>`;
  document.body.appendChild(el);
  el.onclick = (e) => { const b = e.target.closest("[data-c]"); if (b) { el.remove(); cb(b.dataset.c); } else if (e.target === el || e.target.closest("[data-x]")) el.remove(); };
}

/* ---------- collection ---------- */
const STEPS = [["downloading", "Tải về"], ["editing", "Cắt, che chữ"], ["rendering", "Lồng Max"], ["ready", "Sẵn sàng"]];
async function viewBst(params) {
  const tab = params.get("t") || "proc";
  page({ navOn: "bst", top: `<header class="top"><div><h1 class="h1">Bộ sưu tập</h1><p class="sub">Video đã duyệt · Max tự tải về và sửa thành bản có Max</p></div></header>`,
    body: `<main class="main" id="m"><div class="empty"><span class="spin" style="display:inline-block"></span></div></main>` });
  await loadChannels();
  const [{ data: jobs }, { data: st }] = await Promise.all([
    sb.from("jobs").select("*, feed_items(caption_vi,caption_orig,cover_path,views,likes,channel_id)").neq("status", "cancelled").order("created_at", { ascending: false }).limit(100),
    sb.from("settings").select("auto_edit").eq("id", 1).single(),
  ]);
  const all = jobs || [];
  const groups = { proc: all.filter((j) => ["downloading", "editing", "rendering"].includes(j.status)), wait: all.filter((j) => j.status === "queued"), done: all.filter((j) => ["ready", "failed"].includes(j.status)) };
  const cov = await signed("feed", all.map((j) => j.feed_items?.cover_path));
  const m = document.getElementById("m"); if (!m) return;
  const kindTag = (j) => j.kind === "footage" ? '<span class="tag inf">Sửa video gốc</span>' : j.kind === "idea" ? '<span class="tag">Doodle từ ý tưởng</span>' : '<span class="tag yl">Doodle</span>';
  const card = (j) => {
    const f = j.feed_items || {}; const idx = STEPS.findIndex((s) => s[0] === j.status);
    return `<div style="padding:12px;display:flex;flex-direction:column;gap:10px;border-bottom:1px solid #F4F4F5">
    <div class="row" style="gap:12px;align-items:flex-start"><div class="th" style="width:44px;height:78px;background-image:url('${cov[f.cover_path] || ""}'),${grad(j.id)}"></div>
    <div style="flex:1;min-width:0"><div class="row between" style="gap:8px;align-items:flex-start"><span class="vt" style="overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical">${esc(j.topic || f.caption_vi || f.caption_orig || "Video")}</span>${j.status === "failed" ? '<span class="tag bad">Lỗi</span>' : j.status === "ready" ? '<span class="tag ok">✓ Sẵn sàng</span>' : j.progress ? `<span class="tag yl">${j.progress}%</span>` : ""}</div>
    <div class="vm">${esc(S.chMap[f.channel_id]?.name || "")}${f.views ? " · " + num(f.views) + " view" : ""} · ${vnTime(j.created_at)} ${new Intl.DateTimeFormat("vi-VN", { timeZone: tz, day: "2-digit", month: "2-digit" }).format(new Date(j.created_at))}</div>
    <div class="row" style="gap:6px;margin-top:6px;flex-wrap:wrap">${kindTag(j)}${j.run_when === "now" && j.status === "queued" ? '<span class="tag yl">Làm ngay</span>' : ""}${j.step ? `<span class="vm" style="margin:0">${esc(j.step)}</span>` : ""}</div>
    ${j.error ? `<div class="vm" style="color:#B91C1C">${esc(j.error)}</div>` : ""}
    ${j.status === "queued" ? `<div class="row" style="gap:6px;margin-top:8px">${j.run_when === "now" ? "" : `<button class="btn btn-y xs" data-now="${j.id}">Làm ngay</button>`}<button class="btn btn-o xs" data-cancel="${j.id}">Gỡ khỏi BST</button></div>` : ""}
    ${j.status === "ready" ? `<div class="row" style="gap:6px;margin-top:8px"><a class="btn xs" href="#/library">Xem trong Kho</a><button class="btn btn-o xs" data-redo="${j.id}">Sửa lại</button></div>` : ""}
    ${j.status === "failed" ? `<div class="row" style="gap:6px;margin-top:8px"><button class="btn btn-o xs" data-redo="${j.id}">Thử lại</button></div>` : ""}
    </div></div>
    ${j.kind === "footage" && idx >= 0 && j.status !== "ready" ? `<div class="steps">${STEPS.map((s, k) => `<div class="${k < idx ? "d" : k === idx ? "c" : ""}"><i></i>${s[1]}</div>`).join("")}</div>` : ""}
    </div>`;
  };
  m.innerHTML = `
  <div class="card row" style="padding:10px 14px;gap:10px"><div style="flex:1"><div style="font-size:13px;font-weight:700">Sửa tự động mỗi sáng</div><div class="vm">Che chữ gốc · phụ đề EN · Max dẫn chuyện</div></div>
    <input type="checkbox" class="sw" id="ae" ${st?.auto_edit ? "checked" : ""} aria-label="Bật sửa tự động"></div>
  <div class="seg" role="tablist"><button class="${tab === "proc" ? "on" : ""}" data-t="proc">Đang xử lý · ${groups.proc.length}</button><button class="${tab === "wait" ? "on" : ""}" data-t="wait">Chờ · ${groups.wait.length}</button><button class="${tab === "done" ? "on" : ""}" data-t="done">Xong · ${groups.done.length}</button></div>
  <section class="card" style="overflow:hidden">${groups[tab].length ? groups[tab].map(card).join("") : `<div class="empty">${tab === "wait" ? "Chưa có video nào chờ. Vào <a class='lk' href='#/feed'>Lướt video</a> để duyệt." : tab === "proc" ? "Không có video nào đang xử lý. Max làm vào 5:31 mỗi sáng." : "Chưa có video nào xong."}</div>`}</section>`;
  m.querySelectorAll("[data-t]").forEach((b) => b.onclick = () => (location.hash = "#/bst?t=" + b.dataset.t));
  document.getElementById("ae").onchange = async (e) => { await sb.from("settings").update({ auto_edit: e.target.checked }).eq("id", 1); toast("Đã lưu"); };
  m.querySelectorAll("[data-now]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ run_when: "now", updated_at: new Date().toISOString() }).eq("id", b.dataset.now); toast("Max sẽ làm trong lượt kiểm tra kế tiếp (tối đa 1 giờ)"); viewBst(params); });
  m.querySelectorAll("[data-cancel]").forEach((b) => b.onclick = async () => { const j = all.find((x) => x.id === b.dataset.cancel); await sb.from("jobs").update({ status: "cancelled" }).eq("id", j.id); if (j.feed_item_id) await sb.from("feed_items").update({ status: "new" }).eq("id", j.feed_item_id); toast("Đã gỡ, video trở lại màn lướt"); viewBst(params); });
  m.querySelectorAll("[data-redo]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ status: "queued", progress: 0, step: null, error: null, run_when: "now" }).eq("id", b.dataset.redo); toast("Đã xếp làm lại"); viewBst(params); });
}

/* ---------- produce ---------- */
const IDEAS = ["Why does the Moon follow your car?", "Are you more bacteria than human?", "You're sitting still. How fast are you moving?", "Why is the sky blue but sunsets red?", "How many times does your heart beat in a lifetime?"];
function viewProduce() {
  page({ navOn: "produce", top: `<header class="top"><h1 class="h1">Lệnh sản xuất</h1></header>`, body: `<main class="main"><form id="f" style="display:flex;flex-direction:column;gap:10px">
    <div class="card" style="padding:12px 14px;display:flex;flex-direction:column;gap:8px">
      <label class="lbl" for="topic">Câu hỏi tò mò (tiếng Anh hoặc tiếng Việt)</label>
      <input id="topic" class="inp" name="topic" required placeholder="Why does the Moon follow your car?">
      <div class="row" style="gap:6px;flex-wrap:wrap">${IDEAS.slice(0, 3).map((t) => `<button type="button" class="btn btn-o xs" data-idea="${esc(t)}" style="font-weight:600">${esc(t.length > 30 ? t.slice(0, 28) + "…" : t)}</button>`).join("")}</div>
    </div>
    <span class="sec">Tuỳ chọn</span>
    <div class="card">
      <label class="li"><span>Giọng đọc</span><select name="voice"><option value="en-US-AndrewMultilingualNeural">Andrew · nam US</option><option value="en-US-BrianMultilingualNeural">Brian · nam US</option></select></label>
      <label class="li"><span>Phụ đề</span><select name="subs"><option value="en+vi">EN + VI</option><option value="en">Chỉ EN</option></select></label>
      <label class="li"><span>Nhạc nền + SFX</span><input type="checkbox" class="sw" name="music" checked></label>
      <label class="li"><span>Gửi Telegram khi xong</span><input type="checkbox" class="sw" name="tg" checked></label>
    </div>
    <span class="sec">Thời điểm</span>
    <div class="seg" id="when"><button type="button" data-v="now" class="on">Làm ngay</button><button type="button" data-v="next_morning">Xếp vào sáng mai</button></div>
    <span class="vm" id="wh" style="padding:0 2px">Max kiểm tra lệnh mới mỗi giờ (7:00–23:00). Một video doodle mất khoảng 25–35 phút.</span>
    <button class="btn btn-full" style="margin-top:8px" id="go">Gửi lệnh sản xuất</button>
  </form>
  <section class="card" id="q"></section></main>` });
  let when = "now";
  document.querySelectorAll("#when button").forEach((b) => b.onclick = () => { when = b.dataset.v; document.querySelectorAll("#when button").forEach((x) => x.classList.toggle("on", x === b)); document.getElementById("wh").textContent = when === "now" ? "Max kiểm tra lệnh mới mỗi giờ (7:00–23:00). Một video doodle mất khoảng 25–35 phút." : "Làm trong lượt 5:31 sáng mai, gửi cùng các video khác lúc 7:55."; });
  const f = document.getElementById("f");
  f.querySelectorAll("[data-idea]").forEach((b) => b.onclick = () => (f.topic.value = b.dataset.idea));
  f.onsubmit = async (e) => {
    e.preventDefault();
    const { error } = await sb.from("jobs").insert({ kind: "doodle", topic: f.topic.value.trim(), voice: f.voice.value, subs: f.subs.value, music: f.music.checked, telegram: f.tg.checked, run_when: when });
    if (error) return toast("Lỗi: " + error.message);
    toast("Đã gửi lệnh · theo dõi trong BST"); f.topic.value = ""; loadQueue();
  };
  const loadQueue = async () => {
    const { data } = await sb.from("jobs").select("id,topic,run_when,status,created_at").eq("kind", "doodle").in("status", ["queued", "downloading", "editing", "rendering"]).order("created_at");
    const q = document.getElementById("q"); if (!q) return;
    q.innerHTML = `<div class="hd"><span class="ht">Lệnh doodle đang chờ</span><span class="tag">${(data || []).length}</span></div>${(data || []).map((j) => `<div class="li"><span style="flex:1;min-width:0">${esc(j.topic)}<small>${j.status === "queued" ? (j.run_when === "now" ? "Làm ngay" : "Sáng mai") : "Đang làm…"}</small></span>${j.status === "queued" ? `<button class="btn btn-o xs" data-c="${j.id}">Huỷ</button>` : '<span class="spin"></span>'}</div>`).join("") || '<div class="empty">Chưa có lệnh nào.</div>'}`;
    q.querySelectorAll("[data-c]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ status: "cancelled" }).eq("id", b.dataset.c); loadQueue(); });
  };
  loadQueue();
}

/* ---------- schedule ---------- */
async function viewSchedule() {
  page({ navOn: "home", top: backTop("Lịch chạy", "#/home", `<label class="row" style="gap:8px;font-size:13px;font-weight:700;color:#166534">Đang bật<input type="checkbox" class="sw" id="en" style="accent-color:#16A34A"></label>`),
    body: `<main class="main" id="m"><div class="empty"><span class="spin" style="display:inline-block"></span></div></main>` });
  const [{ data: s }, { data: runs }] = await Promise.all([sb.from("settings").select("*").eq("id", 1).single(), sb.from("runs").select("*").order("created_at", { ascending: false }).limit(10)]);
  const m = document.getElementById("m"); if (!m || !s) return;
  document.getElementById("en").checked = s.enabled;
  const numSel = (k, opts) => `<div class="seg" style="width:auto" data-k="${k}">${opts.map((o) => `<button type="button" style="width:38px;height:32px" data-v="${o}" class="${s[k] === o ? "on" : ""}">${o}</button>`).join("")}</div>`;
  m.innerHTML = `<span class="sec">Mỗi sáng (giờ Việt Nam)</span>
  <div class="card">
    <div class="li"><span style="display:flex;gap:12px;align-items:center"><b style="width:48px;font-size:17px">${s.scrape_time}</b><span>Cào kênh nguồn<small>Video 7 ngày gần nhất, xếp theo view</small></span></span></div>
    <div class="li"><span style="display:flex;gap:12px;align-items:center"><b style="width:48px;font-size:17px">${s.produce_time}</b><span>Sản xuất<small>Doodle + video đã duyệt trong BST</small></span></span></div>
    <div class="li"><span style="display:flex;gap:12px;align-items:center"><b style="width:48px;font-size:17px;background:#FFD43B;border-radius:3px;text-align:center">${s.send_time}</b><span>Gửi Telegram<small>Video kèm caption + hashtag tiếng Anh</small></span></span></div>
  </div>
  <span class="sec">Số lượng</span>
  <div class="card">
    <div class="li"><span>Doodle mỗi ngày</span>${numSel("doodles_per_day", [0, 1, 2, 3])}</div>
    <div class="li"><span>Video từ BST mỗi ngày</span>${numSel("footage_per_day", [0, 1, 2, 3])}</div>
    <div class="li" style="border-bottom:0"><span>Ngày chạy</span></div>
    <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px;padding:0 14px 12px" id="days">${[1, 2, 3, 4, 5, 6, 0].map((d) => `<button type="button" data-d="${d}" class="btn ${s.days.includes(d) ? "" : "btn-o"}" style="height:34px;padding:0;font-size:12px">${weekday[d]}</button>`).join("")}</div>
  </div>
  <span class="sec">Lịch sử</span>
  <div class="card">${(runs || []).map((r) => `<div class="li" style="font-size:13px"><span class="row" style="gap:10px"><span style="width:8px;height:8px;border-radius:2px;background:${r.status === "ok" ? "#16A34A" : "#F59E0B"}"></span>${r.run_date.split("-").reverse().slice(0, 2).join("/")} · ${r.videos} video${r.redone ? `, ${r.redone} làm lại` : ""}</span><span class="vm" style="margin:0">${r.sent_at ? "gửi " + vnTime(r.sent_at) : esc(r.note || "")}</span></div>`).join("") || '<div class="empty">Chưa có lượt chạy nào được ghi.</div>'}</div>`;
  const save = async (patch) => { Object.assign(s, patch); const { error } = await sb.from("settings").update({ ...patch, updated_at: new Date().toISOString() }).eq("id", 1); toast(error ? "Lỗi: " + error.message : "Đã lưu"); };
  document.getElementById("en").onchange = (e) => save({ enabled: e.target.checked });
  m.querySelectorAll("[data-k]").forEach((g) => g.onclick = (e) => { const b = e.target.closest("[data-v]"); if (!b) return; g.querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b)); save({ [g.dataset.k]: Number(b.dataset.v) }); });
  document.getElementById("days").onclick = (e) => { const b = e.target.closest("[data-d]"); if (!b) return; const d = Number(b.dataset.d); const days = s.days.includes(d) ? s.days.filter((x) => x !== d) : [...s.days, d]; b.classList.toggle("btn-o"); save({ days }); };
}

/* ---------- library (exports) ---------- */
async function viewLibrary(params) {
  const today = vnDate();
  const f = params.get("d") || "today";
  let from, to, label;
  if (f === "today") { from = today; to = addDays(today, 1); label = "Hôm nay"; }
  else if (f === "yesterday") { from = addDays(today, -1); to = today; label = "Hôm qua"; }
  else if (f === "7d") { from = addDays(today, -6); to = addDays(today, 1); label = "7 ngày"; }
  else { from = f; to = addDays(f, 1); label = f.split("-").reverse().join("/"); }
  page({ navOn: "library", top: `<header class="top"><div class="row between" style="align-items:baseline"><h1 class="h1">Video đã xuất</h1><span class="sub" id="tot"></span></div>
    <div class="row" style="gap:6px">${[["today", "Hôm nay"], ["yesterday", "Hôm qua"], ["7d", "7 ngày"]].map(([k, l]) => `<a href="#/library?d=${k}" class="btn xs ${f === k ? "" : "btn-o"}" style="font-weight:600">${l}</a>`).join("")}
    <label class="btn xs ${/^\d{4}/.test(f) ? "" : "btn-o"}" style="position:relative;font-weight:600">${ic("cal", 14)}${/^\d{4}/.test(f) ? label : "Chọn ngày"}<input type="date" id="dp" max="${today}" style="position:absolute;inset:0;opacity:0"></label></div></header>`,
    body: `<main class="main" id="m"><div class="empty"><span class="spin" style="display:inline-block"></span></div></main>` });
  document.getElementById("dp").onchange = (e) => e.target.value && (location.hash = "#/library?d=" + e.target.value);
  const [{ data }, { count }] = await Promise.all([
    sb.from("exports").select("*").gte("created_at", dayStart(from)).lt("created_at", dayStart(to)).order("created_at", { ascending: false }),
    sb.from("exports").select("id", { count: "exact", head: true }),
  ]);
  const list = data || [];
  document.getElementById("tot").textContent = `${count || 0} video`;
  const th = await signed("exports", list.map((e) => e.thumb_path));
  const m = document.getElementById("m"); if (!m) return;
  if (!list.length) { m.innerHTML = `<div class="empty">Không có video xuất ${label.toLowerCase()}.</div>`; return; }
  const byDay = {}; list.forEach((e) => (byDay[vnDate(new Date(e.created_at))] ||= []).push(e));
  m.innerHTML = Object.entries(byDay).map(([d, arr]) => `<span class="sec">${d === today ? "Hôm nay · " : d === addDays(today, -1) ? "Hôm qua · " : ""}${d.split("-").reverse().slice(0, 2).join("/")}</span>` + arr.map((e) => `
    <article class="card row" style="padding:12px;gap:12px;align-items:stretch" data-e="${e.id}">
      <div class="th" style="width:72px;height:128px;background-image:url('${th[e.thumb_path] || ""}'),${grad(e.id)}"><span>${dur(e.duration_sec)}</span></div>
      <div style="flex:1;min-width:0;display:flex;flex-direction:column">
        <div class="vt">${esc(e.title)}</div>
        <div class="vm">${e.kind === "doodle" ? "Doodle" : "Từ BST"} · xuất ${vnTime(e.created_at)}${e.size_bytes ? " · " + Math.round(e.size_bytes / 1048576) + " MB" : ""}${e.posted ? " · <b style='color:#166534'>✓ đã đăng</b>" : ""}</div>
        <div class="cap">${esc(e.caption || "")}</div>
        <div class="row" style="gap:6px;margin-top:auto;padding-top:8px">
          <button class="btn btn-o xs" data-a="copy">Copy caption</button>
          <button class="btn xs" data-a="dl">${ic("dl", 14, 2.6)}Tải</button>
          <button class="btn btn-o xs" data-a="share" aria-label="Chia sẻ">${ic("share", 14, 2.2)}</button>
        </div>
      </div></article>`).join("")).join("");
  m.onclick = async (ev) => {
    const b = ev.target.closest("[data-a]"); if (!b) return;
    const e = list.find((x) => x.id === b.closest("[data-e]").dataset.e);
    const fname = (e.title || "maxwise").replace(/[^\w\- ]+/g, "").trim().replace(/\s+/g, "-").toLowerCase() + ".mp4";
    if (b.dataset.a === "copy") {
      try { await navigator.clipboard.writeText(e.caption || ""); } catch { const t = document.createElement("textarea"); t.value = e.caption || ""; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); }
      b.textContent = "✓ Đã copy"; b.classList.add("ok"); setTimeout(() => { b.textContent = "Copy caption"; b.classList.remove("ok"); }, 1800);
    } else if (b.dataset.a === "dl") {
      const { data: s } = await sb.storage.from("exports").createSignedUrl(e.video_path, 3600, { download: fname });
      if (s?.signedUrl) location.href = s.signedUrl;
    } else {
      b.innerHTML = '<span class="spin"></span>';
      const { data: s } = await sb.storage.from("exports").createSignedUrl(e.video_path, 3600);
      try {
        const blob = await (await fetch(s.signedUrl)).blob();
        const file = new File([blob], fname, { type: "video/mp4" });
        if (navigator.canShare && navigator.canShare({ files: [file] })) await navigator.share({ files: [file], text: e.caption || "" });
        else if (navigator.share) await navigator.share({ url: s.signedUrl, text: e.caption || "" });
        else { await navigator.clipboard.writeText(s.signedUrl); toast("Đã copy link video (hết hạn sau 1 giờ)"); }
        if (!e.posted) await sb.from("exports").update({ posted: true }).eq("id", e.id);
      } catch (err) { if (err?.name !== "AbortError") toast("Không chia sẻ được: " + err.message); }
      b.innerHTML = ic("share", 14, 2.2);
    }
  };
}

/* ---------- router ---------- */
const routes = { home: viewHome, channels: viewChannels, add: viewAdd, feed: viewFeed, bst: viewBst, produce: viewProduce, schedule: viewSchedule, library: viewLibrary };
async function route() {
  if (!S.session) return viewLogin();
  if (!S.member) {
    page({ navOn: null, body: `<main class="main" style="justify-content:center;text-align:center;padding:40px 24px"><h1 class="h2" style="flex:none">Tài khoản chưa được mời</h1><p class="sub">${esc(S.session.user.email)} chưa có quyền vào MAX WISE Studio.</p><button class="btn" id="lo" style="margin-top:16px">Đăng xuất</button></main>` });
    document.getElementById("lo").onclick = () => sb.auth.signOut(); return;
  }
  const h = location.hash.replace(/^#\/?/, "");
  if (/access_token|error_description/.test(h)) { history.replaceState(null, "", "#/home"); }
  const [name, qs] = (location.hash.replace(/^#\/?/, "") || "home").split("?");
  if (!S.channels.length && name !== "add") await loadChannels();
  if (feedObs && name !== "feed") { feedObs.disconnect(); feedObs = null; }
  (routes[name] || viewHome)(new URLSearchParams(qs || ""));
}
window.addEventListener("hashchange", route);
sb.auth.onAuthStateChange(async (ev, session) => {
  const was = S.session?.user?.id; S.session = session;
  if (!session) { S.member = false; S.channels = []; return viewLogin(); }
  if (was !== session.user.id || ev === "SIGNED_IN") {
    const { data } = await sb.rpc("is_member"); S.member = !!data;
    if (ev === "SIGNED_IN" && /login|^$/.test(location.hash.replace(/^#\/?/, ""))) location.hash = "#/home";
    route();
  }
});
(async () => {
  const { data } = await sb.auth.getSession();
  if (!data.session) viewLogin();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})();
