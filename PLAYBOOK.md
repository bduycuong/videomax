# MAX WISE — daily cloud production playbook

Series: 60–75 s vertical (1080×1920) doodle explainers for Cuong. Narrator **Max**, an original hand-drawn robot (square head with yellow screen face, "Max" chest label, stick arms/legs, red antenna bulb). Every episode opens with a **curious question**, invites a guess, then works out the answer step by step. Male US English voice (Andrew), EN word-by-word subtitles + VI sentence subtitles, music bed + SFX. Ends with "Stay curious!". Everything runs in the cloud container; the user's computer is not needed.

Repo layout (`bduycuong/videomax`, default branch `main`):
- `engine/make_audio.py <episode_dir> <project_dir>` — copies template/assets, TTS per scene, voice.mp3, bgm.mp3, timing.json, mouth.json
- `engine/maxwise.py <episode_dir> <project_dir>` — builds the HyperFrames project (Max rig, captions, SFX, scenes from the episode)
- `engine/telegram_send.py <telegram.json> text|video ...`
- `episodes/ep01-blinking/` — **reference episode**: read `script.json` and `scenes.py` before writing a new one
- `topics.json` — topic queue (status todo/done), each fact-checked with a source
- `telegram.json` — bot token + chat_id (never print the token in replies or logs)
- `log/YYYY-MM-DD.md` — one short log per run

## 0. Setup
- The repo should be at `/home/claude/videomax`. If it is missing, call the `add_repo` tool (owner `bduycuong`, repo `videomax`, access `push`), then `git clone --depth 1 https://github.com/bduycuong/videomax /home/claude/videomax` (10-min timeout).
- `pip install --break-system-packages -q edge-tts` if `import edge_tts` fails. `npx hyperframes --version` must work. Work dir for projects: `/home/claude/videomax/work/` (git-ignored).
- Telegram: if `telegram.json` has `chat_id: null`, call `https://api.telegram.org/bot<token>/getUpdates` and take the chat id of the most recent private message; save it into `telegram.json`. If there is still none, the user has not pressed Start in t.me/usvideoagent_bot yet — continue production, and at delivery time commit the mp4s to `pending/` instead of sending (see step 13).

## Daily run (2 episodes, then deliver at 08:00 Asia/Saigon)

1. **Pick 2 topics**: the first two `status:"todo"` items in `topics.json` (already ordered by fit). Prefer confidence "cao"/"vừa"; a "thấp" topic must be framed as a mystery/debate, never as settled fact. If fewer than 2 remain, research new curious questions (lifetime tallies, weird body, mind-blowing scale), verify each with a reputable source (NIH, NASA, NOAA, USGS, CDC, BLS, peer-reviewed, Scientific American, BBC Science Focus, Library of Congress Everyday Mysteries), and append them to `topics.json` in the same format.
2. **Re-check the facts**: open the topic's `source_url` (WebFetch) and confirm the numbers you will use. Do your own arithmetic in Python. Never copy source text; write in your own words.
3. **Episode number**: next number after the highest `episodes/epNN-*` folder. Folder `episodes/epNN-<slug>/`.
4. **Write `script.json`** (same shape as ep01): ~9–12 scenes, 55–75 s total, ~150–190 words.
   - Order: `hook` (the curious question) → `guess` (invite a guess, 3 options) → `intro` (exactly: "I'm Max, and this is Max Wise." + one short line) → 4–7 explanation scenes that build the answer one step at a time (each step = one number or one idea) → optional twist/bonus/tip → `outro` (answer recap + "Stay curious!"). Scene ids: short lowercase words; `intro` required; the last id must be `outro`.
   - `en`: list of sentences. **Spell all numbers as words; no digits, no hyphens, no symbols** (TTS word boundaries must match the word count). Conversational, short sentences.
   - `vi`: natural Vietnamese translation, one entry per EN sentence (digits allowed here).
4b. **Storyboard first** (`episodes/epNN-<slug>/storyboard.md`): one line per scene — picture, the one formal idea, what appears on which spoken word, how it hands over to the next scene, and which technique from the *Visual technique bank* below it uses. Use at least 4 different techniques per episode and never the same one in two consecutive scenes. Then code it.
5. **Write `scenes.py`** following ep01 exactly: sections `# === SCENES ===`, `# === GESTURES ===`, `# === SFX ===`.
   - One `scenes["<id>"] = scene_file(id, css, html, js[, fade])` per script scene; the last scene `outro` uses `fade=False`.
   - Anchor every reveal to the word that says it with `aw(scene_id, "phrase")` (phrase = consecutive spoken words). Helpers in scope: `pop`, `rise`, `draw`, `count`, `blink`, `fmtInt` (JS); `eye_svg`, `boil_defs`, `C`, `K`, `WS`, `SKETCH` (Python). Classes: `.h1 .h2 .hl .chip .card .pill .big .blue .red .hatch-r`.
   - Look: hand-drawn doodle on lined notebook paper; ink outlines (`WS`), yellow highlighter, blue/red pen, sketchy borders (`SKETCH`), hatching. Every number on screen = the number spoken. One clear picture per scene (a diagram that grows, a counter, a ruler, a comparison, a myth crossed out). No emoji, no stock icons, no copyrighted characters or logos.
   - Layout: content in y 150–960 px. Max stands bottom-left (x 0–400, y 860–1340) except during `intro` and `outro` (centre) — keep that zone clear. Subtitles occupy x 390–990, y ~1000–1310 — keep it clear too. Nothing important below y 1340.
   - Element ids must be unique per scene file (prefix with a scene abbreviation). Initial hidden states go in CSS/inline `style`, not `tl.set(..., 0)`. Use `fromTo`, never `from`.
   - GESTURES: `think(t0, t1)`, `point(t, hold, ang)`, `wow(t, hold)`, `wave(t, n)` with `g(scene_id, "phrase")` for absolute times. Typical: think on the hook question, point at the guess options, wave on "I'm Max", point/wow on the big reveals, wave on "Stay curious".
   - SFX: `sfx += [(file, A(scene_id, "phrase"), volume), ...]` — files: pop, ping, click, click-soft, sparkle, riser, impact-bass-1, impact-bass-2, whoosh-short (`.mp3`; scene whooshes are added automatically). 6–12 hits, each with a visible cause.
6. **Build**: `python3 engine/make_audio.py episodes/epNN-slug work/epNN` then `python3 engine/maxwise.py episodes/epNN-slug work/epNN`. If make_audio reports a word/boundary mismatch, rewrite that sentence (remove digits/hyphens/symbols) and rerun.
7. **QA** in `work/epNN`: `npx hyperframes check --json` (fix every error), then `npx hyperframes snapshot --at <mid-time of every scene, comma separated> --no-end -o ../snap_epNN` and LOOK at the contact sheet(s) with Read. Fix overlaps, clipped text, things hidden behind Max or the subtitles, empty scenes. One fix pass, then re-snapshot only the changed scenes.
8. **Render**: `npx hyperframes render -o renders/epNN-<slug>.mp4 -q delivery --quiet` (~5–8 min). Run it with the Bash tool's own background mode or in the foreground with a 10-minute timeout — never with `&` or nohup, which gets killed when the shell exits. If integrated loudness is below −17 LUFS, re-normalise the audio only: `ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-16:TP=-1.5 -c:a aac -b:a 192k out.mp4`. Verify with ffprobe (duration) and `ffmpeg -af ebur128` (integrated ≈ −16 LUFS, peak ≤ −1 dB).
9. **Caption** per video = a ready-to-post social caption, **English only, plain text, nothing else** (no HTML tags, no Vietnamese, no episode number, no sources — those go in the log). Format exactly:
   - line 1: the hook question (the episode title)
   - line 2: one short teaser line that makes people watch (do not give the full answer away), optionally one emoji
   - blank line
   - line 4: 6–10 English hashtags on one line, mixing broad (#science #funfacts #didyouknow #learnontiktok) and topic-specific ones (e.g. #sleep #humanbody), always ending with #MaxWise
   Keep it under 300 characters so it copies cleanly into TikTok / Reels / Shorts.
10. **Commit the sources** (not the mp4s): `episodes/epNN-<slug>/` (script.json, scenes.py), updated `topics.json` (status "done", episode, done_date), `telegram.json` if chat_id was filled, and `log/<date>.md` (titles, durations, loudness, any problems). `git pull --rebase origin main` then push to `main`.
11. **Wait for 08:00**: if the videos are ready before 07:55 Asia/Saigon, wait until 07:55 (a background `sleep` or a Monitor until-loop on the clock) — do not send early. If it is already past 07:55, send immediately.
12. **Deliver**: for each video `python3 engine/telegram_send.py telegram.json video <mp4> "<caption>"` with the plain-text caption from step 9. Send nothing else on a normal day (no summary message). Also send any mp4s waiting in `pending/` first, then delete them from `pending/` and commit. Only send an extra short Vietnamese text when something failed.
13. **If delivery is impossible** (no chat_id, Telegram error after 3 tries): commit the mp4s to `pending/<date>-epNN.mp4` and note it in the log, so the next run sends them.
14. **If an episode fails** after one fix attempt, still ship the other one and explain the failure in a short Telegram text and the log. If both fail, send a short Vietnamese text saying what went wrong.

## Visual technique bank

Distilled from studying ~100 explainer prompts people shared for code-rendered videos (rewritten in our own words, adapted to Max's doodle world). Pick per scene in the storyboard.

1. **Simulate, don't illustrate.** When the idea is a process, run the real thing in code (seeded, so every frame is a function of time): a real random walk, dots that actually fall and pile, a counter computed from the rate. The viewer feels the number.
2. **Countable units.** Turn a huge quantity into things you can count: 1 bathtub = 150 L, 1 dot = 1 million people, 1 square = 1 week of life. Fill the page unit by unit, then zoom out to show how many.
3. **The ruler that never leaves.** For scale stories (paper to the Moon, heartbeats, ants), keep a hand-drawn ruler or counter on one edge that updates as the camera moves, so the scale is always readable.
4. **One continuous camera move.** Instead of cutting, push into a detail of the last drawing until it becomes the next scene (zoom into the eye's pupil → the brain), or pull out to reveal the bigger picture. Wrap the scene in a group and animate its scale/position; hand off on a spoken word.
5. **One object, many states.** Let a single doodle object morph through the story (a sticky note becomes a bar becomes a ruler) rather than replacing it, so the eye never loses the thread.
6. **Cutaway / exploded view.** Slice the object open with a dashed cut line and slide its parts apart with tape labels (the knuckle joint, the stomach, the onion cell). Labels sit on the part they name, with a leader line.
7. **Myth crossed out.** Write the popular wrong number in pencil, strike it with a red pen stroke, write the real one with the highlighter. Great for "10 bacteria per cell", "two swimming pools of spit".
8. **Side-by-side timeline.** Run two clocks at once: what happens to the subject vs. what happens to you/the world meanwhile (while a photon crawls out of the Sun, humans invent farming).
9. **Honest ranges.** When sources disagree, show the range as a hand-drawn error bar or a shaded band ("2–3.5 years") and say "about". Never fake precision.
10. **Onomatopoeia and visual gags.** Hand-lettered sound words for the key action (POP!, GRRR, SNAP), a tiny gag in Max's reaction, and a callback to the hook in the outro.
11. **Hand-made textures, one system.** Vary the drawing technique between scenes — hatching, stipple dots, coloured-pencil fill, paper cut-outs, sticky notes, washi-tape labels, typewriter-tape captions — while keeping the same palette, ink weight and fonts so it still looks like one show.
12. **Containers move first.** Content enters after its card/arrow starts moving and leaves before the next one moves, so text never overlaps; small overshoot (back.out / elastic), never linear for objects.
13. **Hit the beat.** Snap scene hand-offs and SFX hits to the nearest beat of the music bed when one is within ~0.15 s (`npx hyperframes beats assets/bgm.mp3 --json`); the voice still decides the order.
14. **Curiosity gap + counter-intuition.** The hook poses a question the viewer thinks they can answer; the guess scene offers the intuitive (wrong) answer; one scene flips it. Use an everyday analogy for every abstract step.
15. **Grade your own stills.** In QA, give each scene's snapshot a 1–10 score for clarity (one idea, readable in 1 s, nothing hidden by Max or subtitles) and fix the lowest two before rendering.

## Footage episodes (real video + Max)

Reference: `episodes/f01-wool-to-sweater/` (script.json with `src` ranges, scenes.py, footage.json). Source videos come ONLY from the allow-list `sources/channels.json` (each entry has a `permission` note) or from files Cuong sends himself. Never pull from a channel that is not on the list, and never add channels or permission notes yourself.

Daily: after the 2 doodle episodes, if `tikhub.json` has a token and the allow-list is not empty, make **1** footage episode (skip quietly if there is no new candidate).

F1. `python3 engine/tikhub_pull.py --max 1` → `work/footage/<key>.mp4` + `.json` (channel, permission, desc, likes). It reports skipped channels; mention them in the log.
F2. Inspect the video: ffprobe; a 12-frame contact sheet; 3 full-resolution frames. Find every burned-in caption, logo and watermark with text (any language) and choose a crop `[w, h, x, y]` that keeps the subject and leaves all of them out (vertical sources: crop to a landscape-ish window that avoids them). If text sits over the subject so it cannot be cropped out, skip this video and log why.
F3. Understand it: transcribe with faster-whisper (`language` of the source), scene-detect shots (`select='gt(scene,0.3)',showinfo` on a 480 px copy), map the steps to time ranges.
F4. `script.json` (scenes `hook`, `intro`, …, `outro`; each with `"src": [start, end]` in source seconds and `vi` = "" strings): a NEW English script in your own words that explains what the footage shows — a curious-question hook, the steps, at least one fact checked at a reputable source (not only the source video's claims), "Stay curious!" ending. 80–110 s. Same no-digits/no-hyphens rule for `en`.
F5. `footage.json` = `{"source": "<abs path>", "crop": [w,h,x,y]}`.
F6. `scenes.py` like f01: step chip in the top zone (y 110–220), at most 1–2 doodle tags/stickers on the panel (x 20–1060, y 230–898), notes right of Max (x 430–1040, y 905–995). Max stays bottom-left automatically in footage mode; subtitles are English-only.
F7. Build: `make_audio.py` → `engine/footage_panel.py <ep> <proj>` → `maxwise.py` → check → snapshot every scene and LOOK (no source text visible anywhere, nothing hidden) → render. Original audio is dropped (voice + music + SFX only). Make a social copy ≤ 45 MB for Telegram: `ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 23 -maxrate 6M -bufsize 12M -c:a aac -b:a 160k -movflags +faststart out.mp4`.
F8. Caption: same English-only format; if the channel entry has `credit`, add it as the last line before the hashtags.
F9. Commit the episode folder (no mp4s) and `sources/seen.json`; note the source channel + permission in the log.
