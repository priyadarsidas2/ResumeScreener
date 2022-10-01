import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import time
from googlesearch import search
from newspaper import Article
import random
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
stop_words = stopwords.words('english')
stopset = set(nltk.corpus.stopwords.words('english'))
import string
punct = string.punctuation

def cleanTextUsingNLP(extractedText):
    #remove stopwords
    cleaned_text = []
    for word in nltk.word_tokenize(extractedText):
        if word not in punct:
            if word not in stop_words and word.isalpha():
                cleaned_text.append(word)

    cleanedTextAsString = " ".join(cleaned_text)
    return cleanedTextAsString
