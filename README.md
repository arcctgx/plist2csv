# Background
A Reddit user once asked if it was possible to import their listening history from
Apple Music to Last.fm. Turns out it's possible (sort of), so I created `plist2csv.py`
to help.

The purpose of this tool is to read the library export from Apple Music in Property
List format, and to produce `CSV` output in dialect suitable for use with "Bulk scrobble"
mode of [Universal Scrobbler](http://universalscrobbler.com). It parses exported Apple
Music library file, and for each track it writes a number of `CSV` records equal to the
play count of the track.

# Usage example
```
$ ./plist2csv.py
usage: ./plist2csv.py <input.xml> <output.csv>

$ ./plist2csv.py test/apple_music_library_excerpt.xml test.csv
Record 2046 is missing mandatory artist information, skipping!
Record 2049 is missing mandatory title information, skipping!
Failed to get play count for record 2051, skipping!
Zero plays for record 2053!
223 scrobbles written to test.csv
```
This example shows four possible error cases which will cause the track to be ignored
by `plist2csv.py`. Artist and title information are mandatory for Last.fm. The number
of plays has to be known in order to produce the correct number of `CSV` records.

Missing album, album artist or track duration are not treated as errors, because these
fields are not required by Universal Scrobbler. An empty field is written in these
cases.

# Limitations
Apple Music export is not actually a complete listening history, because it doesn't
store the timestamps of all plays - just of the most recent one. It stores the number
of times each track was played, and that's it. So there's no way to create a scrobble
timestamp in the `CSV` record.

This may seem like a deal breaker, but in practice it isn't. First of all, Last.fm will
anyway reject all scrobbles with timestamps older than 2 weeks from the current date.
Second, the timestamp field is not mandatory for Universal Scrobbler - it will make an
assumption regarding the timestamp if it's not provided.

So if you only care about the play counts, then this tool can be useful. But it can't
convert the contents of your music library into a neat listening history with the true
timestamps.

A final remark - Last.fm limits the number of scrobbles user can submit in one day, so
please have that in mind when importing a large number of scrobbles.
