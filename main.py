import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile

root = tk.Tk()
#frame= ttk.Frame(root,height=600,width=800)
frame = Canvas(root, bg="white", height=600, width=700)


def display():
   print("nothing")

def show():
   filename = askopenfile()
   print(filename)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

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