import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import random
import re

# Downloading the required nltk data
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.downloads('vader_lexicon')
nltk.download('averaged_perceptron_tagger')


# Creating the chatbot class/interface
class SmartChatbot:
    def __init__(self):
        # Enhancing knowledge base with question-answer pairs
        self.knowledge_base = {
            'greetings': {
                'patterns': ['hi', 'hello', 'hey', 'good morning', 'good evening', 'good afternoon'],
                'responses': [
                    "Hi there! How can I help you roday?",
                    "Hello Nice ro meet you! How can I help you today?",
                    "Hey! WHat's on your ind today?"
                ]
            },
            'questions': {
                'what': {
                    'patterns': ['what is', 'what are', 'what can'],
                    'responses': [
                        "let me thing about {topic}...",
                        "Regarding {topic}, I would say...",
                        "When it comes to {topic}, here's what I know..."
                    ]
                },
                'how': {
                    'patterns': ['howdo', 'how can', 'how does'],
                    'responses': [
                        "Here's a wat to approach {topic}...",
                        "when dealing with {topic}, you might want to...",
                        "The process for {topic} typically involves..."
                    ]
                },
                'why': {
                    'patterns': ['why is', 'why do', 'why does'],
                    'responses': [
                        "The reason for {topic} might be...",
                        "thinking about {topic}, I believe...",
                        "let me explain why {topic}..."
                    ]
                }
            },
            'farewell': {
                'patterns': ['bye', 'goodbye', 'see you Later'],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you Later!",
                    "Bye! Come back soon!"
                ]
            }
        }
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords('english')
                              )
