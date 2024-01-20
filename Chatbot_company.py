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

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()
    return text

def learn_response(user_input):
    # Get the correct response from the user
    correct_response = input("Bot: I don't know how to respond. Please provide a correct response: ")
    
    # Store the preprocessed user input and correct response in the learning dictionary
    preprocessed_input = preprocess_text(user_input)
    learning_dict[preprocessed_input] = correct_response
    
    # Save the learning dictionary to the file immediately after teaching
    with open(data_file_path, 'w') as file:
        json.dump({'learning_dict': learning_dict}, file, indent=2)
    
    print("Bot: Thank you for teaching me!")

# Main loop for interacting with the chatbot
print("Bot: Hello! I'm a chatbot. You can type 'quit' to exit.")
while True:
    user_input = input("You: ").lower()  # Convert user input to lowercase
    
    # Check if the user wants to quit
    if user_input == 'quit':
        print("Bot: Goodbye!")
        break

    # Check if the user wants to teach the chatbot
    if user_input == 'teach':
        new_input = input("Bot: What keyword or phrase do you want to teach me a response for? ")
        learn_response(new_input)
    else:
        # Use the chatbot to find a response
        response = chatbot.respond(user_input)
        
        # If the chatbot doesn't have a predefined response, find the best match
        if not response:
            preprocessed_input = preprocess_text(user_input)
            best_match = learning_dict.get(preprocessed_input)
            if best_match:
                print(f"Bot: {best_match}")
            else:
                learn_response(user_input)
        else:
            print(f"Bot: {response}")
        