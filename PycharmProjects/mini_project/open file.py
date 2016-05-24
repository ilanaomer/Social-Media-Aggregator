from csv import DictReader
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


ISRAEL_LAT, ISRAEL_LON = 31.5, 34.75
# originally from http://stackoverflow.com/a/15737218/57952 :


with open('cow.csv', encoding="utf-8") as f:
    reader = DictReader(f)
    s = "<ul>\n"
    for c in reader:
        dis = haversine(ISRAEL_LON, ISRAEL_LAT, float(c['lon']), float(c['lat']))
        s += "\t<li><img src=\"http://static.10x.org.il/flags/{}.png\"><a href=""Co_html//{}.html"">*{}</a>: {:,f} km</li>".format(c['short_name'].lower(),c['short_name'],c['name'], dis)
s += "\n</ul>"
with open('index.html', "w") as f1:
    f1.write(s)
