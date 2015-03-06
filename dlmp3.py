from __future__ import print_function

import json
import wget
import acoustid
import sys
import youtube_dl


options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : 'mp3',      # convert to mp3 
        'outtmpl': 'song.mp3',        # name the file the ID of the video
        'noplaylist' : True,        # only download single song, not playlist 
	}



url = 'https://www.youtube.com/watch?v=5ynEXVg1P6s'

def dlmp3(yturl):
	ydl = youtube_dl.YoutubeDL(options)
	with ydl:
		ydl.download([yturl])
		
if __name__ == '__main__':
	dlmp3(sys.argv[1])