from configs.config import API_key, API_secret_key,access_token_key,access_token_secret

import tweepy

auth = tweepy.OAuthHandler(API_key, API_secret_key) #extra argument of callback_url added for a dynamic URL call (changing url only)
auth.set_access_token(access_token_key, access_token_secret)


api = tweepy.API(auth)

'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

for status in tweepy.Cursor(api.user_timeline, id="TeslaPodcast").items(100):
    process_status(status)
    '''

print('#TSLA')
for tweet in tweepy.Cursor(api.search,q="#TSLA",
                           lang="en",
                           since="2017-04-03").items(5):
    print (tweet.created_at, tweet.text)

print('#TSLAQ')
for tweet in tweepy.Cursor(api.search,q="#TSLAQ",
                           lang="en",
                           since="2017-04-03").items(5):
    print (tweet.created_at, tweet.text)