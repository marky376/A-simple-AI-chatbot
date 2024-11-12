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
        self.stop_words = set(stopwords('english'))


    def tokenize_and_tag(self, user_input):
        """Clean, tokenize, and POs tag user input"""
        #Clean and tokenize user input
        cleaned = user_input.lower().translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(cleaned)
        #POS tag tokens
        tagged = pos_tag(tokens)
        return tokens, tagged

    def extract_topic(self, tokens, question_word):
        """Extract the main topic after a question word"""
        # Finding the question word's position
        try:
            q_pos = tokens.index(question_word.lower())
            # Get everything after the question word and auxilliary verbs
            topic_words = tokens[q_pos + 2:] # Slip question word and auxilliary verb
            # Remove stop words
            topic = ' '.join([word for word in topic_words if word not in self.stop_words])
            return topic if topic else "that"
        except ValueError:
            return "that"
    def identify_question_type(self, user_input, tagged_tokens):
        """Identify the type of question and extract relevant information"""
        question_words = [
            'what', 'why', 'how', 'when', 'where', 'who'
        ]
            
        # Checking if its a question
        is_question = any([
            user_input.endswith('?'),
            any(word.lower() in question_words for word, tag in tagged_tokens),
            any(pattern in user_input.lower() for qtype in self.knowledge_base['questions']
                for patter in seld.knowledge_base['questions'][qtype]['patterns'])
        ])
        if not is_question:
            return None, None
        # Identifying the question type and topic
        for q_type, q_info in self.knowledge_base['questions'].items():
            for pattern in q_info['patterns']:
                if pattern in user_input.lower():
                    topic = self.extract_topic(user_input.split(), q_type)
                    return q_type, topic
        return 'general', 'that'
                