/* MAX WISE Studio – iPhone web app (vanilla JS + Supabase) */
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm";

const SUPA_URL = "https://tygucovkjqfzbxftyvny.supabase.co";
const SUPA_KEY = "sb_publishable_ozl1RjUe3LtgO6PYXg2crQ_66Ws_NPD";
const DOMAIN = "maxwise.studio"; // "admin" -> admin@maxwise.studio
const sb = createClient(SUPA_URL, SUPA_KEY, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } });

const $app = document.getElementById("app");
const S = { session: null, member: false, channels: [], chMap: {} };

/* ---------- local storage (guarded) ---------- */
const LS = {
  get: (k) => { try { return localStorage.getItem(k); } catch { return null; } },
  set: (k, v) => { try { localStorage.setItem(k, v); } catch { /* private mode */ } },
  del: (k) => { try { localStorage.removeItem(k); } catch { /* */ } },
};
const SS = {
  get: (k) => { try { return sessionStorage.getItem(k); } catch { return null; } },
  set: (k, v) => { try { sessionStorage.setItem(k, v); } catch { /* */ } },
};

/* ---------- helpers ---------- */
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const num = (n) => { n = Number(n || 0); if (n >= 1e6) return (n / 1e6).toFixed(1).replace(".", ",").replace(",0", "") + "tr"; if (n >= 1e3) return Math.round(n / 1e3) + "N"; return String(n); };
const dur = (s) => s ? `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}` : "";
const ago = (t) => { const d = (Date.now() - new Date(t)) / 864e5; return d < 1 ? `${Math.max(1, Math.round(d * 24))}h` : `${Math.floor(d)}d`; };
const tz = "Asia/Ho_Chi_Minh";
const vnDate = (d = new Date()) => new Intl.DateTimeFormat("en-CA", { timeZone: tz }).format(d);
const vnTime = (t) => new Intl.DateTimeFormat("vi-VN", { timeZone: tz, hour: "2-digit", minute: "2-digit" }).format(new Date(t));
const dm = (t) => new Intl.DateTimeFormat("vi-VN", { timeZone: tz, day: "2-digit", month: "2-digit" }).format(new Date(t));
const dayStart = (ymd) => new Date(`${ymd}T00:00:00+07:00`).toISOString();
const addDays = (ymd, n) => { const d = new Date(`${ymd}T12:00:00+07:00`); d.setUTCDate(d.getUTCDate() + n); return vnDate(d); };
const weekday = ["CN", "T2", "T3", "T4", "T5", "T6", "T7"];
const toast = (m, ms = 2200) => { const t = document.createElement("div"); t.className = "toast"; t.textContent = m; document.body.appendChild(t); setTimeout(() => t.remove(), ms); };
const grad = (seed) => { const hues = [28, 200, 150, 350, 265, 45, 190, 10]; let h = 0; for (const c of String(seed)) h = (h * 31 + c.charCodeAt(0)) >>> 0; const a = hues[h % hues.length]; return `linear-gradient(160deg,hsl(${a} 35% 62%),hsl(${a} 40% 24%))`; };
const spinner = `<div class="empty"><span class="spin" style="display:inline-block"></span></div>`;

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
  copy: '<rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
  refresh: '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
  chev: '<path d="M9 6l6 6-6 6"/>',
  sound: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6"/>',
  mute: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M17 9l4 6M21 9l-4 6"/>',
  lock: '<rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
  face: '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><path d="M9 9.5v1M15 9.5v1M12 9.5v3.5h-1M9.5 16a3.5 3.5 0 0 0 5 0"/>',
};
const ic = (n, s = 22, w = 2) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${I[n]}</svg>`;

function nav(on) {
  const it = (h, k, icon, label) => `<a href="#/${h}" class="${on === k ? "on" : ""}" ${on === k ? 'aria-current="page"' : ""}>${ic(icon)}${label}</a>`;
  return `<nav class="nav" aria-label="Điều hướng">${it("home", "home", "home", "Hôm nay")}${it("channels", "channels", "ch", "Kênh")}
  <a href="#/produce" class="fab ${on === "produce" ? "on" : ""}" aria-label="Lệnh sản xuất">${ic("plus", 24, 2.4)}</a>
  ${it("bst", "bst", "bst", "BST")}${it("library", "library", "dl", "Kho")}</nav>`;
}
function page({ top, body, navOn, dark = false }) {
  $app.className = dark ? "dark" : "";
  $app.innerHTML = `${top || ""}${body}${navOn === null ? "" : nav(navOn)}`;
}
const head = (title, right = "") => `<header class="top"><div class="row between"><h1 class="h1">${esc(title)}</h1><div class="row" style="gap:8px">${right}</div></div></header>`;
const backTop = (title, href, right = "") => `<header class="top"><div class="row"><a href="${href}" class="icon" aria-label="Quay lại">${ic("back", 18, 2.4)}</a><h1 class="h2">${esc(title)}</h1>${right}</div></header>`;

async function loadChannels() {
  const { data } = await sb.from("channels").select("*").order("created_at");
  S.channels = data || []; S.chMap = Object.fromEntries(S.channels.map((c) => [c.id, c]));
}

/* ---------- Face ID (WebAuthn platform authenticator gates this device's saved session) ---------- */
const b64 = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)));
const unb64 = (s) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
const rnd = (n) => crypto.getRandomValues(new Uint8Array(n));
const faceIdKey = "mw_passkey";
async function canFaceId() {
  try { return !!(window.PublicKeyCredential && await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()); } catch { return false; }
}
async function registerFaceId(email) {
  if (LS.get(faceIdKey) || !(await canFaceId())) return;
  try {
    const cred = await navigator.credentials.create({ publicKey: {
      challenge: rnd(32), rp: { name: "MAX WISE Studio", id: location.hostname },
      user: { id: rnd(16), name: email, displayName: email.split("@")[0] },
      pubKeyCredParams: [{ type: "public-key", alg: -7 }, { type: "public-key", alg: -257 }],
      authenticatorSelection: { authenticatorAttachment: "platform", userVerification: "required", residentKey: "preferred" }, timeout: 60000 } });
    if (cred) LS.set(faceIdKey, b64(cred.rawId));
  } catch { /* user cancelled */ }
}
async function unlockFaceId() {
  const id = LS.get(faceIdKey);
  const { data } = await sb.auth.getSession();
  if (!id || !data.session) return false;
  try {
    await navigator.credentials.get({ publicKey: { challenge: rnd(32), rpId: location.hostname, userVerification: "required",
      allowCredentials: [{ type: "public-key", id: unb64(id), transports: ["internal"] }], timeout: 60000 } });
    return true;
  } catch { return false; }
}
const locked = () => !!LS.get(faceIdKey) && LS.get("mw_lock") === "1" && SS.get("mw_open") !== "1";
const unlock = () => { LS.del("mw_lock"); SS.set("mw_open", "1"); };

/* ---------- login ---------- */
function viewLogin(msg = "") {
  page({ navOn: null, body: `<main class="main login">
    <img src="icon.svg" width="88" height="88" alt="MAX WISE Studio" style="border-radius:18px;align-self:center;margin-bottom:12px">
    <form id="f" style="display:flex;flex-direction:column;gap:12px">
      <input class="inp" name="u" type="text" autocomplete="username" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="Tài khoản" aria-label="Tài khoản" required>
      <input class="inp" name="pw" type="password" autocomplete="current-password" placeholder="Mật khẩu" aria-label="Mật khẩu" required>
      ${msg ? `<p class="err">${esc(msg)}</p>` : ""}
      <button class="btn btn-full" id="go">Đăng nhập</button>
      <button type="button" class="btn btn-o btn-full" id="fid">${ic("face", 22)}Face ID</button>
    </form></main>` });
  const f = document.getElementById("f");
  f.onsubmit = async (e) => {
    e.preventDefault();
    let email = f.u.value.trim().toLowerCase(); if (!email.includes("@")) email += "@" + DOMAIN;
    const b = document.getElementById("go"); b.disabled = true; b.innerHTML = '<span class="spin" style="border-top-color:#FFF"></span>';
    const { error } = await sb.auth.signInWithPassword({ email, password: f.pw.value });
    if (error) return viewLogin(/Invalid login/i.test(error.message) ? "Sai tài khoản hoặc mật khẩu" : error.message);
    unlock(); registerFaceId(email);
    if (S.session) { location.hash = "#/home"; route(); }
  };
  document.getElementById("fid").onclick = async () => {
    if (!LS.get(faceIdKey)) return toast("Đăng nhập bằng mật khẩu một lần để bật Face ID");
    if (await unlockFaceId()) { unlock(); location.hash = "#/home"; route(); } else toast("Face ID không thành công");
  };
}

/* ---------- home ---------- */
async function viewHome() {
  page({ navOn: "home", top: head(`Hôm nay · ${dm(new Date())}`, `<a href="#/schedule" class="icon" aria-label="Lịch chạy">${ic("cal", 18)}</a><button class="icon" id="lo" aria-label="Khoá">${ic("lock", 18)}</button>`),
    body: `<main class="main" id="m">${spinner}</main>` });
  document.getElementById("lo").onclick = lockApp;
  const since = new Date(Date.now() - 7 * 864e5).toISOString();
  const [nWait, nProc, ex, hot] = await Promise.all([
    sb.from("feed_items").select("id", { count: "exact", head: true }).eq("status", "new").gte("posted_at", since),
    sb.from("jobs").select("id", { count: "exact", head: true }).in("status", ["queued", "downloading", "editing", "rendering"]),
    sb.from("exports").select("*").gte("created_at", dayStart(vnDate())).order("created_at"),
    sb.rpc("feed_today", { p_limit: 3 }),
  ]);
  const exs = ex.data || []; const hots = hot.data || [];
  const th = await signed("exports", exs.map((e) => e.thumb_path));
  const cov = await signed("feed", hots.map((h) => h.cover_path));
  const m = document.getElementById("m"); if (!m) return;
  m.innerHTML = `
  <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px">
    <a href="#/feed" class="card stat" style="border-color:#18181B"><b>${nWait.count ?? 0}</b><small>Chờ duyệt</small></a>
    <a href="#/bst" class="card stat"><b>${nProc.count ?? 0}</b><small>Đang làm</small></a>
    <a href="#/library" class="card stat"><b>${exs.length}</b><small>Đã xuất</small></a>
  </div>
  ${exs.length ? `<section class="card" style="padding:12px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px">${exs.slice(0, 3).map((e) => `<a href="#/library" style="display:flex;flex-direction:column;gap:6px"><div class="th" style="aspect-ratio:9/16;background-image:url('${th[e.thumb_path] || ""}'),${grad(e.id)}"><span>${dur(e.duration_sec)}</span></div><span style="font-size:12px;font-weight:600;line-height:1.3">${esc(e.title)}</span></a>`).join("")}</section>` : ""}
  ${hots.length ? `<div class="row between" style="padding:0 2px"><span class="sec">Chờ duyệt</span><a href="#/feed" class="lk">Lướt</a></div>
  <section class="card">${hots.map((h) => `<div class="row" style="padding:10px 12px;border-bottom:1px solid #F4F4F5;gap:12px" data-id="${h.id}">
      <div class="th" style="width:44px;height:78px;background-image:url('${cov[h.cover_path] || ""}'),${grad(h.id)}"></div>
      <div style="flex:1;min-width:0"><div class="clamp2" style="font-size:14px;font-weight:600;line-height:1.3">${esc(h.caption_vi || h.caption_orig || "—")}</div>
      <div class="vm">${esc(S.chMap[h.channel_id]?.name || "")} · ${h.views ? num(h.views) : "♥ " + num(h.likes)}</div></div>
      <button class="btn btn-y sm" data-ap="${h.id}" aria-label="Duyệt">${ic("check", 18, 2.8)}</button></div>`).join("")}</section>`
    : !S.channels.length ? `<a href="#/add" class="card empty" style="display:block">${ic("plus", 28)}<br>Thêm kênh</a>` : ""}`;
  m.querySelectorAll("[data-ap]").forEach((b) => b.onclick = async () => { b.disabled = true; await approve(hots.find((x) => x.id === b.dataset.ap)); b.closest("[data-id]").remove(); });
}
function lockApp() { if (LS.get(faceIdKey)) { LS.set("mw_lock", "1"); SS.set("mw_open", ""); viewLogin(); } else sb.auth.signOut(); }

/* ---------- approve / skip ---------- */
async function approve(item) {
  const ch = S.chMap[item.channel_id] || {};
  const kind = ch.use_original ? "footage" : "idea";
  const { error } = await sb.from("feed_items").update({ status: "approved", approved_at: new Date().toISOString() }).eq("id", item.id);
  if (error) return toast(error.message);
  await sb.from("jobs").insert({ kind, feed_item_id: item.id, topic: item.caption_vi || item.caption_orig, run_when: "next_morning" });
  toast("✓ Đã thêm vào BST");
}
const skip = (item) => sb.from("feed_items").update({ status: "skipped" }).eq("id", item.id);

/* ---------- channels ---------- */
async function viewChannels() {
  page({ navOn: "channels", top: head("Kênh", `<button class="icon" id="sc" aria-label="Cào ngay">${ic("refresh", 18)}</button><a href="#/add" class="icon" style="background:#18181B;color:#FFF;border-color:#18181B" aria-label="Thêm kênh">${ic("plus", 18, 2.4)}</a>`),
    body: `<main class="main" id="m">${spinner}</main>` });
  document.getElementById("sc").onclick = () => runScrape();
  await loadChannels();
  const since = new Date(Date.now() - 7 * 864e5).toISOString();
  const { data: items } = await sb.from("feed_items").select("channel_id,status,views").gte("posted_at", since);
  const agg = {}; (items || []).forEach((i) => { const a = (agg[i.channel_id] ||= { n: 0, wait: 0 }); a.n++; if (i.status === "new") a.wait++; });
  const m = document.getElementById("m"); if (!m) return;
  m.innerHTML = S.channels.length ? `<section class="card" style="overflow:hidden">${S.channels.map((c) => {
    const a = agg[c.id] || { n: 0, wait: 0 };
    return `<div class="ch" data-c="${c.id}"><div class="av" style="${c.avatar_url ? `background-image:url('${esc(c.avatar_url)}')` : `background:${grad(c.id)}`}">${c.avatar_url ? "" : esc((c.name || c.platform)[0].toUpperCase())}</div>
    <div style="flex:1;min-width:0"><div class="ell" style="font-size:15px;font-weight:700">${esc(c.name || c.url)}</div>
    <div class="row" style="gap:6px;margin-top:4px">${c.platform === "douyin" ? '<span class="tag">Douyin</span>' : '<span class="tag">TikTok</span>'}${c.use_original ? '<span class="tag ok">Gốc</span>' : ""}${a.wait ? `<span class="tag yl">${a.wait} chờ</span>` : ""}${c.last_error ? '<span class="tag bad">Lỗi</span>' : ""}${c.active ? "" : '<span class="tag">Tắt</span>'}</div></div>
    <span style="color:#A1A1AA">${ic("chev", 18, 2.2)}</span></div>`;
  }).join("")}</section><a href="#/feed" class="btn btn-full">Lướt video</a>` : `<a href="#/add" class="card empty" style="display:block">${ic("plus", 28)}<br>Thêm kênh</a>`;
  m.querySelectorAll("[data-c]").forEach((el) => el.onclick = () => channelSheet(S.chMap[el.dataset.c]));
}

async function runScrape(channel_id) {
  toast("Đang cào…", 3000);
  const { data, error } = await sb.functions.invoke("scrape", { body: channel_id ? { channel_id } : {} });
  if (error) { toast("Lỗi cào: " + (error.message || error)); return null; }
  const added = (data.channels || []).reduce((s, c) => s + (c.added || 0), 0);
  const errs = (data.channels || []).filter((c) => c.error);
  toast(errs.length ? `+${added} video · lỗi: ${errs[0].error}` : `+${added} video mới`, 3500);
  if (location.hash.startsWith("#/channels")) viewChannels();
  return data;
}

function channelSheet(c) {
  const el = document.createElement("div"); el.className = "sheet";
  el.innerHTML = `<div><div class="row" style="margin-bottom:14px"><div style="flex:1;min-width:0;font-size:17px;font-weight:800" class="ell">${esc(c.name || "Kênh")}</div><button class="icon" data-x aria-label="Đóng">${ic("x", 18)}</button></div>
  ${c.last_error ? `<p class="tag bad" style="height:auto;padding:6px 8px;white-space:normal;margin:0 0 12px">${esc(c.last_error)}</p>` : ""}
  <div class="card" style="margin-bottom:12px">
    <label class="li"><span>Dùng video gốc</span><input type="checkbox" class="sw" data-k="use_original" ${c.use_original ? "checked" : ""}></label>
    <label class="li"><span>Tự cào mỗi sáng</span><input type="checkbox" class="sw" data-k="auto_scrape" ${c.auto_scrape ? "checked" : ""}></label>
    <label class="li"><span>Bật kênh</span><input type="checkbox" class="sw" data-k="active" ${c.active ? "checked" : ""}></label>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
    <a class="btn" href="#/feed?ch=${c.id}">Lướt</a><button class="btn btn-o" data-s>Cào ngay</button>
    <a class="btn btn-o" href="${esc(c.url)}" target="_blank" rel="noopener">Mở kênh</a><button class="btn btn-o" data-del style="color:#B91C1C">Xoá</button>
  </div></div>`;
  document.body.appendChild(el);
  const close = () => el.remove();
  el.onclick = (e) => { if (e.target === el || e.target.closest("[data-x]") || e.target.closest("a")) close(); };
  el.querySelectorAll("[data-k]").forEach((i) => i.onchange = async () => { await sb.from("channels").update({ [i.dataset.k]: i.checked }).eq("id", c.id); c[i.dataset.k] = i.checked; toast("✓ Đã lưu"); if (location.hash.startsWith("#/channels")) viewChannels(); });
  el.querySelector("[data-s]").onclick = () => { close(); runScrape(c.id); };
  el.querySelector("[data-del]").onclick = async () => { if (!confirm("Xoá kênh?")) return; await sb.from("channels").delete().eq("id", c.id); close(); viewChannels(); };
}

/* ---------- add channel ---------- */
function viewAdd() {
  page({ navOn: "channels", top: backTop("Thêm kênh", "#/channels"), body: `<main class="main"><form id="f" style="display:flex;flex-direction:column;gap:10px">
    <input class="inp" name="url" type="url" required placeholder="Link kênh Douyin / TikTok" aria-label="Link kênh" inputmode="url" autocapitalize="off">
    <div class="seg" id="pf"><button type="button" data-v="douyin" class="on">Douyin</button><button type="button" data-v="tiktok">TikTok</button></div>
    <div class="card">
      <label class="li"><span>Tự cào 7 ngày</span><input type="checkbox" class="sw" name="auto" checked></label>
      <label class="li"><span>View tối thiểu</span><select name="minv"><option value="0">Tất cả</option><option value="100000" selected>100N</option><option value="500000">500N</option><option value="1000000">1tr</option></select></label>
      <label class="li"><span>Độ dài</span><select name="dur"><option value="20-300" selected>20s – 5p</option><option value="10-60">&lt; 60s</option><option value="20-600">≤ 10p</option></select></label>
      <label class="li"><span>Dùng video gốc</span><input type="checkbox" class="sw" name="orig"></label>
    </div>
    <input class="inp" name="credit" type="text" placeholder="Ghi công (tuỳ chọn)" aria-label="Ghi công">
    <button class="btn btn-full" id="go" style="margin-top:6px">Lưu & cào</button>
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
    const { data, error } = await sb.from("channels").insert({ url, platform: pf, auto_scrape: f.auto.checked,
      min_views: Number(f.minv.value), min_sec: a, max_sec: b, use_original: f.orig.checked, credit: f.credit.value.trim() || null }).select().single();
    if (error) { go.disabled = false; go.textContent = "Lưu & cào"; return toast(error.message); }
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
    <div class="ftop"><a href="#/channels" class="pill" aria-label="Kênh">${ic("back", 18, 2.4)}</a>
      <div class="row" style="gap:18px"><button class="ftab ${chId ? "" : "on"}" data-t="">Hôm nay</button><button class="ftab ${chId ? "on" : ""}" data-t="ch">${chId ? esc((S.chMap[chId]?.name || "Kênh").slice(0, 14)) : "Theo kênh"}</button></div>
      <span class="pill" id="cnt">…</span></div>
    <div class="feed" id="feed"></div></div>` });
  await loadChannels();
  document.querySelectorAll(".ftab").forEach((b) => b.onclick = () => {
    if (!b.dataset.t) { location.hash = "#/feed"; return; }
    pickChannel((id) => (location.hash = "#/feed?ch=" + id));
  });
  const { data: items, error } = await sb.rpc("feed_today", { p_channel: chId || null, p_limit: 200 });
  const feed = document.getElementById("feed"); if (!feed) return;
  if (error) { feed.innerHTML = `<div class="fdone">${esc(error.message)}</div>`; return; }
  const list = items || [];
  const cnt = document.getElementById("cnt");
  if (!list.length) { feed.innerHTML = `<div class="fdone">${ic("check", 40)}<div>Hết video</div></div>`; cnt.textContent = "0"; return; }
  let rendered = 0, muted = true, done = 0;
  const total = list.length;
  const cardHTML = (it, i) => {
    const ch = S.chMap[it.channel_id] || {};
    const vi = it.caption_vi;
    return `<section class="fi" data-i="${i}" data-id="${it.id}" style="background-image:${grad(it.id)}">
      <video playsinline muted loop preload="none"></video>
      <div class="shade"></div>
      <div class="rail">
        <button class="rb ok" data-a="ap"><i>${ic("check", 24, 2.8)}</i>Duyệt</button>
        <button class="rb" data-a="sk"><i>${ic("x", 22, 2.4)}</i>Bỏ</button>
        ${vi ? `<button class="rb" data-a="lang"><i>VI</i>Gốc</button>` : ""}
        <button class="rb" data-a="snd" aria-label="Âm thanh"><i>${ic("mute", 22)}</i></button>
        <a class="rb" href="${esc(it.share_url || ch.url || "#")}" target="_blank" rel="noopener" aria-label="Mở gốc"><i>${ic("ext", 22)}</i></a>
      </div>
      <div class="info">
        <div class="row" style="gap:8px"><span class="av" style="width:28px;height:28px;font-size:12px;border-radius:4px;${ch.avatar_url ? `background-image:url('${esc(ch.avatar_url)}')` : `background:${grad(ch.id)}`}">${ch.avatar_url ? "" : esc((ch.name || "?")[0])}</span>
          <span class="ell" style="font-size:15px;font-weight:800;max-width:190px">${esc(ch.name || "Kênh")}</span>${ch.use_original ? '<span class="tag" style="background:rgba(255,212,59,.2);color:#FFD43B">Gốc</span>' : ""}</div>
        <p data-cap>${esc(vi || it.caption_orig || "")}</p>
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
    if (rendered >= total) feed.insertAdjacentHTML("beforeend", `<div class="fdone">${ic("check", 40)}<div>Hết video</div><a class="btn btn-y sm" href="#/bst">BST</a></div>`);
    feed.querySelectorAll(`.fi:not([data-obs])`).forEach((s) => { s.dataset.obs = 1; feedObs.observe(s); });
    await media(from, to);
  };
  if (feedObs) feedObs.disconnect();
  feedObs = new IntersectionObserver((ents) => {
    ents.forEach((en) => {
      const v = en.target.querySelector("video"); if (!v) return;
      if (en.isIntersecting && en.intersectionRatio > 0.6) {
        cnt.textContent = `${[...feed.querySelectorAll(".fi")].indexOf(en.target) + 1}/${total - done}`;
        if (v.dataset.url && !v.src) v.src = v.dataset.url;
        v.muted = muted; v.play().catch(() => {});
        if (Number(en.target.dataset.i) >= rendered - 3) more();
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
    if (a === "lang") { const p = sec.querySelector("[data-cap]"); const orig = btn.dataset.o !== "1"; btn.dataset.o = orig ? "1" : ""; p.textContent = orig ? it.caption_orig : it.caption_vi; btn.querySelector("i").textContent = orig ? "中" : "VI"; btn.lastChild.textContent = orig ? "Dịch" : "Gốc"; return; }
    if (a === "snd") { muted = !muted; feed.querySelectorAll("video").forEach((v) => (v.muted = muted)); feed.querySelectorAll('[data-a="snd"] i').forEach((i) => (i.innerHTML = ic(muted ? "mute" : "sound", 22))); return; }
    btn.disabled = true;
    (a === "ap" ? approve(it) : skip(it));
    const v = sec.querySelector("video"); if (v) { v.pause(); v.removeAttribute("src"); v.load(); }
    const top = sec.offsetTop; feedObs.unobserve(sec); sec.remove(); done++;
    feed.scrollTop = top;
    cnt.textContent = String(total - done);
    const cur = [...feed.querySelectorAll(".fi")].find((s) => s.offsetTop === top);
    if (cur) { const cv = cur.querySelector("video"); if (cv.dataset.url && !cv.src) cv.src = cv.dataset.url; cv.muted = muted; cv.play().catch(() => {}); }
  };
}

function pickChannel(cb) {
  const el = document.createElement("div"); el.className = "sheet";
  el.innerHTML = `<div><div class="row between" style="margin-bottom:12px"><b style="font-size:17px">Kênh</b><button class="icon" data-x aria-label="Đóng">${ic("x", 18)}</button></div>
  <div class="card">${S.channels.map((c) => `<button class="li" style="width:100%;background:none;border:0;border-bottom:1px solid #F4F4F5;text-align:left;cursor:pointer" data-c="${c.id}"><span class="ell">${esc(c.name || c.url)}</span>${ic("chev", 16)}</button>`).join("") || '<div class="empty">—</div>'}</div></div>`;
  document.body.appendChild(el);
  el.onclick = (e) => { const b = e.target.closest("[data-c]"); if (b) { el.remove(); cb(b.dataset.c); } else if (e.target === el || e.target.closest("[data-x]")) el.remove(); };
}

/* ---------- collection ---------- */
const STEPS = [["downloading", "Tải"], ["editing", "Cắt"], ["rendering", "Max"], ["ready", "Xong"]];
async function viewBst(params) {
  const tab = params.get("t") || "proc";
  page({ navOn: "bst", top: head("Bộ sưu tập", `<label class="row" style="gap:6px;font-size:12px;font-weight:700">Tự sửa<input type="checkbox" class="sw" id="ae"></label>`),
    body: `<main class="main" id="m">${spinner}</main>` });
  await loadChannels();
  const [{ data: jobs }, { data: st }] = await Promise.all([
    sb.from("jobs").select("*, feed_items(caption_vi,caption_orig,cover_path,views,channel_id)").neq("status", "cancelled").order("created_at", { ascending: false }).limit(100),
    sb.from("settings").select("auto_edit").eq("id", 1).single(),
  ]);
  const ae = document.getElementById("ae"); if (!ae) return;
  ae.checked = !!st?.auto_edit;
  ae.onchange = async () => { await sb.from("settings").update({ auto_edit: ae.checked }).eq("id", 1); toast("✓ Đã lưu"); };
  const all = jobs || [];
  const groups = { proc: all.filter((j) => ["downloading", "editing", "rendering"].includes(j.status)), wait: all.filter((j) => j.status === "queued"), done: all.filter((j) => ["ready", "failed"].includes(j.status)) };
  const cov = await signed("feed", all.map((j) => j.feed_items?.cover_path));
  const m = document.getElementById("m"); if (!m) return;
  const kindTag = (j) => j.kind === "footage" ? '<span class="tag inf">Gốc</span>' : j.kind === "idea" ? '<span class="tag">Ý tưởng</span>' : '<span class="tag yl">Doodle</span>';
  const card = (j) => {
    const f = j.feed_items || {}; const idx = STEPS.findIndex((s) => s[0] === j.status);
    return `<div style="padding:12px;display:flex;flex-direction:column;gap:10px;border-bottom:1px solid #F4F4F5">
    <div class="row" style="gap:12px;align-items:flex-start"><div class="th" style="width:44px;height:78px;background-image:url('${cov[f.cover_path] || ""}'),${grad(j.id)}"></div>
    <div style="flex:1;min-width:0"><div class="vt clamp2">${esc(j.topic || f.caption_vi || f.caption_orig || "Video")}</div>
    <div class="row" style="gap:6px;margin-top:6px;flex-wrap:wrap">${kindTag(j)}${j.status === "failed" ? '<span class="tag bad">Lỗi</span>' : j.status === "ready" ? '<span class="tag ok">✓</span>' : j.progress ? `<span class="tag yl">${j.progress}%</span>` : ""}${j.run_when === "now" && j.status === "queued" ? '<span class="tag yl">Ngay</span>' : ""}<span class="vm" style="margin:0">${esc(S.chMap[f.channel_id]?.name || "")}</span></div>
    ${j.error ? `<div class="vm" style="color:#B91C1C">${esc(j.error)}</div>` : ""}
    ${j.status === "queued" ? `<div class="row" style="gap:6px;margin-top:8px">${j.run_when === "now" ? "" : `<button class="btn btn-y xs" data-now="${j.id}">Làm ngay</button>`}<button class="btn btn-o xs" data-cancel="${j.id}">Gỡ</button></div>` : ""}
    ${j.status === "ready" ? `<div class="row" style="gap:6px;margin-top:8px"><a class="btn xs" href="#/library">Kho</a><button class="btn btn-o xs" data-redo="${j.id}">Sửa lại</button></div>` : ""}
    ${j.status === "failed" ? `<div class="row" style="gap:6px;margin-top:8px"><button class="btn btn-o xs" data-redo="${j.id}">Thử lại</button></div>` : ""}
    </div></div>
    ${j.kind === "footage" && idx >= 0 && j.status !== "ready" ? `<div class="steps">${STEPS.map((s, k) => `<div class="${k < idx ? "d" : k === idx ? "c" : ""}"><i></i>${s[1]}</div>`).join("")}</div>` : ""}
    </div>`;
  };
  m.innerHTML = `<div class="seg"><button class="${tab === "proc" ? "on" : ""}" data-t="proc">Đang làm · ${groups.proc.length}</button><button class="${tab === "wait" ? "on" : ""}" data-t="wait">Chờ · ${groups.wait.length}</button><button class="${tab === "done" ? "on" : ""}" data-t="done">Xong · ${groups.done.length}</button></div>
  ${groups[tab].length ? `<section class="card" style="overflow:hidden">${groups[tab].map(card).join("")}</section>` : `<div class="empty">—</div>`}`;
  m.querySelectorAll("[data-t]").forEach((b) => b.onclick = () => (location.hash = "#/bst?t=" + b.dataset.t));
  m.querySelectorAll("[data-now]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ run_when: "now", updated_at: new Date().toISOString() }).eq("id", b.dataset.now); toast("✓ Làm trong 1 giờ tới"); viewBst(params); });
  m.querySelectorAll("[data-cancel]").forEach((b) => b.onclick = async () => { const j = all.find((x) => x.id === b.dataset.cancel); await sb.from("jobs").update({ status: "cancelled" }).eq("id", j.id); if (j.feed_item_id) await sb.from("feed_items").update({ status: "new" }).eq("id", j.feed_item_id); toast("Đã gỡ"); viewBst(params); });
  m.querySelectorAll("[data-redo]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ status: "queued", progress: 0, step: null, error: null, run_when: "now" }).eq("id", b.dataset.redo); toast("✓ Đã xếp lại"); viewBst(params); });
}

/* ---------- produce ---------- */
const IDEAS = ["Why does the Moon follow your car?", "Are you more bacteria than human?", "You're sitting still. How fast are you moving?"];
function viewProduce() {
  page({ navOn: "produce", top: head("Lệnh sản xuất"), body: `<main class="main"><form id="f" style="display:flex;flex-direction:column;gap:10px">
    <input id="topic" class="inp" name="topic" required placeholder="Câu hỏi tò mò" aria-label="Câu hỏi tò mò">
    <div class="row" style="gap:6px;flex-wrap:wrap">${IDEAS.map((t) => `<button type="button" class="btn btn-o xs" data-idea="${esc(t)}" style="font-weight:600">${esc(t.length > 26 ? t.slice(0, 24) + "…" : t)}</button>`).join("")}</div>
    <div class="card">
      <label class="li"><span>Giọng</span><select name="voice"><option value="en-US-AndrewMultilingualNeural">Andrew</option><option value="en-US-BrianMultilingualNeural">Brian</option></select></label>
      <label class="li"><span>Phụ đề</span><select name="subs"><option value="en+vi">EN + VI</option><option value="en">EN</option></select></label>
      <label class="li"><span>Nhạc + SFX</span><input type="checkbox" class="sw" name="music" checked></label>
      <label class="li"><span>Gửi Telegram</span><input type="checkbox" class="sw" name="tg" checked></label>
    </div>
    <div class="seg" id="when"><button type="button" data-v="now" class="on">Làm ngay</button><button type="button" data-v="next_morning">Sáng mai</button></div>
    <button class="btn btn-full" style="margin-top:6px">Gửi lệnh</button>
  </form>
  <section class="card" id="q"></section></main>` });
  let when = "now";
  document.querySelectorAll("#when button").forEach((b) => b.onclick = () => { when = b.dataset.v; document.querySelectorAll("#when button").forEach((x) => x.classList.toggle("on", x === b)); });
  const f = document.getElementById("f");
  f.querySelectorAll("[data-idea]").forEach((b) => b.onclick = () => (f.topic.value = b.dataset.idea));
  f.onsubmit = async (e) => {
    e.preventDefault();
    const { error } = await sb.from("jobs").insert({ kind: "doodle", topic: f.topic.value.trim(), voice: f.voice.value, subs: f.subs.value, music: f.music.checked, telegram: f.tg.checked, run_when: when });
    if (error) return toast(error.message);
    toast("✓ Đã gửi"); f.topic.value = ""; loadQueue();
  };
  const loadQueue = async () => {
    const { data } = await sb.from("jobs").select("id,topic,run_when,status").eq("kind", "doodle").in("status", ["queued", "downloading", "editing", "rendering"]).order("created_at");
    const q = document.getElementById("q"); if (!q) return;
    q.style.display = (data || []).length ? "" : "none";
    q.innerHTML = (data || []).map((j) => `<div class="li"><span class="ell" style="flex:1;min-width:0">${esc(j.topic)}</span>${j.status === "queued" ? `<span class="tag ${j.run_when === "now" ? "yl" : ""}">${j.run_when === "now" ? "Ngay" : "Sáng"}</span><button class="icon" style="width:30px;height:30px" data-c="${j.id}" aria-label="Huỷ">${ic("x", 14)}</button>` : '<span class="spin"></span>'}</div>`).join("");
    q.querySelectorAll("[data-c]").forEach((b) => b.onclick = async () => { await sb.from("jobs").update({ status: "cancelled" }).eq("id", b.dataset.c); loadQueue(); });
  };
  loadQueue();
}

/* ---------- schedule ---------- */
async function viewSchedule() {
  page({ navOn: "home", top: backTop("Lịch chạy", "#/home", `<input type="checkbox" class="sw" id="en" aria-label="Bật lịch" style="accent-color:#16A34A">`),
    body: `<main class="main" id="m">${spinner}</main>` });
  const [{ data: s }, { data: runs }] = await Promise.all([sb.from("settings").select("*").eq("id", 1).single(), sb.from("runs").select("*").order("created_at", { ascending: false }).limit(10)]);
  const m = document.getElementById("m"); if (!m || !s) return;
  document.getElementById("en").checked = s.enabled;
  const numSel = (k, opts) => `<div class="seg" style="width:auto" data-k="${k}">${opts.map((o) => `<button type="button" style="width:38px;height:32px" data-v="${o}" class="${s[k] === o ? "on" : ""}">${o}</button>`).join("")}</div>`;
  m.innerHTML = `<div class="card">
    <div class="li"><b>${s.scrape_time}</b><span>Cào kênh</span></div>
    <div class="li"><b>${s.produce_time}</b><span>Sản xuất</span></div>
    <div class="li"><b style="background:#FFD43B;border-radius:3px;padding:0 4px">${s.send_time}</b><span>Gửi Telegram</span></div>
  </div>
  <div class="card">
    <div class="li"><span>Doodle / ngày</span>${numSel("doodles_per_day", [0, 1, 2, 3])}</div>
    <div class="li"><span>Từ BST / ngày</span>${numSel("footage_per_day", [0, 1, 2, 3])}</div>
    <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px;padding:12px 14px" id="days">${[1, 2, 3, 4, 5, 6, 0].map((d) => `<button type="button" data-d="${d}" class="btn ${s.days.includes(d) ? "" : "btn-o"}" style="height:34px;padding:0;font-size:12px">${weekday[d]}</button>`).join("")}</div>
  </div>
  ${(runs || []).length ? `<div class="card">${runs.map((r) => `<div class="li" style="font-size:13px"><span class="row" style="gap:10px"><span style="width:8px;height:8px;border-radius:2px;background:${r.status === "ok" ? "#16A34A" : "#F59E0B"}"></span>${r.run_date.split("-").reverse().slice(0, 2).join("/")} · ${r.videos} video</span><span class="vm" style="margin:0">${r.sent_at ? vnTime(r.sent_at) : ""}</span></div>`).join("")}</div>` : ""}`;
  const save = async (patch) => { Object.assign(s, patch); const { error } = await sb.from("settings").update({ ...patch, updated_at: new Date().toISOString() }).eq("id", 1); toast(error ? error.message : "✓ Đã lưu"); };
  document.getElementById("en").onchange = (e) => save({ enabled: e.target.checked });
  m.querySelectorAll("[data-k]").forEach((g) => g.onclick = (e) => { const b = e.target.closest("[data-v]"); if (!b) return; g.querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b)); save({ [g.dataset.k]: Number(b.dataset.v) }); });
  document.getElementById("days").onclick = (e) => { const b = e.target.closest("[data-d]"); if (!b) return; const d = Number(b.dataset.d); const days = s.days.includes(d) ? s.days.filter((x) => x !== d) : [...s.days, d]; b.classList.toggle("btn-o"); save({ days }); };
}

/* ---------- library (exports) ---------- */
async function viewLibrary(params) {
  const today = vnDate();
  const f = params.get("d") || "today";
  let from, to;
  if (f === "today") { from = today; to = addDays(today, 1); }
  else if (f === "yesterday") { from = addDays(today, -1); to = today; }
  else if (f === "7d") { from = addDays(today, -6); to = addDays(today, 1); }
  else if (f === "all") { from = "2020-01-01"; to = addDays(today, 1); }
  else { from = f; to = addDays(f, 1); }
  const isDate = /^\d{4}/.test(f);
  page({ navOn: "library", top: `<header class="top"><h1 class="h1">Kho</h1>
    <div class="row" style="gap:6px">${[["today", "Hôm nay"], ["yesterday", "Hôm qua"], ["7d", "7 ngày"], ["all", "Tất cả"]].map(([k, l]) => `<a href="#/library?d=${k}" class="btn xs ${f === k ? "" : "btn-o"}" style="font-weight:600">${l}</a>`).join("")}
    <label class="btn xs ${isDate ? "" : "btn-o"}" style="position:relative;font-weight:600" aria-label="Chọn ngày">${ic("cal", 14)}${isDate ? f.split("-").reverse().slice(0, 2).join("/") : ""}<input type="date" id="dp" max="${today}" style="position:absolute;inset:0;opacity:0"></label></div></header>`,
    body: `<main class="main" id="m">${spinner}</main>` });
  document.getElementById("dp").onchange = (e) => e.target.value && (location.hash = "#/library?d=" + e.target.value);
  const { data } = await sb.from("exports").select("*").gte("created_at", dayStart(from)).lt("created_at", dayStart(to)).order("created_at", { ascending: false }).limit(200);
  const list = data || [];
  const th = await signed("exports", list.map((e) => e.thumb_path));
  const m = document.getElementById("m"); if (!m) return;
  if (!list.length) { m.innerHTML = `<div class="empty">—</div>`; return; }
  const byDay = {}; list.forEach((e) => (byDay[vnDate(new Date(e.created_at))] ||= []).push(e));
  m.innerHTML = Object.entries(byDay).map(([d, arr]) => `<span class="sec">${d.split("-").reverse().slice(0, 2).join("/")}</span>` + arr.map((e) => `
    <article class="card row" style="padding:12px;gap:12px;align-items:stretch" data-e="${e.id}">
      <div class="th" style="width:72px;height:128px;background-image:url('${th[e.thumb_path] || ""}'),${grad(e.id)}"><span>${dur(e.duration_sec)}</span></div>
      <div style="flex:1;min-width:0;display:flex;flex-direction:column">
        <div class="vt">${esc(e.title)}${e.posted ? ' <span style="color:#16A34A">✓</span>' : ""}</div>
        <div class="cap">${esc(e.caption || "")}</div>
        <div class="row" style="gap:6px;margin-top:auto;padding-top:8px">
          <button class="btn btn-o xs" data-a="copy" aria-label="Copy caption">${ic("copy", 15)}Caption</button>
          <button class="btn xs" data-a="dl" aria-label="Tải về">${ic("dl", 15, 2.4)}</button>
          <button class="btn btn-o xs" data-a="share" aria-label="Chia sẻ">${ic("share", 15)}</button>
        </div>
      </div></article>`).join("")).join("");
  m.onclick = async (ev) => {
    const b = ev.target.closest("[data-a]"); if (!b) return;
    const e = list.find((x) => x.id === b.closest("[data-e]").dataset.e);
    const fname = (e.title || "maxwise").replace(/[^\w\- ]+/g, "").trim().replace(/\s+/g, "-").toLowerCase() + ".mp4";
    if (b.dataset.a === "copy") {
      try { await navigator.clipboard.writeText(e.caption || ""); } catch { const t = document.createElement("textarea"); t.value = e.caption || ""; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); }
      const old = b.innerHTML; b.innerHTML = ic("check", 15, 2.6) + "Đã copy"; b.classList.add("ok"); setTimeout(() => { b.innerHTML = old; b.classList.remove("ok"); }, 1600);
    } else if (b.dataset.a === "dl") {
      const { data: s } = await sb.storage.from("exports").createSignedUrl(e.video_path, 3600, { download: fname });
      if (s?.signedUrl) location.href = s.signedUrl;
    } else {
      const old = b.innerHTML; b.innerHTML = '<span class="spin"></span>';
      const { data: s } = await sb.storage.from("exports").createSignedUrl(e.video_path, 3600);
      try {
        const blob = await (await fetch(s.signedUrl)).blob();
        const file = new File([blob], fname, { type: "video/mp4" });
        if (navigator.canShare && navigator.canShare({ files: [file] })) await navigator.share({ files: [file], text: e.caption || "" });
        else if (navigator.share) await navigator.share({ url: s.signedUrl, text: e.caption || "" });
        else { await navigator.clipboard.writeText(s.signedUrl); toast("✓ Đã copy link"); }
        if (!e.posted) await sb.from("exports").update({ posted: true }).eq("id", e.id);
      } catch (err) { if (err?.name !== "AbortError") toast(err.message); }
      b.innerHTML = old;
    }
  };
}

/* ---------- router ---------- */
const routes = { home: viewHome, channels: viewChannels, add: viewAdd, feed: viewFeed, bst: viewBst, produce: viewProduce, schedule: viewSchedule, library: viewLibrary };
async function route() {
  if (!S.session || locked()) return viewLogin();
  if (!S.member) {
    page({ navOn: null, body: `<main class="main login"><p class="err" style="text-align:center">Tài khoản không có quyền</p><button class="btn btn-full" id="lo">Đăng xuất</button></main>` });
    document.getElementById("lo").onclick = () => sb.auth.signOut(); return;
  }
  if (/access_token|error_description/.test(location.hash)) history.replaceState(null, "", "#/home");
  const [name, qs] = (location.hash.replace(/^#\/?/, "") || "home").split("?");
  if (!S.channels.length && name !== "add") await loadChannels();
  if (feedObs && name !== "feed") { feedObs.disconnect(); feedObs = null; }
  (routes[name] || viewHome)(new URLSearchParams(qs || ""));
}
window.addEventListener("hashchange", route);
// every fresh app launch asks for Face ID once it is set up
if (LS.get(faceIdKey) && SS.get("mw_open") !== "1") LS.set("mw_lock", "1");
sb.auth.onAuthStateChange(async (ev, session) => {
  const was = S.session?.user?.id; S.session = session;
  if (!session) { S.member = false; S.channels = []; return viewLogin(); }
  if (was !== session.user.id) {
    const { data } = await sb.rpc("is_member"); S.member = !!data;
    route();
  }
});
(async () => {
  const { data } = await sb.auth.getSession();
  if (!data.session) viewLogin();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})();
