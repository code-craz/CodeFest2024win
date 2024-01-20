import json
import nltk
from nltk.chat.util import Chat, reflections
import string

nltk.download('punkt')

# Define patterns and responses for the chatbot
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name', ['I am a chatbot. You can call me Bot.']),
    (r'quit', ['Goodbye!', 'Bye!', 'See you later.']),
    # Add more patterns and responses as needed
]

# File path for storing and loading data
data_file_path = 'chatbot_data.json'


try:
    with open(data_file_path, 'r') as file:
        data = json.load(file)
        learning_dict = data.get('learning_dict', {})
except (FileNotFoundError, json.JSONDecodeError):
    learning_dict = {}


chatbot = Chat(patterns, reflections)

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()
    return text

def learn_response(user_input):
    
    correct_response = input("Bot: I don't know how to respond. Please provide a correct response: ")
    

    preprocessed_input = preprocess_text(user_input)
    learning_dict[preprocessed_input] = correct_response
    