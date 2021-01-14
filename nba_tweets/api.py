import tweepy as tw
from . import streamlistener

consumer_key = "rTqL3w4m6iq9h8kFsgufdUHrY"
consumer_secret = "Gd8eHnyYxH27hjDzhf5EDYBBxcaFKIIDlJ2na0xnn24NQygG67"
access_token = "1256988493491863560-AnrQu1rCdmjawNcuKEng89TteDq8zn"
access_secret = "zF6DIILfAnLmi7PSMZQewLnRRD9pf5h4NtDJ7ZhB2mAGo"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth, wait_on_rate_limit=True)

woj = "50323173"
shams = "178580925"

if __name__ == "__main__":
    # initialize stream
    streamListener = streamlistener.StreamListener()
    stream = tw.Stream(auth=api.auth, listener=streamListener, tweet_mode="extended")
    stream.filter(follow=['1256988493491863560'])
