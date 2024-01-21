from tkinter import *
import subprocess

def open_chatbot_file():
    subprocess.Popen(['python', 'intermission.py'], shell=True)

def open_ai_product_file():
    subprocess.Popen(['python', 'AI_productGUI.py'], shell=True)

root = Tk()

# Load the background image
background_image = PhotoImage(file="Yellow-Banner-Background-HD.png")

# Create a label to hold the background image
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

myLabel = Label(root, text="Welcome to SSA", font=("Helvetica", 16, "bold"), bg="#ffffff")
myLabel.grid(row=0, column=1, pady=20)

myLabel2 = Label(root, text="Customizable ChatBot for your website", font=("Helvetica", 14), bg="#ffffff")
myLabel2.grid(row=3, column=0)

myLabel3 = Label(root, text="Product Development Assistant", font=("Helvetica", 14), bg="#ffffff")
myLabel3.grid(row=3, column=2)

myLabel4 = Label(root, text=" ", bg="#ffffff")
myLabel4.grid(row=1, column=1)

myButton = Button(root, text="ChatBot", command=open_chatbot_file, font=("Helvetica", 12))
myButton.grid(row=1, column=0, pady=20)

myButton2 = Button(root, text="AI Product Development", command=open_ai_product_file, font=("Helvetica", 12))
myButton2.grid(row=1, column=2, pady=20)

root.mainloop()
