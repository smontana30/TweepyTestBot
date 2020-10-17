import tweepy 


consumer_key = "Your Api Key"
consumer_secret = "Your Secret Api Key"
access_token = "Your access token"
access_token_secret = "Your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the User object for twitter...
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#     print()
user = api.get_user('twitter')

# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['bts'])
