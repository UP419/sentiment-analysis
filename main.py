from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

file = open('text.txt', encoding='utf-8').read()

sentiment = analyzer.polarity_scores(file)

# Print results
print(sentiment)