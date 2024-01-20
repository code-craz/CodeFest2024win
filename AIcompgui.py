import json
import nltk
import string
from tkinter import Tk, Scrollbar, Text, Entry, Button, END, simpledialog

from nltk.chat.util import Chat, reflections

nltk.download('punkt')

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
chatbot = Chat([], reflections)

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()
    return text

def learn_response(user_input, correct_response):
    # Store the preprocessed user input and correct response in the learning dictionary
    preprocessed_input = preprocess_text(user_input)
    learning_dict[preprocessed_input] = correct_response

    # Save the learning dictionary to the file immediately after teaching
    with open(data_file_path, 'w') as file:
        json.dump({'learning_dict': learning_dict}, file, indent=2)

    output_text.insert(END, "Bot: Thank you for teaching me!\n")

def submit_user_input():
    user_input = user_input_entry.get().lower()  # Convert user input to lowercase

    # Check if the user wants to quit
    if user_input == 'quit':
        output_text.insert(END, "Bot: Goodbye!\n")
        window.destroy()
        return

    # Check if the user input matches any patterns or responses from the JSON file
    response = learning_dict.get(preprocess_text(user_input))
    if response:
        output_text.insert(END, f"Bot: {response}\n")
    else:
        output_text.insert(END, "Bot: I don't know how to respond to that. Can you please teach me?\n")
        new_input = simpledialog.askstring("Teach Bot", "What keyword or phrase do you want to teach me a response for?")
        if new_input:
            correct_response = simpledialog.askstring("Teach Bot", "What is the correct response?")
            if correct_response:
                learn_response(new_input, correct_response)
                user_input_entry.delete(0, END)  # Clear the user input field

# GUI setup
window = Tk()
window.title("Chatbot GUI")

# User Input Entry
user_input_entry = Entry(window, width=50)
user_input_entry.grid(row=0, column=0, padx=10, pady=10)

# Submit Button
submit_button = Button(window, text="Submit", command=submit_user_input)
submit_button.grid(row=0, column=1, padx=10, pady=10)

# Output Text
output_text = Text(window, width=60, height=20, wrap='word')
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Scrollbar for Output Text
scrollbar = Scrollbar(window, command=output_text.yview)
scrollbar.grid(row=1, column=2, sticky='ns')
output_text['yscrollcommand'] = scrollbar.set

# Run the GUI
window.mainloop()
