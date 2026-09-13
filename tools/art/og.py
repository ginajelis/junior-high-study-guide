"""Build the social share cards (1200x630) that Facebook and friends show.

Facebook will not render SVG, so this emits SVGs which the build step
rasterises to PNG. Each card reuses that page's own drawing, so the link
preview looks like the page it opens.

The canvas is square on purpose: QuickLook renders an SVG into a square
bitmap anchored at the top, and `sips` can only crop from the centre, so
each card is drawn in the middle band of a 1200x1200 field. Crop 630
from the centre afterwards and you get exactly the card back.
"""

import base64
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "..", "..", "docs", "assets", "art")
OUT = os.path.join(HERE, "..", "..", "build", "og")

CANVAS = 1200
CARD_H = 630
TOP = (CANVAS - CARD_H) // 2          # 285

INK = "#37322C"
SHELL = "#EDEAE4"
CARD = "#FBF9F6"
CLAY_D = "#8C6450"
TEXT = "#5C564F"
MUTED = "#8A837A"
BORDER = "#C6BEB2"

SERIF = "Noto Serif TC, Songti TC, PingFang TC, serif"
SANS = "PingFang TC, Noto Sans TC, Helvetica, sans-serif"

# name, drawing, eyebrow, title lines, subtitle lines, footnote
CARDS = [
    ("share", "hero", "國一學習節奏指南",
     ["升國中，改變的", "不只是難度，", "還要跟上消化的速度"],
     ["真正缺的往往不只是讀書時間，", "而是當天消化的機制。"],
     "9 篇 · 作息安排 · 債務型與累積型 · 一句話筆記"),

    ("01-rhythm", "01-rhythm", "作息安排 · 第 01 篇",
     ["週間作息安排"],
     ["作業量每天不一樣，固定時段的計畫表", "第一天就會破功。改成固定順序，", "再設一個不能談判的熄燈時間。"],
     "國一學習節奏指南"),

    ("02-homework", "02-homework", "作息安排 · 第 02 篇",
     ["作業就是複習"],
     ["不是「作業」和「複習」兩件事。", "作業本身已經包含複習，", "只差一個確認自己懂不懂的小動作。"],
     "國一學習節奏指南"),

    ("03-stuck", "03-stuck", "讀書方法 · 第 03 篇",
     ["作業很多", "又不會寫"],
     ["開工前先把作業分成三堆，", "並給補觀念一個三十分鐘的硬上限。"],
     "國一學習節奏指南"),

    ("04-types", "04-types", "讀書方法 · 第 04 篇",
     ["債務型與累積型"],
     ["問一句「這科今天不懂，", "會不會害到下個月？」", "兩者的處理方式完全不同。"],
     "國一學習節奏指南"),

    ("05-onesentence", "05-onesentence", "讀書方法 · 第 05 篇",
     ["一句話筆記"],
     ["這不是在做筆記，是在檢查", "「我剛剛有沒有真的在聽」。", "寫不出來的那一節就是今天的洞。"],
     "國一學習節奏指南"),

    ("06-quiz", "06-quiz", "應試技巧 · 第 06 篇",
     ["頻繁小考的技巧"],
     ["小考的本質是記憶的即時提取，", "策略跟段考完全不同。"],
     "國一學習節奏指南"),

    ("07-resources", "07-resources", "讀書方法 · 第 07 篇",
     ["資源清單"],
     ["用法比選擇更重要：當天卡住、", "當天晚上看十分鐘那一個觀念就好。"],
     "國一學習節奏指南"),

    ("08-signals", "08-signals", "給家長 · 第 08 篇",
     ["給家長：", "訊號判讀"],
     ["什麼時候該調整方法，", "什麼時候該求助。"],
     "國一學習節奏指南"),

    ("09-quest", "09-quest", "自我判讀 · 第 09 篇",
     ["給國一生的", "自我判讀"],
     ["七道關卡，就是一個晚上會遇到的", "七個決定。這一篇不用讀，用玩的。"],
     "國一學習節奏指南"),
]


def inner(name):
    """Return that page's artwork ready to nest inside the card.

    Six chapters use generated raster art and four still use drawn SVG,
    so each comes in differently: a photo is embedded as a base64 <image>
    (QuickLook will not follow an external href when it rasterises), an
    SVG just has its outer wrapper stripped.
    """
    jpg = os.path.join(ART, name + ".jpg")
    if os.path.exists(jpg):
        b64 = base64.b64encode(open(jpg, "rb").read()).decode("ascii")
        return ('<image x="0" y="0" width="1000" height="563" '
                'preserveAspectRatio="xMidYMid slice" '
                'href="data:image/jpeg;base64,%s"/>' % b64)
    s = open(os.path.join(ART, name + ".svg"), encoding="utf-8").read()
    s = re.sub(r"^.*?<svg[^>]*>", "", s, flags=re.S)
    return re.sub(r"</svg>\s*$", "", s)


def build(name, drawing, eyebrow, title, subtitle, foot):
    art = inner(drawing)
    size = 54 if len(title) > 1 or len(title[0]) <= 8 else 50
    t_start = 256 if len(title) >= 3 else (296 if len(title) == 2 else 320)
    s_start = t_start + 76 * len(title) + 24

    title_svg = "\n      ".join(
        f'<text x="72" y="{t_start + 76 * i}">{line}</text>'
        for i, line in enumerate(title))
    sub_svg = "\n      ".join(
        f'<text x="72" y="{s_start + 38 * i}">{line}</text>'
        for i, line in enumerate(subtitle))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS}" height="{CANVAS}"
     viewBox="0 0 {CANVAS} {CANVAS}">
  <rect width="{CANVAS}" height="{CANVAS}" fill="{SHELL}"/>

  <g transform="translate(0,{TOP})">
    <rect width="{CANVAS}" height="{CARD_H}" fill="{SHELL}"/>
    <rect x="0" y="0" width="700" height="{CARD_H}" fill="{CARD}"/>
    <rect x="700" y="0" width="3" height="{CARD_H}" fill="{BORDER}"/>

    <g font-family="{SANS}">
      <text x="72" y="118" font-size="26" fill="{CLAY_D}" font-weight="600"
            letter-spacing="4">{eyebrow}</text>
      <line x1="72" y1="150" x2="156" y2="150" stroke="{CLAY_D}" stroke-width="5"
            stroke-linecap="round"/>
    </g>

    <g font-family="{SERIF}" font-weight="700" fill="{INK}" font-size="{size}">
      {title_svg}
    </g>

    <g font-family="{SANS}" font-size="25" fill="{TEXT}">
      {sub_svg}
    </g>

    <g font-family="{SANS}" font-size="21" fill="{MUTED}">
      <text x="72" y="578">{foot}</text>
    </g>

    <g transform="translate(742,175)">
      <rect x="-6" y="-6" width="424" height="250" rx="14" fill="{BORDER}"/>
      <svg x="0" y="0" width="412" height="238" viewBox="0 0 1000 563"
           preserveAspectRatio="xMidYMid slice">
{art}
      </svg>
    </g>
  </g>
</svg>
'''


os.makedirs(OUT, exist_ok=True)
for name, drawing, eyebrow, title, subtitle, foot in CARDS:
    svg = build(name, drawing, eyebrow, title, subtitle, foot)
    open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(svg)
    print("  %-18s %6d bytes" % (name + ".svg", len(svg)))

print("\n%d share cards written to %s" % (len(CARDS), os.path.normpath(OUT)))
