# Footage sources (allow-list)

`channels.json` is the ONLY list of channels the daily run may pull videos from (via TikHub).
Add a channel only if it is yours or you have permission to reuse its videos. Every entry needs a
`permission` note — entries without one are skipped automatically.

```json
[
  {
    "name": "My factory channel",
    "platform": "douyin",                     // "douyin" or "tiktok"
    "url": "https://www.douyin.com/user/MS4wLjABAAAA...",
    "permission": "own channel",              // or e.g. "written permission from <owner>, 2026-10-26, via email"
    "credit": "",                             // optional: text to add to the caption, e.g. "🎥 @factorychannel"
    "max_per_week": 3
  }
]
```

`sec_user_id` is filled in automatically on the first run. `seen.json` lists videos already used.
