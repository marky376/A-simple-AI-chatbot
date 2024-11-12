import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import stringimport random
import re

# Downloading the required nltk data
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.downloads('vader_lexicon')
nltk.download('averaged_perceptron_tagger')


