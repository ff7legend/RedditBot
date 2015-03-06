import praw
import acoustid
import os
import spotipy
import time

def spotifyLink(string):
	try:
		sp = spotipy.Spotify()
		results = sp.search(q=string,limit=10)
		return("Link to Spotify Web Player:" + results['tracks']['items'][0]['external_urls']['spotify'])
	except:
		return("No link found")
def match(string):
	API_KEY = 'HMU8Btr6'
	#filename1 = 'song.mp3'
	dur,fingp = acoustid.fingerprint_file(string)
	commentText = ""
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
			commentText += "\n"
		commentText += '%s - %s \n' % (artist, title)

		#commentText += 'http://musicbrainz.org/recording/%s \n'% rid

		#commentText += 'Score: %i%% \n'% (int(score * 100))
	return(commentText)
		
def ytToMp3(string):	
	os.system(string)
	
def run_bot():
	subreddit = r.get_subreddit("hiphopheads")
	comments = subreddit.get_comments(limit= 25)
	topPostsHour = subreddit.get_new(limit=25)
	for x in topPostsHour:	
		if(os.path.isfile("song.mp3")):
			os.remove("song.mp3")	
		if('youtube.com' in str(x.url)):
			dlmp3 = "dlmp3 " + str(x.url)
			ytToMp3(dlmp3)
			commentStr = "bot in progress, let me know what functionality you'd like to see \n"
			commentStr += match("song.mp3") + "\n " 
			spLink = spotifyLink(match("song.mp3"))
			if(spLink):
				commentStr += spLink
			if("-" in commentStr):
				x.add_comment(commentStr)
			time.sleep(700)
		
		
		
	
	
	
#aidmatch info

#	
dlmp3 = ""		
r = praw.Reddit(user_agent = "WatDatSongBeBot") 
r.login('WatDatSongBeBot','password1')



run_bot()


