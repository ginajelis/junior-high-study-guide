"""Shared manga-style drawing system for the guide's illustrations.

Ink outlines, flat cel fills, screentone dots and speed lines — the
vocabulary of a black-and-white manga panel, tinted with the site's
Morandi palette so the art sits inside the existing design.
"""

W, H = 1000, 563

INK = "#37322C"
PAPER = "#F7F3EC"

CLAY, CLAY_D = "#C2A08A", "#8A6450"
SAGE, SAGE_D = "#A3B2A4", "#5F7263"
BLUE, BLUE_D = "#9DABBB", "#5C6D80"
MAUVE, MAUVE_D = "#BCA6B1", "#7C6270"
GOLD, GOLD_D = "#BCAC86", "#786A4B"
SKIN = "#EFD9C6"
WHITE = "#FFFFFF"


def defs(tone="#37322C", tone_op=".20", accent=CLAY):
    """Screentone + speed-line patterns, plus a soft vignette."""
    return f'''<defs>
  <pattern id="tone" width="14" height="14" patternUnits="userSpaceOnUse">
    <circle cx="4" cy="4" r="2.6" fill="{tone}" opacity="{tone_op}"/>
    <circle cx="11" cy="11" r="2.6" fill="{tone}" opacity="{tone_op}"/>
  </pattern>
  <pattern id="toneFine" width="9" height="9" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="1.5" fill="{tone}" opacity=".16"/>
    <circle cx="7.5" cy="7.5" r="1.5" fill="{tone}" opacity=".16"/>
  </pattern>
  <pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse"
           patternTransform="rotate(35)">
    <rect width="4" height="12" fill="{tone}" opacity=".13"/>
  </pattern>
  <radialGradient id="focus" cx="50%" cy="45%" r="62%">
    <stop offset="55%" stop-color="{accent}" stop-opacity="0"/>
    <stop offset="100%" stop-color="{accent}" stop-opacity=".38"/>
  </radialGradient>
  <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="0"/></clipPath>
</defs>'''


def burst(cx, cy, r_in, r_out, n=26, color=INK, op=".30", width=5):
    """Radial impact lines — the manga 'this matters' mark."""
    import math
    out = []
    for i in range(n):
        a = (360 / n) * i + 4
        rad = math.radians(a)
        x1, y1 = cx + r_in * math.cos(rad), cy + r_in * math.sin(rad)
        x2, y2 = cx + r_out * math.cos(rad), cy + r_out * math.sin(rad)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                   f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" opacity="{op}"/>')
    return "\n  ".join(out)


def speed(x, y, w, count=7, gap=17, color=INK, op=".26", width=5, skew=0):
    """Horizontal motion streaks."""
    out = []
    for i in range(count):
        yy = y + i * gap
        ww = w * (0.55 + 0.45 * ((i * 37) % 11) / 10.0)
        out.append(f'<line x1="{x + skew * i}" y1="{yy}" x2="{x + ww + skew * i}" y2="{yy}" '
                   f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" opacity="{op}"/>')
    return "\n  ".join(out)


def sweat(x, y, s=1.0, color="#8FB6C9"):
    """The manga sweat-drop."""
    return (f'<path d="M {x} {y} c {6*s} {9*s} {10*s} {14*s} {10*s} {20*s} '
            f'a {10*s} {10*s} 0 0 1 {-20*s} 0 c 0 {-6*s} {4*s} {-11*s} {10*s} {-20*s} z" '
            f'fill="{color}" stroke="{INK}" stroke-width="{3.2*s}" stroke-linejoin="round"/>')


def wrap(body, bg=PAPER, title=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">
{body}
</svg>
'''
