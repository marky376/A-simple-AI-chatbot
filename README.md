# SmartChatbot: A Basic NLTK-Powered Chatbot

This project implements a simple chatbot using Python and the NLTK library. The chatbot can handle basic greetings, answer questions (e.g., "what is X?", "how does Y work?"), respond to farewells, and perform sentiment analysis on user inputs to tailor its responses.

## Project Structure
- `chat.py`: The main file containing the `SmartChatbot` class, which handles user interactions, question processing, and sentiment analysis.

## Prerequisites
To run this project, you'll need:
- Python 3.6 or higher
- The NLTK library and its required data packages

## Setup Instructions
1. **Install Python**: Ensure Python 3.6+ is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install NLTK**:
   - Open a terminal and install NLTK using pip:
     ```
     pip install nltk
     ```
3. **Download NLTK Data**:
   - The script automatically downloads the required NLTK data (`punkt_tab`, `stopwords`, `vader_lexicon`, `averaged_perceptron_tagger`, `averaged_perceptron_tagger_eng`) on the first run. Ensure you have an internet connection.
   - If you prefer to download them manually, run the following in a Python shell:
     ```python
     import nltk
     nltk.download('punkt_tab')
     nltk.download('stopwords')
     nltk.download('vader_lexicon')
     nltk.download('averaged_perceptron_tagger')
     nltk.download('averaged_perceptron_tagger_eng')
     ```

## Running the Chatbot
1. Navigate to the project directory in your terminal.
2. Run the script:

   python chat.py

3. Interact with the chatbot:
- Type messages like "hi", "what is Python?", or "bye" to see how the chatbot responds.
- To exit, type "bye", "goodbye", or "exit".

## Example Interaction

Bot: Hi! I'm a smarter chatbot now. I can handle questions! Type 'bye' to exit.
You: Hello
Bot: Hello Nice to meet you! How can I help you today?
You: What is Python?
Bot: Regarding Python, I would say...
You: Bye
Bot: Goodbye! Have a great day!

## Notes
- The chatbot uses NLTK for tokenization, POS tagging, and sentiment analysis.
- It has a basic knowledge base for greetings, questions, and farewells, but its responses are limited and may not handle complex inputs well.
- Known issues:
  - No error handling for failed NLTK downloads.
  - Limited question-handling capabilities (e.g., struggles with multi-part questions).
  - Typos in the code (e.g., `reponses` instead of `responses`).

## Future Improvements
- Add support for multi-turn conversations.
- Improve sentiment analysis for more nuanced responses.
- Add error handling for NLTK downloads and invalid inputs.
