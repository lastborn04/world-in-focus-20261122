"""Render the Run 2 broadsheet and both proofs from original drawings and checked data."""
import argparse
import json
from pathlib import Path
from random import Random
from functools import lru_cache
from math import cos, sin, pi

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
S = 2
PAPER = "#f5f0e4"
INK = "#172b31"
MUTED = "#485957"
RULE = "#b6b6a6"
WHITE = "#fff8e9"
GOLD = "#f0b764"
REGION = {
    "AMERICAS": "#923d38", "EUROPE": "#305986", "AFRICA": "#79532a",
    "MIDDLE EAST": "#466044", "ASIA–PACIFIC": "#813f67", "GLOBAL": "#276366",
}
im = Image.new("RGB", (1024*S, 1024*S), PAPER)
d = ImageDraw.Draw(im)


def points(values):
    return tuple(round(v*S) for v in values)


@lru_cache
def font(size, face):
    name = {"s": "LiberationSerif-Bold", "i": "LiberationSerif-Italic",
            "b": "LiberationSans-Bold", "r": "LiberationSans-Regular"}[face]
    return ImageFont.truetype(f"/usr/share/fonts/truetype/liberation/{name}.ttf", size*S)


def type_at(x, y, value, size, face="r", color=INK, anchor="l", limit=None):
    f = font(size, face)
    if limit and d.textlength(value, font=f) / S > limit:
        raise ValueError(f"Over width {limit}: {value}")
    d.text(points((x, y)), value, font=f, fill=color, anchor=anchor+"t")


def box(x0, y0, x1, y1, fill):
    d.rectangle(points((x0, y0, x1, y1)), fill=fill)


def stroke(path, color, weight=1):
    d.line([points(p) for p in path], fill=color, width=round(weight*S), joint="curve")


def poly(path, color):
    d.polygon([points(p) for p in path], fill=color)


def oval(bounds, fill=None, outline=None, weight=1):
    d.ellipse(points(bounds), fill=fill, outline=outline, width=round(weight*S))


def arc(bounds, first, last, color, weight=1):
    d.arc(points(bounds), first, last, fill=color, width=round(weight*S))


def rule(x, y, end, color=RULE, weight=1):
    stroke([(x, y), (end, y)], color, weight)


class Scene:
    """Give editorial drawings a 160 × 90 coordinate space at any placement."""

    def __init__(self, x, y, w, h, field, dark, light):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.dark, self.light = dark, light
        box(x, y, x+w, y+h, field)

    def coord(self, x, y):
        return self.x+x*self.w/160, self.y+y*self.h/90

    def shape(self, coordinates, color):
        poly([self.coord(x, y) for x, y in coordinates], color)

    def line(self, coordinates, color, width=1.5):
        stroke([self.coord(x, y) for x, y in coordinates], color, max(1, width*self.h/90))

    def ellipse(self, left, top, right, bottom, color, outline=None):
        oval((*self.coord(left, top), *self.coord(right, bottom)), color, outline)


def climate(s):
    # A negotiation table split by the missing fossil-fuel language.
    for n in range(8, 154, 8):
        s.line([(n, 8), (n, 81)], "#285556")
    for n in range(10, 90, 10):
        s.line([(4, n), (156, n)], "#285556")
    s.ellipse(19, 23, 141, 80, "#132f34")
    s.ellipse(23, 16, 137, 72, "#d9995a")
    s.ellipse(30, 22, 130, 66, "#ac6248")
    for angle in (0, 30, 60, 120, 150, 180, 210, 240, 300, 330):
        x = 80 + 61*cos(angle*pi/180)
        y = 43 + 27*sin(angle*pi/180)
        s.ellipse(x-5.8, y-4, x+5.8, y+7, "#162e32", "#8bb5a3")
        s.ellipse(x-3, y-9, x+3, y-2, "#f0bb87")
    s.shape([(77, 22), (88, 36), (74, 48), (84, 66), (72, 66),
             (65, 48), (78, 36), (69, 22)], "#163e42")
    for x in (46, 99):
        s.shape([(x, 34), (x+13, 32), (x+16, 45), (x+3, 47)], "#fae3b7")
        s.line([(x+4, 38), (x+12, 37)], "#875345")
        s.line([(x+5, 42), (x+13, 41)], "#875345")


def dymer(s):
    s.shape([(4, 78), (16, 73), (48, 77), (67, 70), (87, 75), (115, 66),
             (138, 74), (155, 73), (160, 90), (0, 90)], "#8b9ba9")
    s.shape([(27, 78), (27, 14), (115, 14), (115, 25), (101, 29), (110, 42),
             (93, 47), (100, 59), (83, 64), (91, 76)], s.dark)
    s.shape([(27, 14), (41, 8), (128, 8), (115, 14)], "#526f87")
    for x in (35, 52, 69, 86):
        for y in (22, 34, 46, 58, 70):
            if x < 80 or y < 38:
                s.shape([(x,y), (x+8,y), (x+8,y+5), (x,y+5)], "#c6d4d9")
    for x, y in ((101, 51), (117, 58), (102, 67), (126, 69), (143, 72)):
        s.shape([(x,y), (x+10,y+3), (x+8,y+9), (x-4,y+7)], "#526f87")
    s.shape([(108, 72), (118, 81), (99, 83), (92, 78)], "#c5784e")


def bayelsa(s):
    s.shape([(0, 47), (24, 33), (48, 41), (80, 30), (109, 39), (138, 30),
             (160, 36), (160, 90), (0, 90)], "#a9c0ae")
    for y in (51, 59, 68, 78, 86):
        for x in range(6, 155, 27):
            s.line([(x, y), (x+7, y-2), (x+15, y)], "#638c83")
    s.shape([(26, 55), (137, 49), (120, 67), (48, 70)], s.dark)
    s.shape([(42, 47), (50, 29), (109, 25), (126, 44)], "#be6b46")
    for x in (51, 78, 104):
        s.line([(x, 39), (x+2, 54)], s.dark, 2)
    s.line([(33, 58), (127, 54)], "#dcb383")
    for x, y in ((7,24), (17,20), (134,18), (147,25)):
        s.line([(x,y+17), (x,y), (x+8,y-6)], "#69826e", 2)


def capitol(s):
    s.ellipse(55, 12, 105, 58, s.dark)
    s.line([(80, 15), (80, 4)], s.dark, 3)
    s.shape([(15, 51), (80, 36), (145, 51), (145, 57), (15, 57)], s.dark)
    for x in range(25, 144, 13):
        s.line([(x, 57), (x, 75)], s.dark, 5)
    s.line([(17, 78), (144, 78)], s.dark, 5)


def grid(s):
    for x in (42, 119):
        s.line([(x-26, 80), (x, 10), (x+26, 80)], s.dark, 3)
        for y in (26, 42, 61):
            s.line([(x-19, y), (x+18, y)], s.dark, 3)
        s.line([(x-17,65), (x+13,41), (x-11,41), (x+16,65)], s.dark)
    s.shape([(84, 17), (66, 52), (82, 50), (75, 75), (100, 39), (84, 41)], "#a96f1d")


def file_scene(s):
    s.shape([(37, 18), (76, 18), (84, 27), (131, 27), (131, 75), (37, 75)], s.dark)
    s.shape([(48, 35), (129, 35), (117, 74), (38, 74)], s.light)
    for y in (47, 56, 65):
        s.line([(55, y), (106, y)], s.dark, 2)


def market(s):
    s.line([(18, 15), (18, 75), (142, 75)], s.dark, 2)
    for x, y in ((32,31), (54,41), (76,53), (98,61)):
        s.shape([(x,y), (x+13,y), (x+13,74), (x,74)], s.dark)
    s.shape([(123,37),(143,43),(141,59),(123,69),(105,59),(103,43)], s.light)
    s.line([(114, 53), (121, 59), (134, 46)], s.dark, 4)


def atlantic(s):
    s.shape([(10,15), (42,12), (58,26), (50,35), (60,50), (43,67),
             (27,58), (23,46), (12,43)], s.dark)
    s.shape([(104,19), (117,11), (128,24), (145,25), (148,45),
             (132,45), (124,64), (111,55), (117,40), (99,36)], s.dark)
    s.line([(47,48),(61,35),(78,28),(97,29),(114,36)], "#ac604b", 4)
    for x, y in ((47,48),(114,36)):
        s.ellipse(x-6,y-6,x+6,y+6,"#ac604b")


def harbor(s):
    s.shape([(10, 62), (122, 62), (147, 47), (128, 75), (25, 75)], s.dark)
    s.shape([(47,62), (57,44), (111,44), (120,62)], s.dark)
    s.shape([(66,44), (66,32), (88,32), (94,44)], s.dark)
    s.line([(87,32),(87,14),(107,29)], s.dark, 3)
    for x in (14, 59, 106):
        s.line([(x,82),(x+32,82)], s.dark)


def mercury(s):
    s.ellipse(55, 10, 111, 80, s.dark)
    for x, y, r in ((78,29,8),(93,51,10),(75,64,5),(98,26,4)):
        s.ellipse(x-r, y-r, x+r, y+r, s.light)
    s.line([(27,59),(48,67),(75,71),(110,65),(138,49)], "#8a556b", 3)
    s.shape([(127,35),(140,26),(150,35),(138,44)], "#8a556b")


def race(s):
    for x in (40,120):
        s.ellipse(x-15,45,x+15,75,s.dark)
        s.ellipse(x-7,53,x+7,67,s.light)
    s.shape([(35,52),(57,36),(82,45),(114,35),(133,40),(119,58),(73,60)], "#355e86")
    s.line([(59,47),(73,28),(95,30),(111,43)], s.dark, 7)
    s.ellipse(92,14,112,34,s.dark)
    s.line([(12,29),(39,29)],s.dark,3)
    s.line([(12,74),(149,74)],s.dark,2)


def cricket(s):
    for x in (101,112,123):
        s.line([(x,33),(x,74)], s.dark, 3)
    s.line([(100,31),(124,31)],s.dark,3)
    s.shape([(32,70),(24,63),(58,29),(67,37)], "#995440")
    s.line([(63,33),(83,11)], s.dark, 5)
    s.ellipse(65,55,77,69,s.dark)
    s.line([(13,76),(146,76)], s.dark, 2)


def benghazi(s):
    harbor(s)
    s.shape([(119,37),(124,25),(129,34),(136,24),(138,40),(147,39),
             (137,46),(122,46),(112,41)], "#ab5a30")


def masthead():
    rule(24, 19, 1000, INK, 3)
    type_at(24, 28, "WORLD IN FOCUS", 61, "s", limit=640)
    type_at(27, 85, "A global briefing on power, people and the planet", 17, "i", MUTED)
    type_at(998, 38, "SUNDAY", 18, "b", REGION["AMERICAS"], "r")
    type_at(998, 61, "22 NOVEMBER 2026", 30, "b", INK, "r")
    rule(24, 109, 1000, INK, 2)


def statistics():
    metrics = [
        ("258+", "U.S. Democratic House seats", "AMERICAS"),
        ("₦250m", "Aid for Bayelsa families", "AFRICA"),
        ("128", "Runs by India’s Rishabh Pant", "ASIA–PACIFIC"),
        ("8th", "MotoGP title for Márquez", "EUROPE"),
    ]
    for i, (value, label, region) in enumerate(metrics):
        x = 24+i*246
        if i:
            stroke([(x-9, 120), (x-9, 171)], RULE)
        type_at(x, 115, value, 37, "s", REGION[region])
        type_at(x, 153, label, 15, "b", limit=230)
    x = 24
    for region, color in REGION.items():
        span = int(d.textlength(region, font=font(12, "b"))/S)+29
        box(x, 180, x+span, 199, color)
        type_at(x+span/2, 183, region, 12, "b", WHITE, "m")
        x += span+5
    rule(x+5, 189, 1000)


def features():
    teal = "#163e42"
    box(24, 210, 430, 412, teal)
    climate(Scene(215, 230, 207, 116, teal, INK, WHITE))
    type_at(39, 225, "GLOBAL   /   ANTALYA", 13, "b", GOLD)
    type_at(39, 249, "COP31", 49, "s", WHITE, limit=175)
    type_at(39, 294, "deadlock", 45, "s", WHITE, limit=178)
    rule(39, 354, 413, "#66918a")
    type_at(39, 363, "Fossil-fuel dispute blocks the summit’s", 18, "b", WHITE, limit=374)
    type_at(39, 385, "main agreement in Türkiye.", 18, "r", WHITE)

    secondary = [
        (442, "EUROPE", "UKRAINE", "#e0e6e7", "#29465c", dymer,
         ("Russian strike", "hits Kyiv region"),
         ("Part of a Dymer apartment", "block collapsed, officials say.")),
        (727, "AFRICA", "NIGERIA", "#e8e4d3", "#30493d", bayelsa,
         ("Bayelsa boat", "toll reaches 29"),
         ("Tinubu pledges aid and calls", "for tighter waterway safety.")),
    ]
    for x, region, location, field, dark, artist, title, caption in secondary:
        box(x, 210, x+273, 412, field)
        box(x, 210, x+273, 214, REGION[region])
        artist(Scene(x+92, 219, 181, 80, field, dark, WHITE))
        type_at(x+12, 223, location, 13, "b", REGION[region])
        type_at(x+12, 302, title[0], 30, "s", limit=250)
        type_at(x+12, 332, title[1], 30, "s", limit=250)
        type_at(x+12, 369, caption[0], 16, "r", limit=250)
        type_at(x+12, 388, caption[1], 16, "r", limit=250)


def mosaic():
    type_at(24, 422, "Around the world", 26, "s")
    rule(236, 440, 1000, INK)
    columns = [
        (24, 331, "#f0e4db", [
            ("AMERICAS", "UNITED STATES", "Democrats reach 258 seats",
             "Largest House majority since 1992.", capitol),
            ("AMERICAS", "CANADA", "Halifax security forum ends",
             "Canada hosts North Atlantic partners.", atlantic),
            ("MIDDLE EAST", "IRAN", "Iran starts rolling blackouts",
             "Fuel shortages strain power plants.", grid),
        ]),
        (368, 321, "#e4e9eb", [
            ("EUROPE", "POLAND", "Poland alleges a second plot",
             "It says a rapper was Moscow’s target.", file_scene),
            ("EUROPE", "PORTUGAL", "Márquez seals MotoGP title",
             "Bezzecchi wins the Portuguese GP.", race),
            ("AFRICA", "LIBYA", "Blast hits Russian warship",
             "Libyan officials suspect drones.", benghazi),
        ]),
        (702, 298, "#eee3e7", [
            ("ASIA–PACIFIC", "SOUTH KOREA", "Seoul readies market fund",
             "Officials prepare for possible use.", market),
            ("ASIA–PACIFIC", "NEW ZEALAND", "Pant hits 128 in NZ Test",
             "India takes charge on Test day four.", cricket),
            ("GLOBAL", "SPACE SCIENCE", "BepiColombo at Mercury",
             "Nov. 21 orbit insertion · AP report Nov. 22.", mercury),
        ]),
    ]
    for x, w, tint, items in columns:
        for i, (region, place, title, caption, artist) in enumerate(items):
            y = 459+i*76
            color = REGION[region]
            rule(x, y, x+w, color)
            box(x, y+7, x+4, y+65, color)
            art_w = 52
            art_x = x+w-art_w
            artist(Scene(art_x, y+13, art_w, 30, tint, INK, WHITE))
            type_at(x+11, y+8, place, 12, "b", color, limit=w-art_w-17)
            type_at(x+11, y+27, title, 20, "s", limit=w-art_w-17)
            type_at(x+11, y+53, caption, 15, "r", MUTED, limit=w-15)


def world_map():
    x, y, w, h = 24, 691, 562, 174
    box(x, y, x+w, y+h, "#e3ece5")
    type_at(x+13, y+8, "Where the news happened", 24, "s")
    type_at(x+w-12, y+15, "SELECTED LOCATIONS", 11, "b", REGION["GLOBAL"], "r")
    area_x, area_y, area_w, area_h = 34, 731, 340, 124

    def project(lon, lat):
        return area_x+(lon+180)/360*area_w, area_y+(84-lat)/144*area_h

    for lon in range(-180, 181, 60):
        stroke([project(lon, 84), project(lon, -60)], "#c5d5cc")
    for lat in (-60, -30, 0, 30, 60):
        stroke([project(-180, lat), project(180, lat)], "#c5d5cc")

    dataset = json.loads((ROOT/"assets/ne_110m_land.geojson").read_text())
    for feature in dataset["features"]:
        geometry = feature["geometry"]
        polygons = geometry["coordinates"]
        if geometry["type"] == "Polygon":
            polygons = [polygons]
        for rings in polygons:
            if max(lat for _, lat in rings[0]) < -60:
                continue
            for i, ring in enumerate(rings):
                poly([project(lon, lat) for lon, lat in ring], "#aebeb1" if i == 0 else "#e3ece5")

    places = [
        ("Halifax", "Forum", -63.575, 44.649, "AMERICAS"),
        ("Dymer", "Strike", 30.302, 50.784, "EUROPE"),
        ("Antalya", "COP31", 30.705, 36.896, "GLOBAL"),
        ("Bayelsa", "Boat aid", 6.075, 4.792, "AFRICA"),
        ("Seoul", "Markets", 126.978, 37.566, "ASIA–PACIFIC"),
        ("Wellington", "Cricket", 174.783, -41.294, "ASIA–PACIFIC"),
        ("La Jagua", "Curfew", -73.334, 9.563, "AMERICAS"),
    ]
    for i, (place, subject, lon, lat, region) in enumerate(places, 1):
        color = REGION[region]
        mx, my = project(lon, lat)
        if place in {"Dymer", "Antalya"}:
            shift = -12 if place == "Dymer" else 12
            stroke([(mx, my), (mx+shift, my)], color)
            oval((mx-2, my-2, mx+2, my+2), color)
            mx += shift
        oval((mx-7, my-7, mx+7, my+7), color, WHITE)
        type_at(mx, my-5.5, str(i), 10, "b", WHITE, "m")
        row = y+37+(i-1)*17
        oval((387, row+2, 401, row+16), color)
        type_at(394, row+3, str(i), 10, "b", WHITE, "m")
        type_at(409, row, place, 15, "b")
        type_at(573, row+1, subject, 14, "r", MUTED, "r")
    type_at(x+13, y+157, "Natural Earth land data", 10, "r", MUTED)


def digital_assets():
    x, y = 598, 691
    box(x, y, 1000, 865, "#203940")
    type_at(x+14, y+10, "Crypto & Digital Assets", 23, "s", WHITE)
    daily = json.loads((ROOT/"assets/coinbase-btc-usd.json").read_text())["daily"]
    low, high, opening, close = daily[1:5]
    type_at(x+14, y+40, f"${close:,.2f}", 35, "b", GOLD)
    type_at(983, y+43, "BITCOIN / USD", 13, "b", WHITE, "r")
    type_at(983, y+60, "Coinbase · Nov. 22 UTC close", 13, "r", WHITE, "r")
    left, right, center = x+16, 983, y+96
    rule(left, center, right, "#9fb8ae", 3)
    for value, tag, at, anchor in ((low, "Low", left, "l"), (high, "High", right, "r")):
        stroke([(at, center-5), (at, center+5)], "#9fb8ae", 2)
        type_at(at, center+9, f"{tag} ${value:,.0f}", 13, "r", WHITE, anchor)
    for value, color in ((opening, "#b1c8c3"), (close, GOLD)):
        marker = left + (right-left)*(value-low)/(high-low)
        oval((marker-4, center-4, marker+4, center+4), color)
    for marker, label, color in ((753, "Open", "#b1c8c3"), (808, "Close", GOLD)):
        oval((marker-3, center+14, marker+3, center+20), color)
        type_at(marker+7, center+9, label, 12, "r", WHITE)
    rule(x+14, y+126, 985, "#688580")
    type_at(x+14, y+134, "Trump hosts $TRUMP token holders", 19, "s", WHITE, limit=368)
    type_at(x+14, y+155, "Virginia dinner for top holders  /  Reuters", 12, "r", "#c6d8cf")


def digest():
    type_at(24, 873, "World digest", 24, "s")
    rule(179, 889, 1000, INK)
    items = [
        ("AFRICA", "SUDAN · AP", "Strike kills at least 3, official says", "A family home was hit in Omdurman."),
        ("MIDDLE EAST", "WEST BANK · AP", "Eisenkot condemns arson", "Police investigate suspected settler attacks."),
        ("MIDDLE EAST", "YEMEN · AP", "Houthis report Sanaa strike", "They say six fuel-station workers were hurt."),
        ("AMERICAS", "UNITED STATES · REUTERS", "U.S. presses Nvidia on chips", "Bessent seeks answers on sales to China."),
        ("AMERICAS", "MEXICO · IANSEO", "Mexico takes 3 archery golds", "GT Open finals in Strassen, Luxembourg."),
        ("AMERICAS", "COLOMBIA · CARACOL RADIO", "La Jagua imposes curfew", "The mayor acts after a military base attack."),
    ]
    for i, (region, label, title, caption) in enumerate(items):
        y = 904 + (i//3)*54
        x = (24, 354, 684)[i%3]
        color = REGION[region]
        rule(x, y, x+316, color)
        type_at(x, y+4, label, 11, "b", color, limit=316)
        type_at(x, y+16, title, 19, "s", limit=316)
        type_at(x, y+37, caption, 13, "r", MUTED, limit=316)


def render():
    rng = Random(20261122)
    for _ in range(4500):
        x, y = rng.randrange(1024), rng.randrange(1024)
        box(x, y, x+.25, y+.25, "#ece6d7")
    masthead()
    statistics()
    features()
    mosaic()
    world_map()
    digital_assets()
    digest()
    return im.resize((1024, 1024), Image.Resampling.LANCZOS)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("destination", nargs="?", type=Path, default=ROOT/"edition.png")
    cli.add_argument("--proofs", type=Path)
    args = cli.parse_args()
    page = render()
    page.save(args.destination, format="PNG", optimize=True)
    if args.proofs:
        args.proofs.mkdir(parents=True, exist_ok=True)
        for width in (600, 300):
            page.resize((width, width), Image.Resampling.LANCZOS).save(
                args.proofs/f"preview-{width}.png", optimize=True)
