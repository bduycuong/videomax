#!/usr/bin/env python3
"""Bridge between the daily cloud run and the MAX WISE Studio app (Supabase).

usage:
  studio.py settings                         print settings row (JSON)
  studio.py scrape [--channel ID]            run the TikHub scrape edge function (7-day window)
  studio.py untranslated [--out f.json]      feed items whose caption_vi is empty -> [{id, caption_orig}]
  studio.py translations f.json              write [{id, caption_vi}] back
  studio.py jobs [--now] [--kind K]          queued jobs (JSON); --now = only run_when=now
  studio.py job ID STATUS [--progress N] [--step TEXT] [--error TEXT]
  studio.py source JOB_ID OUT.mp4            download the full-quality source video for a footage job
  studio.py export --title T --caption-file F --video V [--thumb P] [--job ID] [--kind doodle|footage|idea]
                   [--duration S] [--source-channel NAME]
  studio.py runlog --videos N [--redone N] [--sent] [--note TEXT] [--status ok|partial|failed]

Reads supabase.json (url, anon_key, engine_email, engine_password) and tikhub.json from the repo root.
Uploads to Storage must be <= 45 MB (free-plan limit is 50 MB per file): upload the social copy.
"""
import argparse, datetime, json, mimetypes, os, re, ssl, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "supabase.json")))
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
TZ = datetime.timezone(datetime.timedelta(hours=7))
_tok = None


def http(method, url, body=None, headers=None, raw=False, timeout=120):
    h = dict(headers or {})
    h.setdefault("User-Agent", "Mozilla/5.0 (compatible; videomax-studio/1.0)")  # Cloudflare 1010 blocks the default Python-urllib UA
    data = None
    if body is not None:
        if isinstance(body, (bytes, bytearray)):
            data = body
        else:
            data = json.dumps(body).encode(); h.setdefault("Content-Type", "application/json")
    for attempt in range(3):
        req = urllib.request.Request(url, data=data, method=method, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                b = r.read()
                return b if raw else (json.loads(b) if b else None)
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="ignore")[:400]
            if e.code < 500 or attempt == 2:
                sys.exit(f"HTTP {e.code} {method} {url.split('?')[0]}: {msg}")
        except Exception as e:  # network blip
            if attempt == 2: sys.exit(f"{method} {url.split('?')[0]} failed: {e}")
        time.sleep(2 + attempt * 3)


def token():
    global _tok
    if not _tok:
        d = http("POST", f"{CFG['url']}/auth/v1/token?grant_type=password",
                 {"email": CFG["engine_email"], "password": CFG["engine_password"]}, {"apikey": CFG["anon_key"]})
        _tok = d["access_token"]
    return _tok


def H(extra=None):
    h = {"apikey": CFG["anon_key"], "Authorization": f"Bearer {token()}"}
    h.update(extra or {}); return h


def rest(method, path, body=None, prefer=None):
    h = H({"Prefer": prefer} if prefer else None)
    return http(method, f"{CFG['url']}/rest/v1/{path}", body, h)


def upload(bucket, path, file):
    size = os.path.getsize(file)
    if size > 48 * 1024 * 1024:
        sys.exit(f"{file} is {size/1048576:.1f} MB; upload the social copy (<= 45 MB)")
    ct = mimetypes.guess_type(file)[0] or "application/octet-stream"
    with open(file, "rb") as f:
        http("POST", f"{CFG['url']}/storage/v1/object/{bucket}/{urllib.parse.quote(path)}", f.read(),
             H({"Content-Type": ct, "x-upsert": "true"}), timeout=600)
    return path


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:50] or "video"


ap = argparse.ArgumentParser()
sp = ap.add_subparsers(dest="cmd", required=True)
sp.add_parser("settings")
p = sp.add_parser("scrape"); p.add_argument("--channel")
p = sp.add_parser("untranslated"); p.add_argument("--out")
p = sp.add_parser("translations"); p.add_argument("file")
p = sp.add_parser("jobs"); p.add_argument("--now", action="store_true"); p.add_argument("--kind")
p = sp.add_parser("job"); p.add_argument("id"); p.add_argument("status")
p.add_argument("--progress", type=int); p.add_argument("--step"); p.add_argument("--error")
p = sp.add_parser("source"); p.add_argument("job"); p.add_argument("out")
p = sp.add_parser("export")
for a in ("--title", "--caption-file", "--video"): p.add_argument(a, required=True)
for a in ("--thumb", "--job", "--source-channel"): p.add_argument(a)
p.add_argument("--kind", default="doodle"); p.add_argument("--duration", type=float)
p = sp.add_parser("runlog"); p.add_argument("--videos", type=int, required=True); p.add_argument("--redone", type=int, default=0)
p.add_argument("--sent", action="store_true"); p.add_argument("--note"); p.add_argument("--status", default="ok")
a = ap.parse_args()

if a.cmd == "settings":
    print(json.dumps(rest("GET", "settings?id=eq.1&select=*")[0], ensure_ascii=False, indent=1))

elif a.cmd == "scrape":
    r = http("POST", f"{CFG['url']}/functions/v1/scrape", {"channel_id": a.channel} if a.channel else {}, H(), timeout=400)
    print(json.dumps(r, ensure_ascii=False, indent=1))

elif a.cmd == "untranslated":
    rows = rest("GET", "feed_items?select=id,caption_orig&status=eq.new&caption_vi=is.null&order=scraped_at.desc&limit=300")
    rows = [r for r in rows if (r.get("caption_orig") or "").strip()]
    out = json.dumps(rows, ensure_ascii=False, indent=1)
    if a.out: open(a.out, "w").write(out); print(f"{len(rows)} captions -> {a.out}")
    else: print(out)

elif a.cmd == "translations":
    n = 0
    for r in json.load(open(a.file)):
        if r.get("id") and (r.get("caption_vi") or "").strip():
            rest("PATCH", f"feed_items?id=eq.{r['id']}", {"caption_vi": r["caption_vi"].strip()}); n += 1
    print(f"saved {n} translations")

elif a.cmd == "jobs":
    q = "jobs?select=*,feed_items(id,platform,aweme_id,caption_orig,caption_vi,share_url,views,likes,duration_sec,channels(name,use_original,credit))&status=eq.queued&order=created_at"
    if a.now: q += "&run_when=eq.now"
    if a.kind: q += f"&kind=eq.{a.kind}"
    print(json.dumps(rest("GET", q), ensure_ascii=False, indent=1))

elif a.cmd == "job":
    patch = {"status": a.status, "updated_at": now_iso()}
    if a.progress is not None: patch["progress"] = a.progress
    if a.step is not None: patch["step"] = a.step
    if a.error is not None: patch["error"] = a.error
    rest("PATCH", f"jobs?id=eq.{a.id}", patch); print("ok")

elif a.cmd == "source":
    j = rest("GET", f"jobs?id=eq.{a.job}&select=kind,feed_items(platform,aweme_id,share_url,channels(use_original))")[0]
    f = j.get("feed_items") or {}
    if j["kind"] != "footage" or not (f.get("channels") or {}).get("use_original"):
        sys.exit("this job is not a footage job from a channel marked 'use original video'")
    tk = json.load(open(os.path.join(ROOT, "tikhub.json")))["token"]
    pf, aid = f["platform"], f["aweme_id"]
    q = urllib.parse.quote
    api = {"douyin": f"/api/v1/douyin/web/fetch_one_video?aweme_id={aid}",
           "tiktok": f"/api/v1/tiktok/app/v3/fetch_one_video?aweme_id={aid}",
           "instagram": f"/api/v1/instagram/v2/fetch_post_info?code_or_url={q(f.get('share_url') or aid)}",
           "youtube": f"/api/v1/youtube/web_v2/get_video_streams?video_id={aid}",
           "xiaohongshu": f"/api/v1/xiaohongshu/app_v2/get_video_note_detail?note_id={aid}"}[pf]
    d = http("GET", "https://api.tikhub.io" + api, headers={"Authorization": f"Bearer {tk}"})
    data = d.get("data") or {}
    cand = []  # (score, url): prefer progressive mp4 with audio, highest quality
    def walk(o, ctx=""):
        if isinstance(o, dict):
            mime = str(o.get("mimeType") or o.get("mime_type") or "")
            for k, v in o.items():
                if isinstance(v, str) and v.startswith("http"):
                    key = k.lower()
                    if pf == "youtube":
                        if "url" in key and "video/mp4" in mime and ("mp4a" in mime or o.get("audioQuality") or o.get("audio_quality")):
                            cand.append((int(o.get("height") or o.get("bitrate") or 0), v))
                    elif any(t in key for t in ("url", "src", "master", "backup")) and any(t in (ctx + key + v).lower() for t in ("play_addr", "video", ".mp4", "h264", "stream", "download")) and not any(t in v.lower() for t in (".jpg", ".jpeg", ".webp", ".png", "image", "avatar", "cover")):
                        cand.append((int(o.get("width") or o.get("bit_rate") or o.get("height") or 0), v))
                else:
                    walk(v, ctx + "/" + k.lower())
        elif isinstance(o, list):
            for x in o: walk(x, ctx)
    walk(data)
    cand.sort(key=lambda c: -c[0])
    ref = {"douyin": "https://www.douyin.com/", "tiktok": "https://www.tiktok.com/", "instagram": "https://www.instagram.com/",
           "youtube": "https://www.youtube.com/", "xiaohongshu": "https://www.xiaohongshu.com/"}[pf]
    seen = set()
    for _, u in cand:
        if u in seen: continue
        seen.add(u)
        if len(seen) > 8: break
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0", "Referer": ref})
            with urllib.request.urlopen(req, timeout=300, context=CTX) as r, open(a.out, "wb") as o:
                o.write(r.read())
            if os.path.getsize(a.out) > 100_000:
                print(json.dumps({"saved": a.out, "bytes": os.path.getsize(a.out), "platform": pf}, ensure_ascii=False)); break
        except Exception as e:
            print("try next url:", str(e)[:100])
    else:
        sys.exit("could not download the source video")

elif a.cmd == "export":
    day = datetime.datetime.now(TZ).strftime("%Y-%m-%d")
    base = f"{day}/{slug(a.title)}-{int(time.time())}"
    vpath = upload("exports", base + ".mp4", a.video)
    tpath = upload("exports", base + ".jpg", a.thumb) if a.thumb else None
    caption = open(a.caption_file).read().strip()
    row = {"title": a.title, "kind": a.kind, "caption": caption, "video_path": vpath, "thumb_path": tpath,
           "duration_sec": round(a.duration) if a.duration else None, "size_bytes": os.path.getsize(a.video),
           "source_channel": a.source_channel, "job_id": a.job}
    ex = rest("POST", "exports", row, prefer="return=representation")[0]
    if a.job:
        rest("PATCH", f"jobs?id=eq.{a.job}", {"status": "ready", "progress": 100, "step": None, "export_id": ex["id"], "updated_at": now_iso()})
        j = rest("GET", f"jobs?id=eq.{a.job}&select=feed_item_id")[0]
        if j.get("feed_item_id"):
            rest("PATCH", f"feed_items?id=eq.{j['feed_item_id']}", {"status": "done"})
    print(json.dumps({"export_id": ex["id"], "video_path": vpath}))

elif a.cmd == "runlog":
    rest("POST", "runs", {"videos": a.videos, "redone": a.redone, "sent_at": now_iso() if a.sent else None,
                          "note": a.note, "status": a.status})
    print("ok")
