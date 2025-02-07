from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text and returns a dictionary
    of sentiment scores.
    """
    sentiment = analyzer.polarity_scores(text)
    return sentiment
