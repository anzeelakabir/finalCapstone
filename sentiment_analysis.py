# Capstone Project - NLP Applications

# Importing the necessary libraries.
import pandas as pd 
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from textblob import TextBlob

# Loading the dataset into a DataFrame. 
# Using raw string literal
csv_file_path = r"C:\Users\anzee\amazon_product_reviews.csv"
dataframe = pd.read_csv(csv_file_path)

# Loading the spaCy model.
nlp = spacy.load("en_core_web_sm")

# Defining the function to preprocess the text data.
def preprocess_text(text):
    # Tokenizing the text using spaCy. 
    doc = nlp(text)
    # Eliminating the stop words and non-alphabetic tokens, and converting them to lowercase.
    tokens = [token.text.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    # Joining the tokens back into a string with space in between.
    return ' '.join(tokens)

# Defining a function to perform sentiment analysis.
def analyse_sentiment(text):
    # Tokenizing the text using spaCy.
    doc = nlp(text)
    # Calculate polarity using TextBlob.
    polarity = TextBlob(text).sentiment.polarity
    # Determine the sentiment based on polarity.
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Sample reviews for testing sentiment analysis.
sample_reviews = ["I love this product! It's amazing.", "The quality is poor and I'm not satisfied."]

# Testing the sentiment analysis function on sample product reviews. 
for review in sample_reviews:
    # Preprocessing the review text.
    preprocessed_review = preprocess_text(review)
    # Analyzing the sentiment.
    sentiment = analyse_sentiment(preprocessed_review)
    # Printing the review and its sentiment.
    print(f"Review: {review} | Sentiment: {sentiment}")


