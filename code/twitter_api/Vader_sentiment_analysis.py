from tweets import tweet_list
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("\n")
    print("{:-<40} {}".format(sentence, str(snt)))

for tweet in tweet_list:
    print_sentiment_scores(tweet)