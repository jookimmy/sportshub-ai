import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportshubai.settings')
django.setup()


from django.db import connection
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

cursor = connection.cursor()

class StreamListener(tw.StreamListener):
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
                quote_tweet = str(status.quoted_status.id)
            else:
                quote_tweet = "None"

            remove_characters = [",", "\n"]
            for c in remove_characters:
                text.replace(c, " ")
            
            reply_tweet = str(status.in_reply_to_status_id)

            # add info into mysql database
            # need to add reply status and its ID
            cursor.execute("SELECT count(*) from tweets;")
            r = cursor.fetchone()
            if r[0] == 3:
                cursor.execute("DELETE FROM tweets LIMIT 1;")

            cursor.execute("INSERT INTO tweets (TweetID,Text,URL,QuoteID,ReplyID) VALUES (%s,%s,%s,%s,%s);",[status.id_str,text,url,quote_tweet,reply_tweet])

            print(status.id_str)




            

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

if __name__ == "__main__":
    # initialize stream
    streamListener = StreamListener()
    stream = tw.Stream(auth=api.auth, listener=streamListener, tweet_mode="extended")
    stream.filter(track=["python"])
    #follow=["1256988493491863560"]