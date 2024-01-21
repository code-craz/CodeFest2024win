import tkinter as tk
from tkinter import filedialog
import subprocess

def run_company_file():
    # Replace 'path_to_company_file' with the actual path to your company file
    subprocess.run(['python', 'AIcompgui.py'])

def run_user_file():
    # Replace 'path_to_user_file' with the actual path to your user file
    subprocess.run(['python', 'Chatbot_user.py'])

def main():
    root = tk.Tk()
    root.title("Button Window")

    company_button = tk.Button(root, text="Company", command=run_company_file)
    company_button.pack(pady=10)

    user_button = tk.Button(root, text="User", command=run_user_file)
    user_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
