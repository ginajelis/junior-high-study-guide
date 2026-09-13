"""Hero, take two: proper back-view figure, clearer staging."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style import (W, H, INK, PAPER, CLAY, CLAY_D, SAGE, SAGE_D, BLUE, BLUE_D,
                   SKIN, WHITE, defs, speed, wrap)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "docs", "assets", "art")

HAIR = "#3E3630"
HAIR_HI = "#5E524A"

hero = wrap(f'''{defs(accent=CLAY)}
  <rect width="{W}" height="{H}" fill="{PAPER}"/>

  <!-- wall + window -->
  <rect x="0" y="0" width="{W}" height="372" fill="#EAE4DA"/>
  <rect x="96" y="26" width="470" height="306" rx="8" fill="#D7E3E1"/>
  <path d="M96 236 l84 -56 82 56 z" fill="{SAGE}" opacity=".9"/>
  <path d="M250 236 l66 -44 66 44 z" fill="{SAGE_D}" opacity=".5"/>
  <path d="M356 236 l104 -64 106 64 z" fill="{SAGE}" opacity=".75"/>
  <rect x="96" y="234" width="470" height="98" fill="#C9D8D5"/>
  <rect x="96" y="26" width="470" height="306" fill="url(#toneFine)"/>
  <g opacity=".55">
    <path d="M126 34 L406 332 L486 332 L206 34 z" fill="{WHITE}"/>
    <path d="M262 30 L530 332 L566 332 L312 30 z" fill="{WHITE}" opacity=".7"/>
  </g>
  <g stroke="{INK}" stroke-width="7" fill="none" stroke-linejoin="round">
    <rect x="96" y="26" width="470" height="306" rx="8"/>
    <line x1="331" y1="26" x2="331" y2="332"/>
    <line x1="96" y1="179" x2="566" y2="179"/>
  </g>

  <!-- plant on the sill -->
  <g>
    <path d="M700 262 q-30 -60 -4 -100" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M700 264 q32 -56 74 -72" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M700 262 q6 -72 -44 -92" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="660" cy="166" rx="29" ry="13" transform="rotate(-34 660 166)" fill="{SAGE}" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="782" cy="186" rx="29" ry="13" transform="rotate(24 782 186)" fill="{SAGE}" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="690" cy="168" rx="25" ry="11" transform="rotate(-72 690 168)" fill="{SAGE_D}" stroke="{INK}" stroke-width="5"/>
    <path d="M664 264 h74 l-10 76 h-54 z" fill="{CLAY}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <rect x="658" y="254" width="86" height="20" rx="6" fill="{CLAY_D}" stroke="{INK}" stroke-width="6"/>
  </g>

  <!-- stack of books -->
  <g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
    <rect x="812" y="300" width="170" height="26" rx="5" fill="{BLUE}"/>
    <rect x="826" y="274" width="156" height="26" rx="5" fill="{PAPER}"/>
    <rect x="818" y="248" width="166" height="26" rx="5" fill="{CLAY_D}"/>
  </g>

  <!-- desk -->
  <rect x="0" y="340" width="{W}" height="24" fill="{CLAY_D}"/>
  <rect x="0" y="364" width="{W}" height="199" fill="{CLAY}"/>
  <rect x="0" y="364" width="{W}" height="199" fill="url(#hatch)"/>
  <line x1="0" y1="340" x2="{W}" y2="340" stroke="{INK}" stroke-width="7"/>

  <!-- open notebook on the desk -->
  <g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
    <path d="M74 452 l150 -30 150 30 -150 38 z" fill="{WHITE}"/>
    <line x1="224" y1="422" x2="224" y2="490"/>
  </g>
  <g stroke="{INK}" stroke-width="3.4" opacity=".42" stroke-linecap="round">
    <line x1="116" y1="452" x2="204" y2="438"/>
    <line x1="126" y1="466" x2="206" y2="453"/>
    <line x1="244" y1="438" x2="332" y2="452"/>
    <line x1="244" y1="453" x2="322" y2="466"/>
  </g>

  <!-- pencil in hand -->
  <g transform="rotate(-24 398 466)">
    <rect x="322" y="456" width="140" height="17" rx="4" fill="#E8C979" stroke="{INK}" stroke-width="5"/>
    <path d="M322 456 l-26 8.5 26 8.5 z" fill="{SKIN}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
    <rect x="444" y="456" width="18" height="17" fill="{CLAY_D}" stroke="{INK}" stroke-width="5"/>
  </g>

  <!-- student, back view -->
  <g>
    <!-- shoulders -->
    <path d="M404 563 q10 -128 156 -128 q146 0 156 128 z"
          fill="{BLUE_D}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <!-- collar -->
    <path d="M506 442 q54 30 108 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
    <!-- neck -->
    <rect x="532" y="392" width="56" height="56" rx="16" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <!-- head: all hair, this is the back -->
    <path d="M560 268 q86 0 90 84 q4 46 -10 76 q-30 26 -80 26 q-50 0 -80 -26 q-14 -30 -10 -76 q4 -84 90 -84 z"
          fill="{HAIR}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <!-- hair highlight -->
    <path d="M512 314 q42 -28 96 -18" fill="none" stroke="{HAIR_HI}" stroke-width="9" stroke-linecap="round" opacity=".85"/>
    <!-- ears -->
    <ellipse cx="470" cy="372" rx="13" ry="20" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
    <ellipse cx="650" cy="372" rx="13" ry="20" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
    <!-- a couple of stray strands -->
    <path d="M486 330 q-10 40 6 64" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity=".8"/>
    <path d="M634 330 q10 40 -6 64" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity=".8"/>
  </g>

  {speed(40, 60, 130, count=5, gap=20, op=".2")}
  <rect width="{W}" height="{H}" fill="url(#focus)"/>
''', title="窗邊書桌前寫功課的學生背影")

open(os.path.join(OUT, "hero.svg"), "w", encoding="utf-8").write(hero)
print("hero.svg rewritten: %d bytes" % len(hero))
