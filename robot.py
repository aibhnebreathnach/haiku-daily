import tweepy, haiku
from time import sleep
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

tw = tweepy.API(auth)

hku = haiku.Haiku()

while True:
    haiku_text = hku.build_haiku()
    print 'Tweeting: '
    print haiku_text
    tw.update_status(haiku_text) # send tweet
    sleep(86400) # wait 24 hours
