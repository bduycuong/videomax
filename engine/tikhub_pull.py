#!/usr/bin/env python3
"""Pull new videos from ALLOW-LISTED channels via TikHub and download them for footage episodes.

usage: python3 engine/tikhub_pull.py [--max 2] [--days 14] [--dry]
reads   tikhub.json            {"token": "..."}
        sources/channels.json  list of channels (see sources/README.md)
writes  work/footage/<platform>-<id>.mp4 + .json, and sources/seen.json (ids already used)

Only channels with a non-empty "permission" field are pulled. Channels without one are skipped
and reported — never fill that field in on the user's behalf.
"""
import argparse, json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.tikhub.io"
CA = "/root/.ccr/ca-bundle.crt"

ap = argparse.ArgumentParser()
ap.add_argument("--max", type=int, default=2, help="max videos to download this run")
ap.add_argument("--days", type=int, default=14, help="only consider posts newer than this")
ap.add_argument("--dry", action="store_true", help="list candidates, download nothing")
args = ap.parse_args()

cfg = json.load(open(os.path.join(ROOT, "tikhub.json")))
if not cfg.get("token"):
    sys.exit("tikhub.json has no token yet")
chs = json.load(open(os.path.join(ROOT, "sources", "channels.json")))
seen_p = os.path.join(ROOT, "sources", "seen.json")
seen = set(json.load(open(seen_p))) if os.path.exists(seen_p) else set()

import ssl
ctx = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

def get(path, **params):
    url = f"{API}{path}?{urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, '')})}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {cfg['token']}"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                d = json.load(r)
            if d.get("code") == 200: return d.get("data") or {}
            print("tikhub error", path, d.get("code"), str(d.get("message"))[:120])
        except Exception as e:
            print("tikhub retry", path, e)
        time.sleep(3)
    return {}

def sec_uid(ch):
    if ch.get("sec_user_id"): return ch["sec_user_id"]
    path = "/api/v1/douyin/web/get_sec_user_id" if ch["platform"] == "douyin" else "/api/v1/tiktok/web/get_sec_user_id"
    d = get(path, url=ch["url"])
    return d if isinstance(d, str) else (d.get("sec_user_id") or d.get("sec_uid") or "")

def posts(ch, sid):
    if ch["platform"] == "douyin":
        d = get("/api/v1/douyin/web/fetch_user_post_videos", sec_user_id=sid, count=20)
    else:
        d = get("/api/v1/tiktok/app/v3/fetch_user_post_videos", sec_user_id=sid, count=20)
    return d.get("aweme_list") or []

def play_url(a):
    v = a.get("video") or {}
    for key in ("play_addr", "download_addr", "play_addr_h264"):
        u = ((v.get(key) or {}).get("url_list") or [])
        if u: return u[0]
    for br in v.get("bit_rate") or []:
        u = ((br.get("play_addr") or {}).get("url_list") or [])
        if u: return u[0]
    return ""

cands, skipped = [], []
cutoff = time.time() - args.days * 86400
for ch in chs:
    if not str(ch.get("permission", "")).strip():
        skipped.append(ch.get("name") or ch.get("url")); continue
    sid = sec_uid(ch)
    if not sid:
        print("could not resolve", ch.get("name")); continue
    ch["sec_user_id"] = sid
    for a in posts(ch, sid):
        aid = str(a.get("aweme_id"))
        if not aid or f"{ch['platform']}-{aid}" in seen or a.get("create_time", 0) < cutoff: continue
        st = a.get("statistics") or {}
        dur = (a.get("duration") or (a.get("video") or {}).get("duration") or 0) / 1000
        if dur and not (20 <= dur <= 300): continue
        cands.append({"key": f"{ch['platform']}-{aid}", "channel": ch.get("name"), "permission": ch["permission"],
                      "platform": ch["platform"], "aweme_id": aid, "desc": a.get("desc", ""), "duration_s": dur,
                      "likes": st.get("digg_count", 0), "plays": st.get("play_count", 0),
                      "create_time": a.get("create_time"), "url": play_url(a)})
json.dump(chs, open(os.path.join(ROOT, "sources", "channels.json"), "w"), ensure_ascii=False, indent=1)
cands.sort(key=lambda c: -c["likes"])
if skipped: print("SKIPPED (no permission recorded):", ", ".join(map(str, skipped)))
print(f"{len(cands)} new candidates")
for c in cands[:10]: print(f"  {c['key']}  {c['likes']:>9} likes  {c['duration_s']:.0f}s  {c['channel']}  {c['desc'][:60]}")
if args.dry: sys.exit(0)

out = os.path.join(ROOT, "work", "footage"); os.makedirs(out, exist_ok=True)
got = 0
for c in cands:
    if got >= args.max: break
    if not c["url"]: continue
    dst = os.path.join(out, c["key"] + ".mp4")
    req = urllib.request.Request(c["url"], headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.douyin.com/" if c["platform"] == "douyin" else "https://www.tiktok.com/"})
    try:
        with urllib.request.urlopen(req, timeout=180, context=ctx) as r, open(dst, "wb") as f:
            f.write(r.read())
    except Exception as e:
        print("download failed", c["key"], e); continue
    json.dump(c, open(dst[:-4] + ".json", "w"), ensure_ascii=False, indent=1)
    seen.add(c["key"]); got += 1
    print("downloaded", dst)
json.dump(sorted(seen), open(seen_p, "w"), indent=1)
print("done:", got, "downloaded")
