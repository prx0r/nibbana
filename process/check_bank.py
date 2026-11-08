#!/usr/bin/env python3
"""Bank emblem gate: every emblem sample must be white-background only.

Usage: python3 check_bank.py
PASS (exit 0) iff all samples/*-emblem.png + contact-sheet.png have a
white rim (mean > 225). Source photos are exempt (they get matted);
emblems are the law. Owner steer: white / transparent, minimal, arty.
"""
import glob
import os
import sys

from PIL import Image

BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image-bank', 'samples')


def rim_mean(path):
    im = Image.open(path)
    if im.mode == 'RGBA':
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    else:
        im = im.convert('RGB')
    w, h = im.size
    rim = []
    for x in range(0, w, 7):
        rim += [im.getpixel((x, 3)), im.getpixel((x, h - 4))]
    for y in range(0, h, 7):
        rim += [im.getpixel((3, y)), im.getpixel((w - 4, y))]
    return sum(sum(p) / 3 for p in rim) / len(rim)


def main():
    bad = 0
    for f in sorted(glob.glob(os.path.join(BANK, '*.png'))):
        m = rim_mean(f)
        ok = m > 225
        bad += not ok
        print(('PASS' if ok else 'FAIL') + f' {m:6.1f} {os.path.basename(f)}')
    print('BANK ' + ('GREEN' if not bad else f'RED ({bad} non-white)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
