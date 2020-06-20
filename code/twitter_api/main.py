from TextBlob_sentiment_analysis import TwitterClient
import pandas as pd

def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = '#TSLA', items=250)
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets)))

    #write csv file
    df = pd.DataFrame()
    df["Tweet"] = [tweet["text"] for tweet in tweets]
    df["Sentiment"] = [sentiment["sentiment"] for sentiment in tweets]
    df.to_csv('sentiment_test.csv')
  
if __name__ == "__main__": 
    # calling main function 
    main() 