
import tweepy
from twitter_auth import auth

api = tweepy.API(auth)
user = api.get_user('twitter')

# tweepy models contain the data plus and some methods.
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)
