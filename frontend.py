from tkinter import *
import subprocess

def open_chatbot_file():
    subprocess.Popen(['python', 'AIcompgui.py'], shell=True)

def open_ai_product_file():
    subprocess.Popen(['python', 'AI_productGUI.py'], shell=True)

root = Tk()

myLabel = Label(root, text="Welcome to SSA")
myLabel.grid(row=0, column=1)
 
myLabel2 = Label(root, text="Customizable ChatBot for your website")
myLabel2.grid(row=3, column=0)

myLabel3 = Label(root, text="Product Development Assistant")
myLabel3.grid(row=3, column=2)

myLabel4 = Label(root, text=" ")
myLabel4.grid(row=1, column=1)

myButton = Button(root, text="ChatBot", command=open_chatbot_file)
myButton.grid(row=1, column=0)

myButton2 = Button(root, text="AI Product Development", command=open_ai_product_file)
myButton2.grid(row=1, column=2)

root.mainloop()
