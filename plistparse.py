#!/usr/bin/env python3

import sys
import plistlib

with open("apple_music_library_excerpt.xml", "rb") as fp:
    pl = plistlib.load(fp)

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
        print('"{}", "{}", "{}", "{}", "{}", "{}"'.format(artist, title, album, "", album_artist, length))
