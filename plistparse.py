#!/usr/bin/env python3

import plistlib

with open("apple_music_library_excerpt.xml", "rb") as fp:
    pl = plistlib.load(fp)

for t in pl["Tracks"]:
    # mandatory fields, don't handle exceptions, let it crash and burn if info is missing
    title = pl["Tracks"][t]["Name"]
    artist = pl["Tracks"][t]["Artist"]
    # there's no way to get timestamps of individual plays
    timestamp = ""

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
        play_count = 0

    for _ in range(play_count):
        print('"{}", "{}", "{}", "{}", "{}", "{}"'.format(artist, title, album, timestamp, album_artist, length))
