# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "I love negativity"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

"""
documentSentiment contains the overall sentiment of the document, which consists of the following fields:
score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text.
magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes).
"""

#score: -1.0(negative) and 1.0(positive) overall emotional leaning of the text
#magnitude: between 0.0 and +inf overall strength of emotion

"""
The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.
"""

def calc_sentiment(sentiment):
    if (sentiment.score > 0):
        return "positive"
    elif (seniment.score < 0):
        return "negative"
    else:
        return "neutral"
print(calc_sentiment(sentiment))
