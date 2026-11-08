# NIBBANA-INTAKE.md — lane log (decisions + unsure list)

## Source
ChatGPT export `ChatGPT-Plan Nibbana Readings-20261107-1405.md` (R2 ayoutube,
exported 2026-11-07, 12 prompt turns). 10 "Mind Stilled" installments =
Chapters I–X, sermons 1–33, colophon "End of Chapter X. End of all 33
sermons." verified: sermon numbers 1–33 all present, none missing.

## Split (2026-11-08, counts asserted)
- 10 units `chapters/n01..n10.md`, 6.6k–17k words each. Ch I sermons 1–3
  through Ch X sermons 29–33 (~3 sermons per chapter).
- Installment 1's planning preamble ("ten-chapter architecture" + rigor
  note, 9.5k chars) moved verbatim to `process/plan-architecture.md`
  (reference, never renders).
- Exporter footer ("Powered by ChatGPT Exporter") dropped; no prose lost.
- n10 tail keeps the Practical Afterword teaser (delivered prose).
- Pre-installment chat jacket (title + first prompt/response) excluded.

## Lane shape (proposed, needs owner confirm)
- 10 units n01–n10, scheme nNN. Pali (not Sanskrit): term cards roman-only,
  no Devanagari — owner call.
- Thumbnail: `assets/thumbnail/series.png` set (Ñāṇananda portrait, 253px,
  Shiva spec).

## Language rule (owner call 2026-11-08)
NO PALI anywhere in video: no diacritics, no Pali headwords on cards,
no Pali in subtitles or TTS. Names normalized to plain ASCII
(Ñāṇananda→Nanananda, Kaṭukurunde→Katukurunde, Anālayo→Analayo).
Key terms render as English equivalents only; glossary is English-only.
Measured load is light — 1.6% of words carry diacritics, mostly names.
Same class as the subtitle-Deva ban: fix the data, never the renderer.

## n01 draft decision (2026-11-08, reversible)
n01 file held TWO Chapter I drafts plus chat debris. Kept the original
("The Fire That Went Nowhere") — matches the architecture and the
colophon's recurring whirlpool motif. Revised draft filed verbatim at
process/n01-alt-draft.md; owner may swap. Chat prompt/response wrappers
dropped; 345 utm params stripped lane-wide.

## Draw logic (owner steer 2026-11-08)
Nibbana is the draw-logic showcase lane: exposition-heavy, long holds,
white-gap-prone by construction. Pipeline unchanged — storyboards first,
scan_holds flags gaps, draws filed per gap (propose_draws → draws_nNN),
fading in between two onsets per the 60s law. No draws without a
flagged gap; audit_white_gaps first (BUG→engine, else honest white).

## Unsure list (owner calls before render)
1. ~~Pali card treatment~~ — RESOLVED above (no-Pali rule).
2. Numerals/headers per unit (sermon refs on screen?).
3. Voice casting: TTS granny/man/verse vs lecture audio (no Nibbana
   lecture audio held locally — TTS assumed).
4. Glossary sources: Ñāṇananda text + Anālayo comparative notes (scholar
   mining needed; no local glossary yet).
5. Lane wiring: lane.py + project.json + holds routing not yet written.
6. Approvals: none yet (owner act at render time).

## Visual rule (owner law 2026-11-08)
Sanskrit units storyboard as normal (verse/term cards fire on confirmed
glossary). Non-Sanskrit units (this lane) NEVER earn cards — white is
structural, filled only by draws/video additions. Scans prove it: 0 cues
lane-wide, ~8-40 white gaps per chapter. Draws and motion carry this lane.

## Cozy pass (owner steer 2026-11-08)
67 swaps lane-wide, all green, vetoable: fucking→flipping,
fucked→stuffed, fucker→thief, fuck→heck, bastard→sod, shit→blast,
bloody→blimming, Christ→Crikey, FOR FUCK'S SAKE→FOR GOODNESS' SAKE.
Same meter, irreverence kept. R2 export canonical if reverting.

## Full-lane annoyance sweep (2026-11-08, autonomous)
CUT: 8 tail chat turns (n02-n09), 137 spoken-dash blocks lane-wide,
n01's duplicate Chapter I (alt filed at process/). Nibbana verified
zero Deva/diacritics all 10. Heuristic misfires on short comic quotes
(n01) restored by hand. Title drops intact (b1 all chapters); n01 beat
proposals recounted. Glossaries now all 10 (heading candidates, glosses
empty). LEFT deliberately: mid-text Tantrasara refs in Paramarthasara
(11, substantive comparison — only intros ordered clean); "Right."
wallpaper (author rhythm — say the word); Paramarthasara openers already
varied per direction. All 10 storyboards green, sheets + manifests fresh.

## Motion bank (owner-made, 2026-11-08)
10 GIFs from R2 ayoutube → process/image-bank/motion/. Nine uniform
310x414 12-frame pencil-engraving pieces (dog-at-water #1 confirmed) +
358px engraved vortex forming-to-calm. Style: blue-ink engraving on
white — house aesthetic match. First frames double as still emblems;
motion needs the builder decision before rendering.

## Images (2026-11-08)
Scan n01: 8 white gaps (301s opening … 448s whirlpool). Seal drafts for
all 8 at process/proposed_draws_n01.md (small-on-white geometry).
Banked sources: Hiroshige Naruto whirlpool (PD emblem), Wellcome
Bhavacakra (CC-BY, 12-link crops), Kyosai fish-whirlpool (CC0).
Pixabay: bot-walled from here, videos don't fit the card pipeline —
owner-side browsing only (whirlpool/fire/raft loops under free license).
Paid gen steps need explicit confirm + keys at render site.
Pixabay key stored at ~/.pixabay_key (600, outside repos). Banked 8
emblem photos (process/image-bank/px-*.jpg, ≤400px, verified by eye):
candle-smoke, funnel, surgeon, raft, dog-reflection, oil-lamp,
sandcastle, magician. Pixabay /get/ full-size URLs are bot-walled;
CDN _640 pattern works. Videos noted but don't fit card pipeline.

## Series opening (owner steer 2026-11-08, OVERRIDDEN same day)
n01 COLD-OPENS on "Sri Lanka. 1988." — series header, byline, chapter
title and prologue heading cut from voicing (filed verbatim at
process/n01-preamble-removed.md). First voiced block is b1 Sri Lanka.
n01 title drop removed (no title block; theme runs n02-n10). n02-n10
keep series header + byline + question shape.

## Title theme (owner order 2026-11-08 — renders as drops)
3.0s hold after "Nibbana - The Mind Stilled" spoken, EVERY chapter.
Mechanism: drops_nNN.json {title-bid: {pause 3.0, why}} — exact seconds
(Fish tags are model-timed, drops are exact). Filed for all 10 (title is
b1 everywhere). Gate currently blind to them (lane-awareness debt below)
but they execute at render once routing lands.

## All-chapter storyboards GREEN (2026-11-08)
n01 346 through n10 2156 blocks; 0 errors 0 warnings each after
provisional rule-cast (man=self-talk/patient/comic/caps, granny=doctrine/
teacher; ~434 calls total, casting/cast_nNN.md sheets await M/G bless —
nothing renders on provisional voices without it). Along the way: 2
msword droppings + 1 embedded stock image stripped at source (lotus-leaf
motif banked in prospectus), Pali surgery confined to n01 (only chapter
carrying Deva/Pali lines).
Shared-code debt before render: gate lane-awareness (H-list path +
drops resolution), holds.lane_for routing, render-path parametrization
(NEW-LANE §4). 149-block longest group noted as TTS watch item.

## Prelim complete n01 (2026-11-08)
359→344 blocks, storyboard GREEN (0e 0w), frozen at
storyboards/storyboard_n01.json. 25 quotes provisionally cast
(man=skeptic/patient, granny=teacher; casting/cast_n01.md awaits M/G).
Glossary: 13 English-only candidates, glosses empty for owner.
9 pause proposals at beat breaks (drops_n01.proposed.json — proposed
only, gate still sees none filed). Pali surgery: 15 Deva/Pali/label
lines dropped (English translations kept), 166 tokens ASCII-folded
(process/pali_fold_map.json), 265+84 citation/link debris stripped.
Lane wired (projects/nibbana: lane.py + project.json, loads + resolves).
Review pack review/n01/manifest.json pins SHAs.
Honest REDs at prelim (all resolve downstream): no confirmed glossary
yet, intro hold 302s to first card change (thumbnail + blessed drops +
confirmed cards break it), H8 448s max unchanged (draw showcase).
Shared-code debt before render: gate lane-awareness (H-list path),
holds.lane_for routing, render-path parametrization (NEW-LANE §4).
149-block longest group noted as TTS watch item.

## Next (autonomous, gates decide)
storyboard n01 → casting sheets → provisional cast → glossaries →
review packs → approval → render (video path busy: shiva chain running).

House visual law: videofactory/docs/VISUALS.md (ladder: Deva+gloss → GIF motifs → drawn landscapes; white law).

## Om intro (2026-11-08)
Source: bookfactory media/youtube_short_jWTj7Gk_o5Q.mp3 (45s, 3 chants;
silence map: chant1 ends 13.2s, chant2 starts 17.1s). First cut 0-14.5s
(lossless -c copy on render box, Rule 8), verified clean tail into
silence. Staged: assets/om-intro-first-chant.mp3 (342KB).
