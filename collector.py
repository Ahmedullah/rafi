
from tweepy import Stream, OAuthHandler, StreamListener, TweepError
import json
import sys

def load_auth_info(keys_file, app_name):

    with open(keys_file) as fp:
        d = json.load(fp)
        for record in d:
            if record['app_name'] == app_name:
                return record

class TwitterStreamListener(StreamListener):

    def __init__(self, fp):
        self.fp = fp
        
    def on_data(self, data):
        d = json.loads(data)
        json.dump(d, self.fp)
        fp.write('\n')
        return True

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print '>>> Usage: python collector.py twitter_app_keys_file app_name dump_filename'
        sys.exit(-1)

    keys = load_auth_info(sys.argv[1], sys.argv[2])

    try:
        auth = OAuthHandler(keys['api_key'], keys['api_secret'])
        auth.set_access_token(keys['access_token'], keys['access_token_secret'])

        with open(sys.argv[3], 'a') as fp: # keep adding to the file
            stream = Stream(auth = auth, listener = TwitterStreamListener(fp))
            stream.filter(track = ['global warming', 'oil spill'])
        
    except TweepError as e:
        print '>>> tweepy error: ', e
    except KeyboardInterrupt:
        print '>>> Keyboard interrupt received...'
    finally:
        print '>>> Closing twitter stream...'
        stream.disconnect()
