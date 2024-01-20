import string
from tkinter import Tk, Scrollbar, Text, Entry, Button, END

from nltk.chat.util import Chat, reflections

# Create a simple chatbot
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name', ['I am a chatbot. You can call me Bot.']),
    (r'quit', ['Goodbye!', 'Bye!', 'See you later.']),
    # Add more patterns and responses as needed
]

chatbot = Chat(patterns, reflections)

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()
    return text

def submit_user_input():
    user_input = user_input_entry.get().lower()  # Convert user input to lowercase

    # Check if the user wants to quit
    if user_input == 'quit':
        output_text.insert(END, "Bot: Goodbye!\n")
        window.destroy()
        return

    # Use the chatbot to find a response
    response = chatbot.respond(user_input)

    # If the chatbot doesn't have a predefined response, display a default message
    if not response:
        preprocessed_input = user_input.translate(str.maketrans("", "", string.punctuation)).lower()
        best_match = learning_dict.get(preprocessed_input)
        if best_match:
            print(f"Bot: {best_match}")
        else:
            print("Bot: I don't know how to respond to that. I will relay you query to our main center. I am sorry for the inconvenience.")
