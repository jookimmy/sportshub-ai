import tweepy as tw
from pandas import DataFrame as df
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
    def on_status(self, status):
        url = f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"

        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status, "extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status, "extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",", "\n"]
        for c in remove_characters:
            text.replace(c, " ")
            quoted_text.replace(c, " ")

        with open("out.csv", "a", encoding="utf-8") as f:
            f.write(
                "%s,%s,%s,%s,%s,%s,%s\n"
                % (
                    status.created_at,
                    status.user.screen_name,
                    is_retweet,
                    is_quote,
                    text,
                    quoted_text,
                    url,
                )
            )

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()


if __name__ == "__main__":
    # initialize stream
    streamListener = StreamListener()
    stream = tw.Stream(auth=api.auth, listener=streamListener, tweet_mode="extended")
    stream.filter(follow=[woj, shams])
    with open("out.csv", "w", encoding="utf-8") as f:
        f.write("date,user,is_retweet,is_quote,text,quoted_text,url\n")

