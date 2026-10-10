#!/usr/bin/env python3
"""
Builds a neofetch/fastfetch-style profile card as dark_mode.svg + light_mode.svg.

  python generate.py                  # ASCII art from art.txt (or the built-in flood/LoRa art)
  python generate.py --photo me.jpg   # convert your photo to art.txt first (needs: pip install pillow)
  python generate.py --fetch          # also add a live "GitHub Stats" block (optional: set GITHUB_TOKEN)

Edit the INFO list below -- that's the whole card.
"""
import argparse
import json
import math
import os
import random
import sys
import urllib.request
from xml.sax.saxutils import escape

USER = "netteyr14"

# ---------------------------------------------------------------- card content
# ("title", text)            -> bold header + dashes to the edge
# ("section", text)          -> section header + dashes
# ("kv", key, value)         -> "Key:  ......  value"  (value right-aligned)
# ("note", text)             -> dim comment line
# ("blank",)
INFO = [
    ("title", "arvin@netteyr14"),
    ("kv", "Name", "Isorena, Arvin Jay"),
    ("kv", "Alias", "netteyr14, sheeshkebab"),
    ("kv", "OS", "Arch Linux (Caelestia)"),
    ("kv", "Course/Year", "BS Information Technology, 4th Year"),
    ("kv", "Location", "Philippines (UTC +08:00)"),
    ("kv", "Focus", "IoT Systems, ML Forecasting, Full-Stack"),
    ("blank",),
    ("kv", "Languages.Programming", "Python, C++, C#, Java, JavaScript, Dart"),
    ("kv", "Languages.Frameworks", "Flutter, Flask"),
    ("kv", "ML.Libraries", "LightGBM"),
    ("kv", "Infra.Tools", "Docker, NGINX, MySQL, Cloudflare, Azure VM, Git"),
    ("kv", "Design.Tools", "Figma, Canva"),
    ("blank",),
    ("section", "Projects"),
    ("kv", "Currently.Shipping", "FloodWatch (under development)"),
    ("kv", "Pipeline.Edge", "LoRa32 Nodes → LoRa Gateway"),
    ("kv", "Pipeline.Cloud", "Docker API → LightGBM → MySQL"),
    ("kv", "Pipeline.Client", "Flutter: mobile, web, desktop"),
    ("kv", "Repo", "github.com/netteyr14/FloodWatch"),
    ("blank",),
    ("section", "Contact"),
    ("kv", "Email.Personal", "753951852456arvin@gmail.com"),
    ("kv", "Facebook", "Arvin Jay Isorena"),
    ("kv", "GitHub", "netteyr14"),
    ("note", "// Private repos (backend, mobile, admin)? Email me."),
]

# ---------------------------------------------------------------- layout grid
FONT_SIZE = 14
CW = 8.4          # width of one monospace cell (px)
LH = 18           # line height (px)
PAD = 26          # outer padding (px)
GAP_COLS = 4      # blank columns between art and info
INFO_COLS = 66    # width of the info column (cells)
ART_COLS, ART_ROWS = 50, 28
FONT = "'JetBrains Mono','Fira Code',Consolas,'DejaVu Sans Mono','Courier New',monospace"

THEMES = {
    "dark": dict(bg="#0d1117", border="#30363d", text="#c9d1d9", title="#f0f6fc",
                 key="#ffa657", val="#79c0ff", dim="#6e7681",
                 art_top="#a5d6ff", art_bot="#1f6feb", art_flat="#79c0ff"),
    "light": dict(bg="#ffffff", border="#d0d7de", text="#24292f", title="#0d1117",
                  key="#bc4c00", val="#0969da", dim="#8c959f",
                  art_top="#218bff", art_bot="#0a3069", art_flat="#0969da"),
}


# ---------------------------------------------------------------- ASCII art
def default_art(cols=ART_COLS, rows=ART_ROWS):
    """A LoRa tower beaming a signal over flood waves (fits FloodWatch)."""
    g = [[" "] * cols for _ in range(rows)]
    c = cols // 2
    water_top = rows - 11

    def put(r, x, ch):
        if 0 <= r < rows and 0 <= x < cols:
            g[r][x] = ch

    rnd = random.Random(14)
    for _ in range(26):  # stars
        put(rnd.randrange(0, water_top - 2), rnd.randrange(cols), rnd.choice(".." "+*"))

    beacon = 6
    for rr in (5, 9, 13, 17):  # signal arcs
        for sgn, ch_mid, ch_up, ch_dn in ((-1, "(", ".", "'"), (1, ")", ".", "'")):
            put(beacon, c + sgn * rr, ch_mid)
            put(beacon - 1, c + sgn * (rr - 1), ch_up)
            put(beacon + 1, c + sgn * (rr - 1), ch_dn)
            put(beacon - 2, c + sgn * (rr - 2), ch_up) if rr > 5 else None
            put(beacon + 2, c + sgn * (rr - 2), ch_dn) if rr > 5 else None
    put(beacon, c, "@")

    top, bottom = beacon + 1, water_top + 2  # mast + lattice legs
    for r in range(top, bottom + 1):
        hw = 1 + (r - top) * 6 / (bottom - top)
        hw = round(hw)
        put(r, c, "|")
        put(r, c - hw, "/")
        put(r, c + hw, "\\")
        if (r - top) % 3 == 2:
            for x in range(c - hw + 1, c + hw):
                if x != c:
                    put(r, x, "=")
        elif (r - top) % 3 == 0 and hw > 1:
            put(r, c - hw + 1, "\\")
            put(r, c + hw - 1, "/")

    for y in range(water_top, rows):  # waves (never overwrite the tower)
        depth = y - water_top
        for x in range(cols):
            if g[y][x] != " ":
                continue
            v = math.sin(x * 0.46 + y * 1.25) + 0.55 * math.sin(x * 0.19 - y * 0.8)
            t = 0.95 - 0.13 * depth
            if v > t + 1.0:
                ch = "#"
            elif v > t + 0.6:
                ch = "="
            elif v > t + 0.25:
                ch = "~"
            elif v > t:
                ch = "-"
            else:
                ch = " "
            g[y][x] = ch
    return ["".join(r).rstrip() for r in g]


def photo_to_art(path, cols=ART_COLS, rows=ART_ROWS, invert=False):
    from PIL import Image, ImageOps
    ramp = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    if invert:
        ramp = ramp[::-1]
    im = ImageOps.autocontrast(Image.open(path).convert("L"))
    w, h = im.size
    # fit inside cols x rows, remembering a cell is ~2x taller than wide
    scale = min(cols / w, rows * 2 / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale / 2))
    im = im.resize((nw, nh))
    lines = []
    for y in range(nh):
        row = "".join(ramp[im.getpixel((x, y)) * (len(ramp) - 1) // 255] for x in range(nw))
        lines.append((" " * ((cols - nw) // 2) + row).rstrip())
    return lines


# ---------------------------------------------------------------- GitHub stats
def fetch_stats(user):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-card"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    def get(url):
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
            return json.load(r)

    u = get(f"https://api.github.com/users/{user}")
    stars, page = 0, 1
    while True:
        repos = get(f"https://api.github.com/users/{user}/repos?per_page=100&page={page}")
        stars += sum(r["stargazers_count"] for r in repos if not r["fork"])
        if len(repos) < 100:
            break
        page += 1
    commits = get(f"https://api.github.com/search/commits?q=author:{user}&per_page=1")["total_count"]
    return [
        ("section", "GitHub Stats"),
        ("kv", "Repos", f"{u['public_repos']}"),
        ("kv", "Stars", f"{stars}"),
        ("kv", "Commits", f"{commits:,}"),
        ("kv", "Followers", f"{u['followers']}"),
    ]


# ---------------------------------------------------------------- SVG rendering
def lerp(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02x}" for i in range(3))


def text(x, y, s, fill, extra="", cw=CW, fs=None):
    """One monospace run, pinned to the cell grid so every font lines up."""
    if not s:
        return ""
    size = f' font-size="{fs:.2f}"' if fs else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" textLength="{len(s) * cw:.1f}" '
            f'lengthAdjust="spacing" xml:space="preserve" style="white-space:pre"{size} {extra}>'
            f'{escape(s)}</text>')


def normalize_art(lines):
    """Trim blank rows and the common left margin so the art fills its box."""
    lines = [l.rstrip() for l in lines]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    margin = min((len(l) - len(l.lstrip(" ")) for l in lines if l.strip()), default=0)
    return [l[margin:] for l in lines]


def render(art, info, th, flat=False):
    art = normalize_art(art)
    art_w = max((len(l) for l in art), default=1)
    k = min(1.0, ART_COLS / art_w)           # shrink wide art to fit its box
    acw, alh, afs = CW * k, LH * k, FONT_SIZE * k
    art_h, info_h = len(art) * alh, len(info) * LH
    body_h = max(art_h, info_h)
    art_x = PAD + (ART_COLS * CW - art_w * acw) / 2
    info_x = PAD + (ART_COLS + GAP_COLS) * CW
    info_right = info_x + INFO_COLS * CW
    width = round(info_right + PAD)
    height = round(PAD * 2 + body_h)
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="{FONT}" font-size="{FONT_SIZE}">',
        f'<rect width="{width}" height="{height}" rx="14" fill="{th["bg"]}" stroke="{th["border"]}"/>',
    ]

    art_y0 = PAD + (body_h - art_h) / 2
    for i, line in enumerate(art):
        stripped = line.lstrip(" ")
        if not stripped:
            continue
        lead = len(line) - len(stripped)
        y = art_y0 + (i + 1) * alh - 5 * k
        col = th["art_flat"] if flat else lerp(th["art_top"], th["art_bot"], i / max(1, len(art) - 1))
        out.append(text(art_x + lead * acw, y, stripped.rstrip(), col, cw=acw, fs=afs))

    info_y0 = PAD + (body_h - info_h) / 2
    for i, item in enumerate(info):
        y = info_y0 + (i + 1) * LH - 5
        kind = item[0]
        if kind in ("title", "section"):
            label = item[1]
            out.append(text(info_x, y, label, th["title"], 'font-weight="bold"'))
            dashes = INFO_COLS - len(label) - 1
            out.append(text(info_x + (len(label) + 1) * CW, y, "-" * dashes, th["dim"]))
        elif kind == "kv":
            key, val = item[1] + ":", item[2]
            room = INFO_COLS - len(key) - len(val)
            if room < 4:
                sys.exit(f"Line too long ({room} cells free, need >= 4): {item[1]} = {val}")
            out.append(text(info_x, y, key, th["key"]))
            leader = (". " * (room // 2))[: room - 2]
            out.append(text(info_x + (len(key) + 1) * CW, y, leader, th["dim"]))
            out.append(text(info_right - len(val) * CW, y, val, th["val"]))
        elif kind == "note":
            out.append(text(info_x, y, item[1], th["dim"], 'font-style="italic"'))
    out.append("</svg>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--photo", help="image to convert to ASCII art (saved to art.txt)")
    ap.add_argument("--invert", action="store_true", help="invert brightness for --photo")
    ap.add_argument("--fetch", action="store_true", help="add live GitHub stats")
    args = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    art_path = os.path.join(here, "art.txt")

    flat = True
    if args.photo:
        art = photo_to_art(args.photo, invert=args.invert)
        open(art_path, "w", encoding="utf-8").write("\n".join(art) + "\n")
        print(f"wrote {art_path}")
    elif os.path.exists(art_path):
        art = open(art_path, encoding="utf-8").read().splitlines()
    else:
        art, flat = default_art(), False

    info = list(INFO)
    if args.fetch:
        try:
            # insert before the Contact section
            idx = next(i for i, it in enumerate(info) if it[0] == "section" and it[1] == "Contact")
            info[idx:idx] = fetch_stats(USER) + [("blank",)]
        except Exception as e:  # rate limit, offline, ...
            print(f"! could not fetch stats ({e}); set GITHUB_TOKEN and retry", file=sys.stderr)

    for name, th in THEMES.items():
        path = os.path.join(here, f"{name}_mode.svg")
        open(path, "w", encoding="utf-8").write(render(art, info, th, flat))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()