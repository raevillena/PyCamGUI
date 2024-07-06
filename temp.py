from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile

class myApp(tk.Frame):
    def __init__(self,root):
        self.root = root
        self.bg_menubar = '#fcfcfc'
        self.fg_menubar = 'BLACK'
        self.active_bg_menubar = '#dedede'
        self.active_fg_menubar = 'BLACK'
        self.bg_menus = '#f3f4f5'
        self.fg_menus = 'BLACK'
        self.active_bg_menus = '#bcdff2'
        self.active_fg_menus = 'BLACK'
        self.bg_app = '#1f1f1f'

        super().__init__(
            root,
            bg=self.bg_app
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=TRUE)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.create_menubar()

    def create_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        def donothing():
            print("nothing")

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_command(label="Save as...", command=donothing)
        self.filemenu.add_command(label="Close", command=donothing)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=donothing)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=donothing)
        self.editmenu.add_command(label="Copy", command=donothing)
        self.editmenu.add_command(label="Paste", command=donothing)
        self.editmenu.add_command(label="Delete", command=donothing)
        self.editmenu.add_command(label="Delete", command=donothing)
        self.editmenu.add_command(label="Select All", command=donothing)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

root = Tk()
root.title('Black Garlic Classification System')
root.geometry('800x600')
window = myApp(root)
root.mainloop()



def display():
   print("nothing")

def show():
   filename = askopenfile()
   print(filename)





frame = Canvas(master=root, bg="white", height=600, width=700)

button= ttk.Button(frame, text= "Open file", command = show)
button.pack(padx = 10, pady = 10, side = tk.LEFT)



root.config(menu=menubar)
frame.pack(padx = 5, pady = 5)
