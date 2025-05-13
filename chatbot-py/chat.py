from ast import pattern
import string
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
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Creating the chatbot class/interface
class SmartChatbot:
    def __init__(self):
        # Enhancing knowledge base with question-answer pairs
        self.knowledge_base = {
            'greetings': {
                'patterns': ['hi', 'hello', 'hey', 'good morning', 'good evening', 'good afternoon'],
                'responses': [
                    "Hi there! How can I help you roday?",
                    "Hello Nice to meet you! How can I help you today?",
                    "Hey! WHat's on your mind today?"
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
                    'patterns': ['how do', 'how can', 'how does'],
                    'responses': [
                        "Here's a way to approach {topic}...",
                        "When dealing with {topic}, you might want to...",
                        "The process for {topic} typically involves..."
                    ]
                },
                'why': {
                    'patterns': ['why is', 'why do', 'why does'],
                    'responses': [
                        "The reason for {topic} might be...",
                        "Thinking about {topic}, I believe...",
                        "Let me explain why {topic}..."
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
        self.stop_words = set(stopwords.words('english'))


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
                for patter in self.knowledge_base['questions'][qtype]['patterns'])
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
    # Building the bots rudimentaty brain
    def get_response(self, user_input):
        """Generate a more thoughtful response based on imput type"""
        tokens, tagged_tokens = self.tokenize_and_tag(user_input)

        # Checking for greetings and farewells first
        for category in ['greetings', 'farewell']:
            if any(pattern in user_input.lower() for pattern in self.knowledge_base[category]['patterns']):
                return random.choice(self.knowledge_base[category]['responses'])

        # Identifying question type and extracting topic
        q_type, topic = self.identify_question_type(user_input, tagged_tokens)
        if q_type:
            if q_type in self.knowledge_base['questions']:
                template = random.choice(self.knowledge_base['questions'][q_type]['reponses'])
                return template.format(topic=topic)
            else:
                # Handling general questions
                return f"That's an interesting question about {topic} . Let me think..."
        # If not a question, use sentiment analysis for response
        sentiment = self.analyze_sentiment(user_input)
        if sentiment > 0.2:
            return "I sense enthusism! Tell me more about your thoughts on this."
        elif sentiment < -0.2:
            return "I understand this might be chalenging. Would you like to explore this further?"
        else:
            return "I see what you mean. Can you elaborate on that?"
    def analyze_sentiment(self, text):
        """Analyze the sentiment of the user input"""
        scores = self.sentiment_analyzer.popularity_score(text)
        return scores['compound']
    
    def chat(self):
        """Main chat loop"""
        print("Bot:Hi! I'm a smarter chatbot now. I can handle questions! Type 'bye' to exit.")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['bye', 'goodbye', 'exit']:
                print("Bot:", random.choice(self.knowledge_base['farewell']['responses']))
                break
            response = self.get_response(user_input)
            print("Bot:", response)

    
# Creating an instance of the chatbot and starting the chatbot
if __name__ == "__main__":
    chatbot = SmartChatbot()
    chatbot.chat()
