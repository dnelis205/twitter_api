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

query = "#TSLA"
language = "en"
start_date = "2017-04-03"
max_tweets = 20

print('#TSLA')
tweet_list = []
for tweet in tweepy.Cursor(api.search,q=query,
                           lang=language,
                           since=start_date).items(max_tweets):
    tweet_text = tweet.text
    tweet_list.append(tweet_text)
    #print (tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location)

#tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location