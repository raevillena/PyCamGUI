import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile

root = tk.Tk()
frame= ttk.Frame(root,height=600,width=800)

def increment():
   progressBar.step(20)
   
def decrement():
   progressBar.step(-20)
   
def display():
   print(progressBar["value"])

def show():
   filename = askopenfile()
   print(filename)

C = Canvas(root, bg="white", height=600, width=700)

progressBar= ttk.Progressbar(frame, mode='determinate')
progressBar.pack(padx = 10, pady = 10)

button= ttk.Button(frame, text= "Open file", command = show)
button.pack(padx = 10, pady = 10, side = tk.LEFT)

button= ttk.Button(frame, text= "Capture Image", command = decrement)
button.pack(padx = 10, pady = 10, side = tk.LEFT)

button= ttk.Button(frame, text= "Classify", command = display)
button.pack(padx = 10, pady = 10, side = tk.LEFT)

label = ttk.Label(frame, text = "Classification: ")
label.pack(padx = 5)

label = ttk.Label(frame, text = "N/A")
label.pack(padx = 5)

frame.pack(padx = 5, pady = 5)
root.mainloop()