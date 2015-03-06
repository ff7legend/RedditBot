from __future__ import print_function

import json
import wget
import acoustid
import sys
import youtube_dl
API_KEY = 'HMU8Btr6'
filename1 = 'song.mp3'
dur,fingp = acoustid.fingerprint_file(filename1)

	
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
	