import tweepy as tw
import sys

consumer_key = "rTqL3w4m6iq9h8kFsgufdUHrY"
consumer_secret = "Gd8eHnyYxH27hjDzhf5EDYBBxcaFKIIDlJ2na0xnn24NQygG67"
access_token = "1256988493491863560-AnrQu1rCdmjawNcuKEng89TteDq8zn"
access_secret = "zF6DIILfAnLmi7PSMZQewLnRRD9pf5h4NtDJ7ZhB2mAGo"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth, wait_on_rate_limit=True)

woj = "50323173"
shams = "178580925"

class StreamListener(tw.StreamListener):
    tweet_id = None
    screen_name = None
    text = None
    quote_tweet = None
    url = None
    
    def on_status(self, status):
        url = f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"

        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        if not is_retweet:
            # check if text has been truncated
            if hasattr(status, "extended_tweet"):
                text = status.extended_tweet["full_text"]
            else:
                text = status.text

            # check if this is a quote tweet.
            is_quote = hasattr(status, "quoted_status")
            if is_quote:
                # if it is a quote, then note down the ID of the original tweet
                quote_tweet = status.quoted_status.id
            else:
                quote_tweet = False

            # remove characters that might cause problems with csv encoding
            remove_characters = [",", "\n"]
            for c in remove_characters:
                text.replace(c, " ")

            tweet_id = status.id
            screen_name = status.user.screen_name
            text = text
            quote_tweet = quote_tweet
            url = url
            # if len(self.tweet_list) > 10:
            #     self.tweet_list.pop(0)
            # self.tweet_list.append([status.user.screen_name,status.id, text, quote_tweet, url])

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

if __name__ == "__main__":
    # initialize stream
    streamListener = StreamListener()
    stream = tw.Stream(auth=api.auth, listener=streamListener, tweet_mode="extended")
    stream.filter(follow=['1256988493491863560'])