#!/bin/bash
# Render the share cards to the PNGs Facebook actually accepts.
# QuickLook draws an SVG into a square bitmap anchored at the top and
# sips only crops from the centre, so og.py pads each card into the
# middle of a 1200x1200 field; cropping 630 back out lands on the card.
set -e
cd "$(dirname "$0")/.."
python3 tools/art/og.py
mkdir -p docs/assets/og
for svg in build/og/*.svg; do
  name=$(basename "$svg" .svg)
  rm -f "build/og/$name.svg.png"
  qlmanage -t -s 1200 -o build/og "$svg" >/dev/null 2>&1
  sips --cropToHeightWidth 630 1200 "build/og/$name.svg.png" \
       --out "docs/assets/og/$name.png" >/dev/null 2>&1
  printf "  %-20s %s %s\n" "$name.png" \
    "$(sips -g pixelWidth -g pixelHeight "docs/assets/og/$name.png" | awk '/pixel/{printf "%sx", $2}')" \
    "$(ls -lh "docs/assets/og/$name.png" | awk '{print $5}')"
done
