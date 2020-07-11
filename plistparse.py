#!/usr/bin/env python3

import sys
import plistlib
import csv

if len(sys.argv) != 3:
    print("usage: {} <input.xml> <output.csv>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "rb") as fp:
    pl = plistlib.load(fp)

with open(sys.argv[2], "w") as fc:
    csv.register_dialect("UniversalScrobbler", delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(fc, dialect="UniversalScrobbler")
    scrobbles = 0

    for t in pl["Tracks"]:
        try:
            title = pl["Tracks"][t]["Name"]
        except KeyError:
            print("Record {} is missing mandatory title information, skipping!".format(t), file=sys.stderr)
            continue

        try:
            artist = pl["Tracks"][t]["Artist"]
        except KeyError:
            print("Record {} is missing mandatory artist information, skipping!".format(t), file=sys.stderr)
            continue

        try:
            album = pl["Tracks"][t]["Album"]
        except KeyError:
            album = ""

        try:
            album_artist = pl["Tracks"][t]["Album Artist"]
        except KeyError:
            album_artist = ""

        try:
            length = int(pl["Tracks"][t]["Total Time"]/1000)
        except KeyError:
            length = ""

        try:
            play_count = pl["Tracks"][t]["Play Count"]
        except KeyError:
            print("Failed to get play count for record {}, skipping!".format(t), file=sys.stderr)
            continue
        else:
            if play_count == 0:
                print("Zero plays for record {}!".format(t), file=sys.stderr)

        for _ in range(play_count):
            writer.writerow([artist, title, album, "", album_artist, length])
            scrobbles += 1

print("{} scrobbles written to {}".format(scrobbles, sys.argv[2]))
