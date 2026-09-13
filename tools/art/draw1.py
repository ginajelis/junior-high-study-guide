"""First three illustrations — hero, 01 rhythm, 02 homework."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style import (W, H, INK, PAPER, CLAY, CLAY_D, SAGE, SAGE_D, BLUE, BLUE_D,
                   SKIN, WHITE, defs, burst, speed, sweat, wrap)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "docs", "assets", "art")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    path = os.path.join(OUT, name)
    open(path, "w", encoding="utf-8").write(svg)
    print("  %-22s %6d bytes" % (name, len(svg)))


# ══ hero — a desk by the window, evening light, one kid at work ══
hero = wrap(f'''{defs(accent=CLAY)}
  <rect width="{W}" height="{H}" fill="{PAPER}"/>

  <!-- window wall -->
  <rect x="0" y="0" width="{W}" height="360" fill="#EAE4DA"/>
  <rect x="120" y="28" width="530" height="300" rx="8" fill="#DCE6E4"/>
  <rect x="120" y="28" width="530" height="300" rx="8" fill="url(#toneFine)"/>

  <!-- distant rooftops -->
  <path d="M120 250 l90 -58 90 58 z" fill="{SAGE}" opacity=".85"/>
  <path d="M300 250 l70 -44 70 44 z" fill="{SAGE_D}" opacity=".55"/>
  <path d="M440 250 l110 -66 100 66 z" fill="{SAGE}" opacity=".7"/>
  <rect x="120" y="248" width="530" height="80" fill="#CFDCD9"/>

  <!-- light rays -->
  <g opacity=".5">
    <path d="M150 40 L470 330 L560 330 L240 40 z" fill="{WHITE}" opacity=".55"/>
    <path d="M300 32 L600 330 L640 330 L350 32 z" fill="{WHITE}" opacity=".4"/>
  </g>

  <!-- window frame -->
  <g stroke="{INK}" stroke-width="7" fill="none" stroke-linejoin="round">
    <rect x="120" y="28" width="530" height="300" rx="8"/>
    <line x1="385" y1="28" x2="385" y2="328"/>
    <line x1="120" y1="178" x2="650" y2="178"/>
  </g>

  <!-- plant on the sill -->
  <g>
    <path d="M742 250 q-34 -62 -6 -104" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M742 254 q34 -58 78 -76" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M742 252 q6 -76 -46 -96" stroke="{SAGE_D}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="700" cy="150" rx="30" ry="14" transform="rotate(-32 700 150)" fill="{SAGE}" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="828" cy="172" rx="30" ry="14" transform="rotate(26 828 172)" fill="{SAGE}" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="730" cy="152" rx="26" ry="12" transform="rotate(-70 730 152)" fill="{SAGE_D}" stroke="{INK}" stroke-width="5"/>
    <path d="M706 252 h74 l-10 74 h-54 z" fill="{CLAY}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <rect x="700" y="242" width="86" height="20" rx="6" fill="{CLAY_D}" stroke="{INK}" stroke-width="6"/>
  </g>

  <!-- desk -->
  <rect x="0" y="360" width="{W}" height="26" fill="{CLAY_D}"/>
  <rect x="0" y="386" width="{W}" height="177" fill="{CLAY}"/>
  <rect x="0" y="386" width="{W}" height="177" fill="url(#hatch)"/>
  <line x1="0" y1="360" x2="{W}" y2="360" stroke="{INK}" stroke-width="7"/>
  <line x1="0" y1="386" x2="{W}" y2="386" stroke="{INK}" stroke-width="6" opacity=".6"/>

  <!-- stack of books -->
  <g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
    <rect x="640" y="318" width="230" height="26" rx="5" fill="{BLUE}"/>
    <rect x="656" y="292" width="214" height="26" rx="5" fill="{PAPER}"/>
    <rect x="646" y="266" width="228" height="26" rx="5" fill="{CLAY_D}"/>
  </g>

  <!-- open notebook -->
  <g stroke="{INK}" stroke-width="6" stroke-linejoin="round">
    <path d="M112 300 l176 -26 176 26 -176 34 z" fill="{WHITE}"/>
    <line x1="288" y1="274" x2="288" y2="334"/>
  </g>
  <g stroke="{INK}" stroke-width="3.4" opacity=".45" stroke-linecap="round">
    <line x1="160" y1="300" x2="262" y2="288"/>
    <line x1="168" y1="312" x2="266" y2="300"/>
    <line x1="312" y1="288" x2="414" y2="300"/>
    <line x1="312" y1="300" x2="404" y2="311"/>
  </g>

  <!-- pencil -->
  <g transform="rotate(-19 470 340)">
    <rect x="386" y="330" width="150" height="17" rx="4" fill="#E8C979" stroke="{INK}" stroke-width="5"/>
    <path d="M386 330 l-26 8.5 26 8.5 z" fill="{SKIN}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
    <rect x="518" y="330" width="18" height="17" fill="{CLAY_D}" stroke="{INK}" stroke-width="5"/>
  </g>

  <!-- student, seen from behind -->
  <g>
    <path d="M470 563 q6 -132 130 -132 q124 0 130 132 z" fill="{BLUE_D}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <circle cx="600" cy="404" r="66" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <path d="M536 398 q6 -74 64 -74 q58 0 64 74 q-22 -34 -64 -34 q-42 0 -64 34 z" fill="{INK}"/>
    <path d="M534 400 q-14 40 8 62 q-30 -16 -22 -62 z" fill="{INK}"/>
    <path d="M666 400 q14 40 -8 62 q30 -16 22 -62 z" fill="{INK}"/>
  </g>
  {speed(60, 70, 150, count=5, gap=20, op=".18")}
  <rect width="{W}" height="{H}" fill="url(#focus)"/>
''', title="窗邊書桌，學生在寫功課")
save("hero.svg", hero)


# ══ 01 — the alarm clock, ringing ══
c01 = wrap(f'''{defs(accent=CLAY)}
  <rect width="{W}" height="{H}" fill="#F3EAE1"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>
  {burst(500, 300, 190, 430, n=30, op=".22", width=7)}

  <!-- bells -->
  <g stroke="{INK}" stroke-width="8" stroke-linejoin="round">
    <path d="M352 150 a54 54 0 0 1 84 -42 l-52 66 z" fill="{CLAY_D}"/>
    <path d="M648 150 a54 54 0 0 0 -84 -42 l52 66 z" fill="{CLAY_D}"/>
    <line x1="440" y1="112" x2="560" y2="112" stroke-linecap="round"/>
  </g>

  <!-- body -->
  <circle cx="500" cy="316" r="172" fill="{CLAY}" stroke="{INK}" stroke-width="9"/>
  <circle cx="500" cy="316" r="140" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  <circle cx="500" cy="316" r="140" fill="url(#toneFine)"/>

  <!-- ticks -->
  <g stroke="{INK}" stroke-width="7" stroke-linecap="round">
    <line x1="500" y1="196" x2="500" y2="220"/>
    <line x1="500" y1="412" x2="500" y2="436"/>
    <line x1="380" y1="316" x2="404" y2="316"/>
    <line x1="596" y1="316" x2="620" y2="316"/>
  </g>
  <g stroke="{INK}" stroke-width="4.5" stroke-linecap="round" opacity=".55">
    <line x1="560" y1="212" x2="551" y2="232"/>
    <line x1="440" y1="212" x2="449" y2="232"/>
    <line x1="604" y1="256" x2="584" y2="265"/>
    <line x1="396" y1="256" x2="416" y2="265"/>
    <line x1="604" y1="376" x2="584" y2="367"/>
    <line x1="396" y1="376" x2="416" y2="367"/>
  </g>

  <!-- hands: just past five -->
  <g stroke="{INK}" stroke-linecap="round">
    <line x1="500" y1="316" x2="500" y2="228" stroke-width="11"/>
    <line x1="500" y1="316" x2="576" y2="358" stroke-width="11"/>
    <circle cx="500" cy="316" r="14" fill="{INK}" stroke="none"/>
  </g>

  <!-- feet -->
  <g stroke="{INK}" stroke-width="8" stroke-linecap="round">
    <line x1="392" y1="466" x2="360" y2="516"/>
    <line x1="608" y1="466" x2="640" y2="516"/>
  </g>

  {speed(70, 180, 180, count=6, gap=26, op=".22")}
  {speed(760, 180, 180, count=6, gap=26, op=".22")}
''', title="響個不停的鬧鐘")
save("01-rhythm.svg", c01)


# ══ 02 — the desk from above: open book, pencil, mug ══
c02 = wrap(f'''{defs(accent=SAGE)}
  <rect width="{W}" height="{H}" fill="#EFEAE0"/>
  <rect width="{W}" height="{H}" fill="url(#hatch)"/>

  <!-- open book -->
  <g stroke="{INK}" stroke-width="8" stroke-linejoin="round">
    <path d="M170 126 q160 -34 320 8 q160 -42 320 -8 l0 300 q-160 -34 -320 8 q-160 -42 -320 -8 z" fill="{WHITE}"/>
    <path d="M490 134 v300"/>
  </g>
  <g stroke="{INK}" stroke-width="4" opacity=".4" stroke-linecap="round">
    <line x1="222" y1="190" x2="440" y2="176"/>
    <line x1="222" y1="230" x2="440" y2="216"/>
    <line x1="222" y1="270" x2="392" y2="258"/>
    <line x1="222" y1="310" x2="440" y2="298"/>
    <line x1="540" y1="176" x2="758" y2="190"/>
    <line x1="540" y1="216" x2="758" y2="230"/>
    <line x1="540" y1="258" x2="712" y2="270"/>
  </g>
  <!-- a line just written, underlined -->
  <g>
    <line x1="540" y1="300" x2="700" y2="312" stroke="{SAGE_D}" stroke-width="9" stroke-linecap="round"/>
    <line x1="540" y1="322" x2="686" y2="333" stroke="{SAGE_D}" stroke-width="5" stroke-linecap="round" opacity=".6"/>
  </g>

  <!-- pencil, mid-stroke -->
  <g transform="rotate(28 720 330)">
    <rect x="628" y="320" width="190" height="20" rx="5" fill="#E8C979" stroke="{INK}" stroke-width="6"/>
    <path d="M628 320 l-32 10 32 10 z" fill="{SKIN}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <rect x="800" y="320" width="22" height="20" fill="{CLAY_D}" stroke="{INK}" stroke-width="6"/>
  </g>
  {burst(704, 318, 40, 96, n=12, color=SAGE_D, op=".55", width=6)}

  <!-- mug -->
  <g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
    <rect x="76" y="360" width="132" height="120" rx="14" fill="{SAGE}"/>
    <path d="M208 388 q46 0 46 32 q0 32 -46 32" fill="none"/>
    <ellipse cx="142" cy="360" rx="66" ry="18" fill="{PAPER}"/>
  </g>
  <g stroke="{INK}" stroke-width="5" fill="none" opacity=".45" stroke-linecap="round">
    <path d="M116 336 q14 -22 0 -44"/>
    <path d="M158 336 q14 -22 0 -44"/>
  </g>
''', title="攤開的筆記本、鉛筆和馬克杯")
save("02-homework.svg", c02)

print("\nwrote 3 illustrations")
