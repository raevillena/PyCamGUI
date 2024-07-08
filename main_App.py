from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from PIL import Image, ImageTk

from main_classify import *

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
        self.bg_app = '#adadad'

        super().__init__(
            root,
            bg=self.bg_app
        )

        self.main_frame = self
        self.main_frame.grid(column=0, row=0)
        self.main_frame.columnconfigure(0, minsize=30, weight=1)
        self.main_frame.rowconfigure(0, minsize=40, weight=1)
        self.main_frame.rowconfigure(1, minsize=40, weight=1)

        self.create_menubar()
        self.create_buttons()

    def create_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        def donothing(self):
            #filewin = tk.Toplevel(self)
            #button = tk.Button(filewin, text="Do nothing button")
            #button.pack()
            print("nionoe")

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

    shared_file_path=""
    
    def create_buttons(self):
        
        def open_image():
            file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
            if file_path:
                display_image(file_path)
                global shared_file_path
                shared_file_path = file_path

        def display_image(file_path):
            image = Image.open(file_path)
            zoom = 0.12
            pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
            photo = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
            image_label.config(image=photo)
            image_label.photo = photo
            status_label.config(text=f"Image loaded: {file_path}")
            image_label.grid(row=1, column=0, padx=10, pady=2)

        def classify_pls(self):
            pred_label,pred_accuracy = classify(shared_file_path)
            classification.set("Classification: ", pred_label, ", with Accuracy :", np.round(pred_accuracy*100, 2), "%.")

        classification = "No Image Loaded"

        frm_image = tk.Frame(self.root, relief="ridge", width=500, height=300, background="#d1e3ff")
        image_label = tk.Label(frm_image, textvariable = classification , compound="center")

        status_label = tk.Label(self.root, text="Please open or capture image first.", padx=10, pady=1)
        
        frm_buttons = tk.Frame(self.root, relief=tk.RAISED, bd=2)

        button_open = tk.Button(frm_buttons, text= "Open file", command = open_image)
        button_capture= tk.Button(frm_buttons, text= "Capture Image", command = open_image)
        button_classify= tk.Button(frm_buttons, text= "Classify", command = classify_pls)

        button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        button_capture.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        button_classify.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        status_label.grid(row=0, column=0)
        frm_image.grid(row=1, column=0)
        frm_buttons.grid(row=2, column=0)

root = Tk()
root.title('Black Garlic Classification System')
#root.geometry('600x400')
window = myApp(root)
root.mainloop()