"""Illustrations 03–09."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style import (W, H, INK, PAPER, CLAY, CLAY_D, SAGE, SAGE_D, BLUE, BLUE_D,
                   MAUVE, MAUVE_D, GOLD, GOLD_D, SKIN, WHITE,
                   defs, burst, speed, sweat, wrap)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "docs", "assets", "art")
HAIR = "#3E3630"
HAIR_HI = "#5E524A"


def save(name, svg):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(svg)
    print("  %-22s %6d bytes" % (name, len(svg)))


# ══ 03 — buried under the pile ══════════════════════════════
save("03-stuck.svg", wrap(f'''{defs(accent=BLUE)}
  <rect width="{W}" height="{H}" fill="#EDEAE3"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>
  {speed(60, 90, 150, count=6, gap=22, op=".2")}
  {speed(800, 90, 150, count=6, gap=22, op=".2")}

  <!-- leaning stack -->
  <g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
    <rect x="330" y="452" width="330" height="46" rx="6" fill="{CLAY_D}"/>
    <rect x="346" y="406" width="300" height="46" rx="6" fill="{PAPER}" transform="rotate(-2 496 429)"/>
    <rect x="336" y="360" width="318" height="46" rx="6" fill="{BLUE}" transform="rotate(2.5 495 383)"/>
    <rect x="356" y="314" width="286" height="46" rx="6" fill="{SAGE}" transform="rotate(-3.5 499 337)"/>
    <rect x="344" y="268" width="300" height="46" rx="6" fill="{CLAY}" transform="rotate(4.5 494 291)"/>
    <rect x="372" y="222" width="254" height="46" rx="6" fill="{PAPER}" transform="rotate(-5.5 499 245)"/>
  </g>

  <!-- loose sheets flying off -->
  <g stroke="{INK}" stroke-width="6" stroke-linejoin="round" fill="{WHITE}">
    <path d="M662 206 l86 -34 26 60 -86 34 z" transform="rotate(14 704 226)"/>
    <path d="M226 250 l86 34 -26 60 -86 -34 z" transform="rotate(-10 268 292)"/>
  </g>

  <!-- wobble marks -->
  <g stroke="{INK}" stroke-width="6" stroke-linecap="round" opacity=".5">
    <path d="M300 210 q-16 -18 -6 -38" fill="none"/>
    <path d="M700 186 q16 -18 6 -38" fill="none"/>
  </g>

  <!-- kid peering out from behind -->
  <g>
    <path d="M676 563 q6 -96 108 -96 q102 0 108 96 z" fill="{SAGE_D}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <circle cx="784" cy="412" r="62" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <path d="M784 350 q64 0 62 66 q-16 -30 -62 -30 q-46 0 -62 30 q-2 -66 62 -66 z" fill="{HAIR}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <!-- worried eyes -->
    <path d="M756 412 q10 -12 20 0" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
    <path d="M792 412 q10 -12 20 0" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
    <path d="M772 444 q12 -10 24 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  </g>
  {sweat(836, 356, .95)}
  {sweat(714, 372, .7)}
''', title="快倒下來的書堆，和躲在後面冒冷汗的學生"))


# ══ 04 — debt stacks, accumulation scatters ═════════════════
save("04-types.svg", wrap(f'''{defs(accent=CLAY)}
  <rect width="{W}" height="{H}" fill="#F0EBE3"/>

  <!-- left half: debt -->
  <rect x="0" y="0" width="500" height="{H}" fill="#F3E7DF"/>
  <rect x="0" y="0" width="500" height="{H}" fill="url(#toneFine)"/>
  <g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
    <rect x="118" y="430" width="270" height="62" rx="8" fill="{CLAY}"/>
    <rect x="148" y="368" width="210" height="62" rx="8" fill="{CLAY}"/>
    <rect x="178" y="306" width="150" height="62" rx="8" fill="{CLAY_D}"/>
    <rect x="206" y="244" width="94" height="62" rx="8" fill="{CLAY_D}"/>
  </g>
  <!-- the crack at the bottom -->
  <path d="M196 492 l22 -34 -18 -6 26 -22" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <g stroke="{INK}" stroke-width="6" stroke-linecap="round" opacity=".55">
    <path d="M100 402 q-22 -16 -14 -40" fill="none"/>
    <path d="M406 402 q22 -16 14 -40" fill="none"/>
  </g>
  {burst(253, 244, 66, 118, n=12, color=CLAY_D, op=".5", width=6)}

  <!-- divider -->
  <line x1="500" y1="0" x2="500" y2="{H}" stroke="{INK}" stroke-width="9"/>

  <!-- right half: accumulation -->
  <rect x="500" y="0" width="500" height="{H}" fill="#E6EBEF"/>
  <rect x="500" y="0" width="500" height="{H}" fill="url(#toneFine)"/>
  <g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
    <rect x="556" y="404" width="112" height="74" rx="10" fill="{BLUE}"/>
    <rect x="704" y="428" width="112" height="74" rx="10" fill="{BLUE}" transform="rotate(-7 760 465)"/>
    <rect x="848" y="386" width="112" height="74" rx="10" fill="{BLUE_D}" transform="rotate(9 904 423)"/>
    <rect x="614" y="256" width="112" height="74" rx="10" fill="{BLUE_D}" transform="rotate(-12 670 293)" opacity=".78"/>
    <rect x="792" y="222" width="112" height="74" rx="10" fill="{BLUE}" transform="rotate(7 848 259)" opacity=".5"/>
    <rect x="676" y="126" width="112" height="74" rx="10" fill="{BLUE}" transform="rotate(-4 732 163)" opacity=".26"/>
  </g>
  <!-- drifting-away marks -->
  <g stroke="{BLUE_D}" stroke-width="6" stroke-linecap="round" opacity=".55">
    <line x1="628" y1="104" x2="600" y2="72"/>
    <line x1="744" y1="100" x2="768" y2="66"/>
    <line x1="686" y1="92" x2="686" y2="56"/>
  </g>
''', title="左邊堆疊的方塊，右邊逐漸飄散的方塊"))


# ══ 05 — one sentence in a speech bubble ════════════════════
save("05-onesentence.svg", wrap(f'''{defs(accent=SAGE)}
  <rect width="{W}" height="{H}" fill="#EDEFE9"/>
  <rect width="{W}" height="{H}" fill="url(#hatch)"/>
  {burst(500, 250, 210, 330, n=22, color=SAGE_D, op=".22", width=6)}

  <!-- bubble -->
  <path d="M190 78 h620 a34 34 0 0 1 34 34 v250 a34 34 0 0 1 -34 34 h-360 l-108 84 14 -84 h-166 a34 34 0 0 1 -34 -34 v-250 a34 34 0 0 1 34 -34 z"
        fill="{WHITE}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>

  <!-- the one written line -->
  <g stroke-linecap="round">
    <line x1="256" y1="184" x2="700" y2="184" stroke="{INK}" stroke-width="14"/>
    <line x1="256" y1="216" x2="614" y2="216" stroke="{SAGE_D}" stroke-width="9"/>
    <line x1="256" y1="262" x2="700" y2="262" stroke="{SAGE_D}" stroke-width="5" opacity=".5"/>
  </g>
  <!-- the blanks you could not fill -->
  <g stroke="{INK}" stroke-width="7" stroke-linecap="round" opacity=".38">
    <line x1="256" y1="308" x2="330" y2="308"/>
    <line x1="360" y1="308" x2="434" y2="308"/>
    <line x1="464" y1="308" x2="538" y2="308"/>
  </g>

  <!-- pencil -->
  <g transform="rotate(-32 780 440)">
    <rect x="672" y="430" width="176" height="20" rx="5" fill="#E8C979" stroke="{INK}" stroke-width="6"/>
    <path d="M672 430 l-30 10 30 10 z" fill="{SKIN}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <rect x="830" y="430" width="20" height="20" fill="{CLAY_D}" stroke="{INK}" stroke-width="6"/>
  </g>

  <!-- sticky note -->
  <g transform="rotate(-8 138 448)">
    <rect x="62" y="382" width="152" height="132" rx="4" fill="#E9DE9A" stroke="{INK}" stroke-width="7"/>
    <g stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity=".45">
      <line x1="90" y1="424" x2="186" y2="424"/>
      <line x1="90" y1="456" x2="166" y2="456"/>
    </g>
  </g>
''', title="對話框裡只寫著一句話，旁邊有鉛筆和便利貼"))


# ══ 06 — answer sheet against the clock ═════════════════════
save("06-quiz.svg", wrap(f'''{defs(accent=BLUE)}
  <rect width="{W}" height="{H}" fill="#E9ECF0"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>
  {speed(40, 70, 190, count=7, gap=24, op=".22")}
  {speed(770, 330, 190, count=6, gap=24, op=".22")}

  <!-- answer sheet -->
  <g transform="rotate(-5 470 300)">
    <rect x="212" y="96" width="516" height="410" rx="10" fill="{WHITE}" stroke="{INK}" stroke-width="9"/>
    <line x1="212" y1="164" x2="728" y2="164" stroke="{INK}" stroke-width="6"/>
    <g stroke="{INK}" stroke-width="5" fill="none">''' + "".join(
        f'<circle cx="{292 + c * 62}" cy="{216 + r * 58}" r="19"/>'
        for r in range(5) for c in range(6)
    ) + f'''</g>
    <g fill="{BLUE_D}">
      <circle cx="354" cy="216" r="19"/>
      <circle cx="478" cy="274" r="19"/>
      <circle cx="292" cy="332" r="19"/>
      <circle cx="602" cy="390" r="19"/>
    </g>
    <g stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity=".4">
      <line x1="252" y1="132" x2="392" y2="132"/>
      <line x1="560" y1="132" x2="688" y2="132"/>
    </g>
  </g>

  <!-- pencil, poised -->
  <g transform="rotate(38 700 250)">
    <rect x="600" y="240" width="200" height="22" rx="5" fill="#E8C979" stroke="{INK}" stroke-width="7"/>
    <path d="M600 240 l-34 11 34 11 z" fill="{SKIN}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <rect x="782" y="240" width="22" height="22" fill="{CLAY_D}" stroke="{INK}" stroke-width="7"/>
  </g>

  <!-- stopwatch -->
  <g>
    <circle cx="826" cy="150" r="86" fill="{PAPER}" stroke="{INK}" stroke-width="9"/>
    <rect x="806" y="48" width="40" height="24" rx="7" fill="{BLUE_D}" stroke="{INK}" stroke-width="7"/>
    <g stroke="{INK}" stroke-width="9" stroke-linecap="round">
      <line x1="826" y1="150" x2="826" y2="96"/>
      <line x1="826" y1="150" x2="866" y2="176"/>
    </g>
    <circle cx="826" cy="150" r="10" fill="{INK}"/>
  </g>
  {burst(826, 150, 100, 152, n=14, color=BLUE_D, op=".4", width=6)}
''', title="電腦閱卷答案卡、鉛筆和碼錶"))


# ══ 07 — one concept, ten minutes ═══════════════════════════
save("07-resources.svg", wrap(f'''{defs(accent=GOLD)}
  <rect width="{W}" height="{H}" fill="#EFEBE0"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>

  <!-- tablet -->
  <g>
    <rect x="196" y="96" width="420" height="380" rx="26" fill="{INK}"/>
    <rect x="214" y="116" width="384" height="316" rx="10" fill="#D9DFE3" stroke="{INK}" stroke-width="6"/>
    <rect x="214" y="116" width="384" height="316" rx="10" fill="url(#toneFine)"/>
    <circle cx="406" cy="454" r="12" fill="#6E665E"/>
    <!-- play button -->
    <circle cx="406" cy="274" r="80" fill="{WHITE}" stroke="{INK}" stroke-width="8"/>
    <path d="M384 236 l64 38 -64 38 z" fill="{INK}"/>
    <!-- progress bar: a short clip -->
    <rect x="256" y="394" width="300" height="14" rx="7" fill="{WHITE}" stroke="{INK}" stroke-width="5"/>
    <rect x="259" y="397" width="86" height="8" rx="4" fill="{GOLD_D}"/>
  </g>

  <!-- the idea popping out -->
  <g>
    <path d="M770 118 a86 86 0 0 1 86 86 q0 44 -34 70 v34 h-104 v-34 q-34 -26 -34 -70 a86 86 0 0 1 86 -86 z"
          fill="#EFDFA6" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>
    <rect x="722" y="322" width="96" height="20" rx="8" fill="{GOLD_D}" stroke="{INK}" stroke-width="7"/>
    <rect x="736" y="352" width="68" height="18" rx="8" fill="{GOLD_D}" stroke="{INK}" stroke-width="7"/>
    <g stroke="{INK}" stroke-width="6" stroke-linecap="round" opacity=".6">
      <path d="M746 198 q24 -30 48 0" fill="none"/>
      <line x1="770" y1="204" x2="770" y2="266"/>
    </g>
  </g>
  {burst(770, 210, 116, 176, n=16, color=GOLD_D, op=".45", width=7)}

  <!-- 10 minute sand timer -->
  <g transform="translate(96,340)">
    <path d="M0 0 h104 l-38 60 38 60 h-104 l38 -60 z" fill="{PAPER}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
    <path d="M8 4 h88 l-32 52 z" fill="{GOLD}"/>
    <path d="M40 104 h24 l28 12 h-80 z" fill="{GOLD}"/>
    <rect x="-12" y="-16" width="128" height="18" rx="6" fill="{CLAY_D}" stroke="{INK}" stroke-width="7"/>
    <rect x="-12" y="118" width="128" height="18" rx="6" fill="{CLAY_D}" stroke="{INK}" stroke-width="7"/>
  </g>
''', title="平板上的教學影片、亮起的燈泡和沙漏"))


# ══ 08 — two people, one table ══════════════════════════════
save("08-signals.svg", wrap(f'''{defs(accent=MAUVE)}
  <rect width="{W}" height="{H}" fill="#F0EAEC"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>

  <!-- speech bubbles -->
  <g>
    <path d="M108 58 h244 a26 26 0 0 1 26 26 v96 a26 26 0 0 1 -26 26 h-150 l-56 48 8 -48 h-46 a26 26 0 0 1 -26 -26 v-96 a26 26 0 0 1 26 -26 z"
          fill="{WHITE}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
    <g fill="{INK}" opacity=".55">
      <circle cx="176" cy="132" r="13"/><circle cx="230" cy="132" r="13"/><circle cx="284" cy="132" r="13"/>
    </g>
  </g>
  <g>
    <path d="M642 40 h250 a26 26 0 0 1 26 26 v104 a26 26 0 0 1 -26 26 h-60 l-52 46 6 -46 h-144 a26 26 0 0 1 -26 -26 v-104 a26 26 0 0 1 26 -26 z"
          fill="{WHITE}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
    <g stroke="{MAUVE_D}" stroke-width="12" stroke-linecap="round">
      <line x1="686" y1="98" x2="866" y2="98"/>
      <line x1="686" y1="140" x2="808" y2="140"/>
    </g>
  </g>

  <!-- table -->
  <rect x="0" y="440" width="{W}" height="22" fill="{CLAY_D}"/>
  <rect x="0" y="462" width="{W}" height="101" fill="{CLAY}"/>
  <rect x="0" y="462" width="{W}" height="101" fill="url(#hatch)"/>
  <line x1="0" y1="440" x2="{W}" y2="440" stroke="{INK}" stroke-width="7"/>

  <!-- kid, left, facing right -->
  <g>
    <path d="M136 440 q8 -104 118 -104 q110 0 118 104 z" fill="{SAGE_D}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <circle cx="254" cy="288" r="62" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <path d="M254 226 q66 0 62 68 q-18 -32 -62 -32 q-44 0 -62 32 q-4 -68 62 -68 z" fill="{HAIR}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <circle cx="286" cy="292" r="7" fill="{INK}"/>
    <circle cx="246" cy="292" r="7" fill="{INK}"/>
    <path d="M262 322 q14 8 28 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  </g>

  <!-- adult, right, facing left -->
  <g>
    <path d="M602 440 q8 -116 132 -116 q124 0 132 116 z" fill="{MAUVE_D}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <circle cx="734" cy="272" r="68" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <path d="M734 204 q74 0 68 76 q-4 -34 -30 -44 q-30 22 -76 12 q-10 16 -30 32 q-6 -76 68 -76 z" fill="{HAIR}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
    <circle cx="700" cy="278" r="7" fill="{INK}"/>
    <circle cx="744" cy="278" r="7" fill="{INK}"/>
    <path d="M704 312 q18 10 36 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  </g>

  <!-- mug between them -->
  <g stroke="{INK}" stroke-width="7" stroke-linejoin="round">
    <rect x="446" y="368" width="96" height="76" rx="10" fill="{SAGE}"/>
    <path d="M542 386 q34 0 34 22 q0 22 -34 22" fill="none"/>
    <ellipse cx="494" cy="368" rx="48" ry="13" fill="{PAPER}"/>
  </g>
''', title="大人和小孩隔著桌子說話"))


# ══ 09 — the seven-stage board ══════════════════════════════
nodes = [(118, 452), (244, 358), (382, 430), (510, 318), (640, 400), (768, 296), (892, 372)]
path_d = "M118 452 " + " ".join(
    f"Q {(nodes[i][0] + nodes[i+1][0]) / 2:.0f} {min(nodes[i][1], nodes[i+1][1]) - 54:.0f} "
    f"{nodes[i+1][0]} {nodes[i+1][1]}" for i in range(len(nodes) - 1))

dots = "\n  ".join(
    f'<circle cx="{x}" cy="{y}" r="36" fill="{GOLD if i < 3 else PAPER}" stroke="{INK}" stroke-width="8"/>'
    f'<text x="{x}" y="{y + 11}" font-family="ui-monospace,Menlo,monospace" font-size="30" '
    f'font-weight="700" text-anchor="middle" fill="{INK}">{i + 1}</text>'
    for i, (x, y) in enumerate(nodes))

save("09-quest.svg", wrap(f'''{defs(accent=GOLD)}
  <rect width="{W}" height="{H}" fill="#EFEADC"/>
  <rect width="{W}" height="{H}" fill="url(#toneFine)"/>
  {speed(40, 60, 130, count=4, gap=22, op=".18")}

  <!-- hills behind -->
  <path d="M0 470 q150 -96 300 0 q150 -104 320 0 q160 -96 380 0 v93 h-1000 z" fill="{SAGE}" opacity=".4"/>

  <!-- the route -->
  <path d="{path_d}" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round" opacity=".28"/>
  <path d="{path_d}" fill="none" stroke="{GOLD_D}" stroke-width="7" stroke-linecap="round"
        stroke-dasharray="4 22"/>

  {dots}

  <!-- marker on stage 3 -->
  <g transform="translate(382,318)">
    <path d="M0 44 q-42 -30 -42 -62 a42 42 0 0 1 84 0 q0 32 -42 62 z" fill="{CLAY_D}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
    <circle cx="0" cy="-20" r="17" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>
  </g>

  <!-- finish flag -->
  <g transform="translate(916,372)">
    <line x1="0" y1="-36" x2="0" y2="-142" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
    <path d="M0 -142 h84 l-20 28 20 28 h-84 z" fill="{CLAY_D}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
  </g>
  {burst(892, 372, 56, 106, n=14, color=GOLD_D, op=".45", width=6)}
''', title="七個關卡的闖關路線圖，終點插著旗子"))

print("\nwrote 7 illustrations")
