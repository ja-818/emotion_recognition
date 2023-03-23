from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    sentiment = ""
    
    if sentiment_dict['compound'] >= 0.05 :
        sentiment = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = "Negative"

    else :
        sentiment = "Neutral"  

    return sentiment