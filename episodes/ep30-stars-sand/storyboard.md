# ep30 — More stars in the universe than grains of sand on Earth?

Confidence LOW: framed as a match-up (stars vs sand), never settled; ends with "vote in the comments".
Facts: Universe Today "Are there more grains of sand than stars?" (universetoday.com/106725): beaches ≈ 5 sextillion grains (Jason Marshall estimate, range 2.5–10 sextillion); stars ≥ 10 sextillion (100 billion galaxies × 100 billion stars). The Naked Scientists "More stars in the Universe, or sand on Earth?" (thenakedscientists.com/node/192226, Michael Merrifield, Nottingham): ~10,000 grains per metre → ~10^12 per m³; Sahara ~10 million km² × 1 cm = 10^11 m³ → ~10^23 grains; counting faint small galaxies lifts stars ~×10 to ~10^23. Scientific American source page (topics.json) could not be fetched (permission timeout).
Arithmetic (Python): 1e11 × 1e11 = 1e22 (ten sextillion); 1e22 / 5e21 = 2 (two to one); 1e7 km² × 1e6 m²/km² × 0.01 m = 1e11 m³; × (1e4)^3 = 1e23 (a hundred sextillion); 1e22 × 10 = 1e23.

| scene | picture | idea | reveal on word | technique |
|---|---|---|---|---|
| hook | night card with twinkling stars vs paper card where seeded sand grains really fall and pile; "VS" stamp | the match-up | "stars", "grains of sand" | 1 simulate + 10 gag |
| guess | three sticky notes Stars? / Sand? / A tie? | options | each option | 12 containers first |
| intro | MAX WISE + scoreboard STARS 0 : 0 SAND inks itself | plan | "count both sides" | ink |
| galaxy | 3D: spiral galaxy of points, camera pulls back until 100 billion galaxies appear; labels 100,000,000,000 | stars per galaxy × galaxies | "hundred billion stars", "hundred billion galaxies" | 4 one continuous camera move (three.js) |
| stars | 100 billion × 100 billion = 10 sextillion; the digits 1 and 22 zeros pop one by one, bracket inks "22 zeros" | the star total | "ten sextillion", "twenty two zeros" | 2 countable units + ink |
| grain | 1 m ruler inks, a grain rides along it while a counter climbs to 10,000; a cube inks: 1 m³ ≈ 1 trillion grains | sand per volume | "ten thousand", "one metre", "trillion" | 3 ruler + along |
| beach | two bars: STARS 10 sextillion vs BEACHES 5 sextillion ("one estimate" tape); "2 : 1" stamp | round one result | "five sextillion", "two to one" | 12 containers + comparison |
| desert | Sahara outline inks; thin hatched 1 cm slab cutaway; ≈ 100 sextillion grains; a dune with a growing depth arrow "deeper!" | sand fights back | "Sahara", "one centimetre", "hundred sextillion", "deeper" | 11 texture + 6 cutaway + ink |
| recount | the stars bar morphs from 10 to 100 sextillion while faint stippled galaxies pop around | stars fight back | "faint little galaxies", "hundred sextillion" | 5 one object + morph |
| verdict | honest-range bands on a sextillion axis: stars 10–100, sand 5–100+ with "?" arrow; chips "only beaches → stars", "every desert → sand?" | it depends | "only beaches", "every desert" | 9 honest ranges |
| outro | two vote boxes STARS / SAND with checkmark ink, "Vote in the comments!", Stay curious | callback + vote | "vote", "stay curious" | 10 callback + ink |
