import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# NLTK Downloads (lines 10-14)
for package in ['punkt_tab', 'stopwords', 'vader_lexicon', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng']:
    try:
        nltk.download(package)
    except Exception as e:
        print(f"Error downloading NLTK package: {package}. Some features may not work correctly.")

class SmartChatbot:
    def __init__(self):
        self.greetings = ["Hello! How can I assist you roday?", "Hi there! How can I help you roday?"]  # Line 17: 'roday' typo (unchanged)
        self.farewells = ["Goodbye! Have a great day!", "See you later!"]
        self.stop_words = set(stopwords.words('english'))
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.knowledge_base = {
            'questions': {
                'what': {
                    'responses': ["Regarding {topic}, I would say...", "{topic} is..."]
                },
                'why': {
                    'responses': ["The reason for {topic} is...", "Because..."]
                },
                'how': {
                    'responses': ["To {topic}, you can...", "Here’s how to {topic}..."]
                },
                'default': {
                    'responses': ["I’m not sure about {topic}, but...", "Let me think about {topic}..."]
                }
            }
        }

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        return [token for token in tokens if token not in self.stop_words]

    def identify_question_type(self, text):
        tokens = self.preprocess_text(text)
        tagged = pos_tag(tokens)
        patter = [(word, tag) for word, tag in tagged]  # Line 69: 'patter' typo (unchanged)
        if tokens and tokens[0] in ['what', 'which']:
            return 'what'
        elif tokens and tokens[0] == 'why':
            return 'why'
        elif tokens and tokens[0] == 'how':
            return 'how'
        else:
            return 'default'

    def get_response(self, text):
        if any(greeting.lower() in text.lower() for greeting in ['hello', 'hi', 'hey']):
            return random.choice(self.greetings)
        elif any(farewell.lower() in text.lower() for farewell in ['bye', 'goodbye', 'see you']):
            return random.choice(self.farewells)
        else:
            q_type = self.identify_question_type(text)
            template = random.choice(self.knowledge_base['questions'][q_type]['responses'])  # Line 79: Fixed
            topic = ' '.join(self.preprocess_text(text))
            return template.format(topic=topic)

    def analyze_sentiment(self, text):
        scores = self.sentiment_analyzer.polarity_scores(text)  # Line 91: Fixed
        if scores['compound'] >= 0.05:
            return "That sounds positive!"
        elif scores['compound'] <= -0.05:
            return "That sounds negative."
        else:
            return "That sounds neutral."

    def chat(self):
        print("Welcome to the Smart Chatbot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if any(farewell.lower() in user_input.lower() for farewell in ['bye', 'goodbye', 'see you']):
                print("Bot:", self.get_response(user_input))
                break
            elif any(greeting.lower() in user_input.lower() for greeting in ['hello', 'hi', 'hey']):
                print("Bot:", self.get_response(user_input))
            else:
                sentiment_response = self.analyze_sentiment(user_input)
                knowledge_response = self.get_response(user_input)
                print("Bot:", knowledge_response)
                print("Bot:", sentiment_response)

if __name__ == "__main__":
    chatbot = SmartChatbot()
    chatbot.chat()