#!/usr/bin/env python3
"""Send MAX WISE videos or a message to Telegram.

usage:
  python3 telegram_send.py <config.json> text "<message>"
  python3 telegram_send.py <config.json> video <file.mp4> "<caption>"
config.json = {"token": "...", "chat_id": 123}
"""
import json, subprocess, sys

cfg = json.load(open(sys.argv[1]))
base = f"https://api.telegram.org/bot{cfg['token']}"
kind = sys.argv[2]
if kind == "text":
    cmd = ["curl", "-sS", "-m", "60", f"{base}/sendMessage", "-d", f"chat_id={cfg['chat_id']}",
           "--data-urlencode", f"text={sys.argv[3]}", "-d", "disable_web_page_preview=true"]
elif kind == "video":
    # --form-string: captions start with "<b>", which plain -F would read as a file path
    cmd = ["curl", "-sS", "-m", "600", f"{base}/sendVideo", "--form-string", f"chat_id={cfg['chat_id']}",
           "-F", f"video=@{sys.argv[3]}", "--form-string", f"caption={sys.argv[4][:1024]}",            "--form-string", "supports_streaming=true", "--form-string", "width=1080", "--form-string", "height=1920"]
else:
    raise SystemExit("kind must be text or video")
for attempt in range(3):
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    try:
        r = json.loads(out)
        if r.get("ok"):
            print("sent ok"); break
        print("telegram error:", r)
    except Exception:
        print("bad response:", out[:300])
else:
    sys.exit(1)
