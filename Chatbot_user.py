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

# Load existing data from the file or create an empty dictionary
try:
    with open(data_file_path, 'r') as file:
        data = json.load(file)
        learning_dict = data.get('learning_dict', {})
except (FileNotFoundError, json.JSONDecodeError):
    learning_dict = {}

# Create a simple chatbot
chatbot = Chat(patterns, reflections)

# Main loop for interacting with the chatbot
print("Bot: Hello! I'm a simple chatbot. You can type 'quit' to exit.")
while True:
    user_input = input("You: ").lower()  # Convert user input to lowercase
    
    # Check if the user wants to quit
    if user_input == 'quit':
        print("Bot: Goodbye!")
        break

    # Use the chatbot to find a response
    response = chatbot.respond(user_input)
    
    # If the chatbot doesn't have a predefined response, try to fetch from the JSON file
    if not response:
        preprocessed_input = user_input.translate(str.maketrans("", "", string.punctuation)).lower()
        best_match = learning_dict.get(preprocessed_input)
        if best_match:
            print(f"Bot: {best_match}")
        else:
            print("Bot: I don't know how to respond to that. I will relay you query to our main center. I am sorry for the inconvenience.")