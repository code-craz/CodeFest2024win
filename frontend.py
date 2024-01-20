from tkinter import *

root = Tk()

myLabel = Label(root, text="Welcome to SSA")
myLabel.grid(row=0, column=1)

myLabel2 = Label(root, text="Customizible ChatBot for your website")
myLabel2.grid(row=3, column=0)

myLabel3 = Label(root, text="Product Development Assistant")
myLabel3.grid(row=3, column=2)

myLabel4 = Label(root, text=" ")
myLabel4.grid(row=1, column=0)

myButton = Button(root, text="ChatBot")
myButton.grid(row=1, column=0)

myButton2 = Button(root, text="AI Product Development")
myButton2.grid(row=1, column=2)

root.mainloop()