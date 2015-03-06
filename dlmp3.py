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

# API key for this demo script only. Get your own API key at the
# Acoustid Web for your application.
# http://acoustid.org/
#YtLink = 'http://www.youtube.com/watch?v=v06jVJMnrTs'
API_KEY = 'HMU8Btr6'
#url = 'http://YouTubeInMP3.com/fetch/?video=' + YtLink #API can go down sometimes
options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : 'mp3',      # convert to mp3 
        'outtmpl': 'song.mp3',        # name the file the ID of the video
        'noplaylist' : True,        # only download single song, not playlist 
	}


#url = 'https://www.youtube.com/watch?v=BTPRlerb1zQ'
url = 'https://www.youtube.com/watch?v=5ynEXVg1P6s'
#filename1 = 'song.mp3'
#dur,fingp = acoustid.fingerprint_file(filename1)
def dlmp3(yturl):
	ydl = youtube_dl.YoutubeDL(options)
	with ydl:
		ydl.download([yturl])
		
if __name__ == '__main__':
	dlmp3(sys.argv[1])