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
        output_text.insert(END, "Bot: I am sorry, I do not know how to answer that. "
                                "I will relay the question to our main center. "
                                "Sorry for the inconvenience.\n")
    else:
        output_text.insert(END, f"Bot: {response}\n")

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
