# GIF spec — house motion emblems (for the maker: human or ChatGPT)

## Doctrine
GIFs are for REPEATING MOTIFS — images the work returns to, that reward
dwelling (dog, whirlpool, lamp, raft). Draws are FILLER — one gap, one
use, pacing only. If a motif recurs, it graduates from draw to GIF.

## Mechanism
- Files live in `process/image-bank/motion/<slug>.gif` in the lane repo.
- First frame doubles as the still emblem until motion support lands in
  the card pipeline (today: stills only; motion plays later, same files).
- Contact strips (`samples*/contact-sheet*.png`) are the review surface;
  new GIFs get eyeballed onto a strip before adoption.
- Naming: `<motif>.gif` (lowercase, hyphens). No spaces (R2 URLs).

## Technical reference (match the banked set exactly)
- Format GIF89a, loop forever (Netscape loop, 12 frames).
- Portrait ~310x414 or square ~360x360. Keep files 0.5–1.5 MB.
- White background, blue-ink pencil-engraving line style, minimal, arty.
- NO text, NO letters, NO watermark. Seamless loop: last frame must
  flow back into first (still water, held pose, cycle-complete motion).
- Animate the ESSENCE, not the scene: ripple rings, smoke rise, flame
  flicker, wheel turn, water swirl — one moving element, rest still.

## Nibbana motif queue
HAVE: dog-water, cinema, donkey-carrot, sewing-machine, lotus-rain,
lamp-flame, hands-sand, magician, raft, wave-vortex.
NEED: fire-going-out, surgeon, leaning-wall figure, empty hand-mirror,
jewel-in-pond, passbook/exam paper, carpenter tools, chariot team,
relay runner, Mara army, grasping hand, knotted thread, signpost.
Next up: fire-going-out (n01 opening), surgeon (n01), empty mirror (n03).

## Shiva Sutras queue (mined from 78 storyboards)
fire (27x), seed (22x), tree (13x), ocean (12x), wheel (7x), heart (7x),
bird (7x). Verdict: YES — fire first (dominant chant-image), then seed,
ocean, wheel. Same spec, Sanskrit lane needs no script handling.
