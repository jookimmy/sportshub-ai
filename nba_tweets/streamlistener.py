import tweepy as tw

class StreamListener(tw.StreamListener):

    tweet_list = []
    
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
                quote_tweet = status.quoted_status.id_str
            else:
                quote_tweet = False

            # remove characters that might cause problems with csv encoding
            remove_characters = [",", "\n"]
            for c in remove_characters:
                text.replace(c, " ")

            if len(self.tweet_list) > 10:
                self.tweet_list.pop(0)
            self.tweet_list.append([status.user.screen_name, text, quote_tweet, url])

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()
