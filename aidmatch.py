from __future__ import print_function
# This file is part of pyacoustid.
# Copyright 2011, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

#"""Example script that identifies metadata for files specified on the
#command line.
#"""
import json
import wget
import acoustid
import sys
import youtube_dl
API_KEY = 'HMU8Btr6'
filename1 = 'song.mp3'
dur,fingp = acoustid.fingerprint_file(filename1)
# options = {
        # 'format': 'bestaudio/best', # choice of quality
        # 'extractaudio' : True,      # only keep the audio
        # 'audioformat' : 'mp3',      # convert to mp3 
        # 'outtmpl': 'song.mp3',        # name the file the ID of the video
        # 'noplaylist' : True,        # only download single song, not playlist 
	# }
	
def aidmatch(filename):
    try:
        #results = acoustid.match(API_KEY, filename)
        results1 = acoustid.lookup(API_KEY, fingp, dur)
        results = acoustid.parse_lookup_result(results1)
    except acoustid.NoBackendError:
        print("chromaprint library/tool not found", file=sys.stderr)
        sys.exit(1)
    except acoustid.FingerprintGenerationError:
        print("fingerprint could not be calculated", file=sys.stderr)
        sys.exit(1)
    except acoustid.WebServiceError as exc:
        print("web service request failed:", exc.message, file=sys.stderr)
        sys.exit(1)

    first = True
    for score, rid, title, artist in results:
        if first:
            first = False
        else:
            print()
        print('%s - %s' % (artist, title))
        print('http://musicbrainz.org/recording/%s' % rid)
        print('Score: %i%%' % (int(score * 100)))

if __name__ == '__main__':
	aidmatch(sys.argv[1])
	