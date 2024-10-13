from textblob import TextBlob


file = open('text.txt', encoding='utf-8').read()

blob = TextBlob(file)
sentiment = blob.sentiment.polarity

# sentiment is between -1 and 1
# -1 - very negative sentiment
# 0  - neutral
# 1 -  very positive sentiment

print(sentiment)
