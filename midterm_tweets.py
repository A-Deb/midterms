import sys, codecs, json

from twython import TwythonStreamer, Twython
from datetime import datetime
from time import time

app_key = 'Ok8h1IXemPbnpsUoj0nukaNAF'
app_sec = 'oQcZNzBd5eKnjobSTUdHFwzgUcI3XoFTRSI8u9LvibjdGKEofu'
user_key = '984308525223432192-DtvgjOaD7rfdX6J1spjDKOGnY3fPi31'
user_sec = 'isYXAJtBLhHqywhMiN77zWwmatGRBCAXfyFw04zv9Fg1r'

class FilterAPI(TwythonStreamer):
    def on_success(self, data):
        dt = datetime.now()
        filename = "data/midterms-%s.txt" % (dt.strftime("%Y-%m-%d"),)
        if 'text' in data:
            #print(data['text'])
            fp = codecs.open(filename, 'a', 'utf-8')
            fp.write(json.dumps(data))
            fp.write("\n")
            fp.close()

    def on_error(self, status_code, data):
        print("ERROR!")
        print(status_code)

stream = FilterAPI(app_key, app_sec, user_key, user_sec)
stream.statuses.filter(track=['midtermelections', '2018midterms','2018midtermelections','midterm','elections'])
