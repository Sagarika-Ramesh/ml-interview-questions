"""SVG helpers for figures on the ML Interview Prep site.

Two figure styles (see CLAUDE.md):
  * Concept illustrations -> wrap output in <svg class="il" viewBox="..."> inside
    <figure class="diagram illus"><div class="diagram-inner">...</div><figcaption>...</figcaption></figure>
  * Graphs with axes/curves -> <svg class="g3"> inside <figure class="diagram graph">.

These functions only return SVG strings; build a figure, paste it into the page.
Example at the bottom (python3 tools/figure_helpers.py prints a demo SVG).
"""

# ---------- palette ----------
INK = "#22252e"; CREAM = "#f3ecdc"; CORAL = "#ff6b5e"; TEAL = "#4fb3a5"
TAN = "#c9a063"; AMBER = "#f0b43c"; BLUE = "#6ea8e6"; PURPLE = "#a78bfa"
SHADOW = "rgba(0,0,0,0.25)"
# 3Blue1Brown palette for graphs
B3_BLUE = "#58C4DD"; B3_YELLOW = "#F7D96F"; B3_RED = "#FC6255"; B3_GREEN = "#83C167"; B3_GREY = "#9a9a9a"


# ---------- concept-illustration pieces (svg.il) ----------
def card(x, y, w, h, fill=CREAM):
    """Cream card with ink outline and drop shadow."""
    return (f'<rect x="{x}" y="{y+4}" width="{w}" height="{h}" rx="12" fill="{SHADOW}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="3"/>')


def text_lines(cx, y, lines, size=13, step=20):
    """Centred mono text lines (ink colour), e.g. inside a card."""
    return "".join(f'<text x="{cx}" y="{y+i*step}" text-anchor="middle" font-size="{size}">{t}</text>'
                   for i, t in enumerate(lines))


def big_label(cx, y, text):
    """Bold display text, e.g. the title inside a card ('an outlier!')."""
    return f'<text class="val" x="{cx}" y="{y}" text-anchor="middle">{text}</text>'


def tag(cx, y, text, color, txt="#fff"):
    """Coloured label chip centred at cx (e.g. 'DATA ERROR' coral, 'it's real' teal)."""
    w = len(text) * 7.6 + 22; x = cx - w / 2
    return (f'<rect x="{x}" y="{y+3}" width="{w}" height="26" rx="6" fill="{SHADOW}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="6" fill="{color}"/>'
            f'<text class="tag-t" x="{cx}" y="{y+17.5}" text-anchor="middle" style="fill:{txt}">{text}</text>')


def tag_left(x, y, text, color, txt="#fff"):
    w = len(text) * 7.6 + 22
    return tag(x + w / 2, y, text, color, txt)


def chip(x, y, text, anchor="start"):
    """Dark ink chip with cream mono text (item labels)."""
    w = len(text) * 7.25 + 20
    if anchor == "middle":
        x = x - w / 2
    return (f'<rect x="{x}" y="{y+3}" width="{w}" height="24" rx="6" fill="{SHADOW}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="6" fill="{INK}"/>'
            f'<text class="chip-t" x="{x+w/2}" y="{y+16}" text-anchor="middle">{text}</text>')


def rope(x1, y1, x2, y2, knot=True):
    """Tan connector with ink outline; optional knot at the end."""
    k = f'<circle cx="{x2}" cy="{y2}" r="5.5" fill="{TAN}" stroke="{INK}" stroke-width="2.5"/>' if knot else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{TAN}" stroke-width="4.5" stroke-linecap="round"/>{k}')


def group(x, y, w, h):
    """Dashed rounded group box."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="rgba(255,255,255,0.05)" '
            f'stroke="rgba(241,243,248,0.6)" stroke-width="2.5" stroke-dasharray="10 8"/>')


def action(x, y, w, text, color):
    """Dark box with coloured outline for an outcome ('→ fix it or remove it')."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="8" fill="{INK}" stroke="{color}" stroke-width="2.5"/>'
            f'<text class="act-t" x="{x+w/2}" y="{y+21}" text-anchor="middle">{text}</text>')


def question_node(cx, y, w, text):
    """Decision-chart question card."""
    return card(cx - w / 2, y, w, 46) + f'<text x="{cx}" y="{y+29}" text-anchor="middle" font-size="13.5" font-weight="600">{text}</text>'


def leaf(cx, y, text, dot=TEAL):
    """Decision-chart answer chip with a status dot."""
    w = len(text) * 7.6 + 40; x = cx - w / 2
    return (f'<rect x="{x}" y="{y+4}" width="{w}" height="34" rx="9" fill="{SHADOW}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="9" fill="{INK}"/>'
            f'<circle cx="{x+16}" cy="{y+17}" r="5.5" fill="{dot}"/>'
            f'<text class="chip-t" x="{x+28}" y="{y+22}" style="font-size:13px">{text}</text>')


def edge(x1, y1, x2, y2, label=None, lx=None, ly=None, anchor="middle"):
    """Thin cream decision-chart edge with an optional label."""
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CREAM}" stroke-opacity="0.75" stroke-width="2.5" stroke-linecap="round"/>'
    if label:
        s += f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" font-size="12.5" style="fill:#f3ecdc">{label}</text>'
    return s


def mind_branch(cx, top, title, color, items, txt="#fff"):
    """Mind-map branch: coloured title tag over a cream card of three short items."""
    w, h = 196, 78
    return card(cx - w / 2, top, w, h) + text_lines(cx, top + 32, items, 12.5, 19) + tag(cx, top - 15, title, color, txt)


# ---------- 3Blue1Brown graph pieces (svg.g3) ----------
def g3_defs(marker_id):
    """Arrowhead marker; give each SVG on a page its own id (g3a1, g3a2, ...)."""
    return (f'<defs><marker id="{marker_id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d6d6d6"/></marker></defs>')


def g3_axes(marker_id, x0, y0, x1, y1, xlabel="x", ylabel="y"):
    """Arrowed axes from origin (x0, y0) to (x1, y1 = top). Labels are italic math."""
    return (f'<line class="ax" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" marker-end="url(#{marker_id})"/>'
            f'<line class="ax" x1="{x0}" y1="{y0+10}" x2="{x0}" y2="{y1}" marker-end="url(#{marker_id})"/>'
            f'<text class="m" x="{x1+6}" y="{y0+17}" font-size="20">{xlabel}</text>'
            f'<text class="m" x="{x0+12}" y="{y1+8}" font-size="20">{ylabel}</text>')


def g3_grid(x0, x1, y0, y1, step_x=60, step_y=50):
    return ("".join(f'<line class="grid" x1="{x}" y1="{y1}" x2="{x}" y2="{y0}"/>' for x in range(x0 + step_x, x1 + 1, step_x)) +
            "".join(f'<line class="grid" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/>' for y in range(y0 - step_y, y1 - 1, -step_y)))


def g3_curve(d, color):
    """A 4px curve from an SVG path string."""
    return f'<path class="curve" d="{d}" stroke="{color}"/>'


def g3_dots(points, color=B3_BLUE, r=6.5):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>' for x, y in points)


if __name__ == "__main__":
    demo = (f'<svg class="il" viewBox="0 0 740 404">'
            f'{rope(330,88,190,206)}{rope(410,88,550,206)}'
            f'{tag(255,134,"it&#39;s wrong",CORAL)}{tag(485,134,"it&#39;s real",TEAL,"#0f2b25")}'
            f'{card(270,22,200,66)}{big_label(370,64,"an outlier!")}'
            f'{group(20,210,332,180)}{group(388,210,332,180)}'
            f'{tag_left(40,197,"DATA ERROR",CORAL)}{tag_left(408,197,"REAL RARE EVENT",TEAL)}'
            f'</svg>')
    print(demo)
