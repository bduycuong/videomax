#!/usr/bin/env python3
"""Convert HEIC covers/avatars in Storage bucket `feed` to real JPEG (laptop browsers can't show HEIC).
usage: fiximages.py   (needs: pip install --break-system-packages pillow-heif)"""
import io, json, os, ssl, urllib.parse, urllib.request
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "supabase.json")))
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

def http(method, url, body=None, headers=None, raw=False):
    h = dict(headers or {}); data = None
    if body is not None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        if not isinstance(body, bytes): h.setdefault("Content-Type", "application/json")
    with urllib.request.urlopen(urllib.request.Request(url, data=data, method=method, headers=h), timeout=120, context=CTX) as r:
        b = r.read(); return b if raw else (json.loads(b) if b else None)

tok = http("POST", f"{CFG['url']}/auth/v1/token?grant_type=password", {"email": CFG["engine_email"], "password": CFG["engine_password"]}, {"apikey": CFG["anon_key"]})["access_token"]
H = {"apikey": CFG["anon_key"], "Authorization": f"Bearer {tok}"}
paths = [c["avatar_url"][3:] for c in http("GET", f"{CFG['url']}/rest/v1/channels?select=avatar_url", headers=H) if (c["avatar_url"] or "").startswith("sb:")]
paths += [x["cover_path"] for x in http("GET", f"{CFG['url']}/rest/v1/feed_items?select=cover_path&cover_path=not.is.null&status=in.(new,approved)", headers=H)]
fixed = 0
for p in paths:
    q = urllib.parse.quote(p)
    try:
        b = http("GET", f"{CFG['url']}/storage/v1/object/authenticated/feed/{q}", headers=H, raw=True)
        if b[:2] == b"\xff\xd8" or b[:4] == b"\x89PNG": continue
        im = Image.open(io.BytesIO(b)).convert("RGB")
        out = io.BytesIO(); im.save(out, "JPEG", quality=85)
        http("POST", f"{CFG['url']}/storage/v1/object/feed/{q}", out.getvalue(), {**H, "Content-Type": "image/jpeg", "x-upsert": "true"})
        fixed += 1
    except Exception as e:
        print("skip", p, str(e)[:80])
print(json.dumps({"checked": len(paths), "fixed": fixed}))
