"""Draw the front page from original geometry and typeset copy."""
from functools import lru_cache
from math import cos, sin, pi
from pathlib import Path
from random import Random
import argparse

from PIL import Image, ImageDraw, ImageFont

SCALE = 2
PAGE = "#f5eedc"
INK = "#172720"
GREEN = "#24483d"
RUST = "#a33524"
GOLD = "#eeb668"
MINT = "#aed2ab"
FONT_DIR = Path("/usr/share/fonts/truetype")
image = Image.new("RGB", (1024 * SCALE, 1024 * SCALE), PAGE)
draw = ImageDraw.Draw(image)


def px(values):
    return tuple(round(value * SCALE) for value in values)


@lru_cache
def font(size, face):
    path = {
        "serif": "liberation/LiberationSerif-Bold.ttf",
        "italic": "liberation/LiberationSerif-Italic.ttf",
        "sans": "liberation/LiberationSans-Regular.ttf",
        "bold": "liberation/LiberationSans-Bold.ttf",
    }[face]
    return ImageFont.truetype(str(FONT_DIR / path), size * SCALE)


def text(x, y, value, size, face="sans", color=INK, align="l"):
    draw.text(px((x, y)), value, font=font(size, face), fill=color, anchor=align + "t")


def width(value, size, face):
    return draw.textlength(value, font=font(size, face)) / SCALE


def rect(box, color):
    draw.rectangle(px(box), fill=color)


def ellipse(box, color=None, outline=None, weight=1):
    draw.ellipse(px(box), fill=color, outline=outline, width=weight * SCALE)


def line(points, color, weight=1):
    draw.line([px(point) for point in points], fill=color, width=weight * SCALE, joint="curve")


def polygon(points, color):
    draw.polygon([px(point) for point in points], fill=color)


def arc(box, start, end, color, weight=1):
    draw.arc(px(box), start, end, fill=color, width=weight * SCALE)


def tracked(x, y, value, size, color=INK, spacing=2):
    for letter in value:
        text(x, y, letter, size, "bold", color)
        x += width(letter, size, "bold") + spacing


def hero():
    rect((34, 173, 990, 479), GREEN)
    # The fractured globe is a visual metaphor. Its contours are abstract.
    cx, cy = 760, 308
    for r in (117, 125):
        arc((cx-r, cy-r, cx+r, cy+r), 199, 342, "#648779")
    for i in range(37):
        angle = pi * (1.1 + i * 0.8 / 36)
        x, y = cx + 129 * cos(angle), cy + 129 * sin(angle)
        line([(x, y), (x + 4 * cos(angle), y + 4 * sin(angle))], "#93ad91")
    ellipse((653, 201, 867, 415), "#335b50", MINT, 2)
    for box in [(680, 201, 840, 415), (725, 201, 795, 415),
                (653, 254, 867, 362), (653, 284, 867, 332)]:
        ellipse(box, outline="#699384")
    polygon([(671, 255), (687, 229), (721, 218), (744, 222), (728, 239),
             (734, 250), (719, 271), (708, 274), (703, 292), (686, 278)], MINT)
    polygon([(705, 285), (730, 293), (749, 312), (736, 340), (727, 365),
             (712, 379), (705, 345), (693, 315)], "#8bb18f")
    polygon([(784, 225), (807, 219), (832, 232), (851, 254), (846, 269),
             (817, 262), (802, 274), (786, 268), (778, 251)], MINT)
    polygon([(779, 272), (807, 280), (817, 303), (804, 330), (786, 345),
             (775, 319), (764, 300)], "#8bb18f")
    polygon([(825, 326), (843, 318), (858, 332), (848, 349), (826, 345)], MINT)
    polygon([(766, 200), (744, 247), (766, 270), (743, 306), (764, 330),
             (748, 359), (762, 415), (771, 415), (761, 358), (780, 326),
             (756, 304), (781, 269), (756, 244), (775, 202)], GREEN)
    line([(773, 201), (751, 246), (774, 270), (750, 305), (773, 327),
          (755, 359), (767, 414)], GOLD, 2)

    # Two rows of delegates around a negotiation table.
    ellipse((550, 377, 967, 469), "#193832")
    ellipse((548, 368, 969, 453), "#bd694f")
    ellipse((555, 370, 962, 435), "#f0cb90", "#172720", 2)
    ellipse((576, 378, 941, 423), "#bd694f", "#895132")
    center = (758, 400)
    for angle in (195, 215, 237, 263, 285, 306, 327, 347):
        r = angle * pi / 180
        x, y = center[0] + 201 * cos(r), center[1] + 48 * sin(r)
        ellipse((x-11, y-4, x+11, y+13), INK)
        ellipse((x-6, y-12, x+6, y+1), GOLD, INK)
    for index in range(9):
        x = 594 + 41 * index
        y = 423 + 21 * sin(pi * index / 8)
        ellipse((x-17, y-6, x+17, y+21), INK, "#84a291")
        ellipse((x-9, y-16, x+9, y+3), ("#eab274", "#c58560", "#94583f")[index % 3])
        line([(x-8, y+13), (x+8, y+13)], "#49695a")

    tracked(56, 198, "ANTALYA  /  CLIMATE", 23, GOLD, 2)
    text(54, 237, "COP31 talks", 83, "serif", PAGE)
    text(54, 312, "end in deadlock", 71, "serif", PAGE)
    text(57, 407, "Fossil-fuel dispute blocks", 29, "sans", PAGE)
    text(57, 439, "the summit’s main agreement.", 29, "sans", PAGE)


def iran(x, y):
    rect((x, y, x+104, y+57), "#e7d3bb")
    for offset in (20, 72):
        apex = x + offset
        line([(apex-15, y+53), (apex, y+4), (apex+15, y+53)], GREEN, 2)
        for level, span in [(14, 13), (25, 18), (39, 10)]:
            line([(apex-span, y+level), (apex+span, y+level)], GREEN, 2)
        line([(apex-11, y+42), (apex+7, y+24), (apex-8, y+25),
              (apex+11, y+42)], GREEN)
    arc((x+19, y-3, x+75, y+32), 20, 160, GREEN, 2)
    polygon([(x+52, y+11), (x+42, y+33), (x+54, y+31),
             (x+48, y+51), (x+66, y+23), (x+54, y+25)], RUST)


def boat(x, y):
    rect((x, y, x+104, y+57), "#d1e0d8")
    for row in (38, 47, 54):
        for offset in (3, 34, 65):
            arc((x+offset, y+row-7, x+offset+34, y+row+5), 190, 345, "#507869", 2)
    polygon([(x+13,y+28), (x+93,y+28), (x+78,y+40), (x+29,y+40)], GREEN)
    polygon([(x+32,y+28), (x+42,y+13), (x+68,y+13), (x+79,y+28)], GREEN)
    rect((x+45, y+17, x+65, y+23), PAGE)
    line([(x+55,y+13), (x+55,y+5)], RUST, 2)


def bitcoin(x, y):
    rect((x, y, x+104, y+57), "#f1dab1")
    ellipse((x+6, y+1, x+60, y+55), GOLD, RUST, 2)
    ellipse((x+11, y+6, x+55, y+50), outline=RUST)
    text(x+33, y+13, "₿", 32, "bold", RUST, "m")
    line([(x+64,y+46), (x+96,y+14), (x+96,y+32)], GREEN, 3)
    line([(x+77,y+14), (x+96,y+14)], GREEN, 3)


def capitol(x, y):
    rect((x, y, x+104, y+57), "#dfe6d8")
    ellipse((x+36, y+10, x+70, y+39), GREEN)
    rect((x+50, y+5, x+55, y+13), GREEN)
    polygon([(x+10,y+36), (x+53,y+22), (x+94,y+36)], GREEN)
    for offset in range(16, 94, 10):
        rect((x+offset, y+37, x+offset+3, y+50), GREEN)
    rect((x+7, y+51, x+97, y+54), GREEN)


def orbit(x, y):
    rect((x, y, x+104, y+57), GREEN)
    ellipse((x+30, y+4, x+75, y+49), GOLD)
    for dx, dy, r in [(43,18,6),(58,32,7),(62,14,4),(42,35,5)]:
        ellipse((x+dx-r, y+dy-r, x+dx+r, y+dy+r), "#c48453")
    arc((x+8, y+12, x+97, y+50), 0, 174, PAGE, 2)
    arc((x+8, y+12, x+97, y+50), 207, 236, PAGE, 2)
    polygon([(x+89,y+13), (x+98,y+22), (x+89,y+31), (x+80,y+22)], PAGE)


def race(x, y):
    rect((x, y, x+104, y+57), "#ebd4c5")
    line([(x+11,y+50), (x+93,y+50)], RUST, 2)
    for dx in (27, 79):
        ellipse((x+dx-10,y+28,x+dx+10,y+48), INK)
        ellipse((x+dx-4,y+34,x+dx+4,y+42), PAGE)
    polygon([(x+24,y+32),(x+38,y+22),(x+54,y+28),(x+71,y+21),
             (x+87,y+25),(x+78,y+38),(x+52,y+39),(x+36,y+36)], RUST)
    line([(x+38,y+29),(x+51,y+17),(x+65,y+21),(x+72,y+28)], INK, 5)
    ellipse((x+63,y+7,x+77,y+20), INK)
    line([(x+5,y+19),(x+25,y+19)], RUST, 2)


def story(x, y, label, title, detail, art):
    line([(x, y), (x+297, y)], INK, 2)
    tracked(x, y+17, label[0], 19, RUST, 1)
    text(x, y+44, label[1], 19, "bold", INK)
    art(x+193, y+12)
    for index, row in enumerate(title):
        if width(row, 40, "serif") > 297:
            raise ValueError(f"Headline exceeds column width: {row}")
        text(x, y+79+index*39, row, 40, "serif")
    for index, row in enumerate(detail):
        if width(row, 22, "sans") > 297:
            raise ValueError(f"Caption exceeds column width: {row}")
        text(x, y+170+index*24, row, 22)


def render():
    rng = Random(22)
    for _ in range(9000):
        x, y = rng.randrange(1024), rng.randrange(1024)
        rect((x, y, x, y), rng.choice(("#ebe3cd", "#faf4e6", "#eee6d3")))

    line([(34, 27), (990, 27)], INK, 3)
    tracked(34, 39, "SUNDAY", 24, RUST, 3)
    text(990, 38, "22 NOVEMBER 2026", 26, "bold", INK, "r")
    size = 103
    masthead = "WORLD IN FOCUS"
    while width(masthead, size, "serif") > 956:
        size -= 1
    text(512, 69, masthead, size, "serif", INK, "m")
    line([(34, 158), (990, 158)], INK, 2)

    hero()
    story(34, 499, ("IRAN", "WAR & ENERGY"), ("Iran starts", "power cuts"),
          ("Fuel shortages squeeze", "a war-hit power grid."), iran)
    story(364, 499, ("NIGERIA", "BAYELSA"), ("Boat disaster", "toll rises to 29"),
          ("Tinubu pledges ₦250m", "for bereaved families."), boat)
    story(693, 499, ("MARKETS", "BITCOIN"), ("Bitcoin tops", "$60,000"),
          ("Coinbase, 18:00 UTC.", "U.S. equity futures rebound."), bitcoin)
    story(34, 728, ("U.S. HOUSE", "POLITICS"), ("Democrats win", "258+ seats"),
          ("Their largest House majority", "since 1992, per AP’s count."), capitol)
    story(364, 728, ("MERCURY", "SPACE SCIENCE"), ("BepiColombo", "enters orbit"),
          ("The ESA–JAXA spacecraft", "arrives on Nov. 22 in Japan."), orbit)
    story(693, 728, ("PORTUGAL", "MOTOGP"), ("Márquez takes", "eighth title"),
          ("Bezzecchi wins the race", "as Márquez seals the crown."), race)
    line([(346, 500), (346, 946)], "#beb5a0")
    line([(676, 500), (676, 946)], "#beb5a0")
    rect((34, 961, 990, 1004), GREEN)
    tracked(50, 973, "AI & TECH", 22, GOLD, 1)
    line([(182, 970), (182, 994)], "#729384")
    text(197, 968, "U.S. presses Nvidia on AI chip sales to China", 32, "serif", PAGE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", nargs="?", type=Path, default=Path("edition.png"))
    args = parser.parse_args()
    render()
    image.resize((1024, 1024), Image.Resampling.LANCZOS).save(
        args.destination, format="PNG", optimize=True
    )
