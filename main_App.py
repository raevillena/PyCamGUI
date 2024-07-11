from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil

from main_classify import *
from main_capture import *

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

        def donothing():
            filewin = tk.Toplevel(self)
            label = tk.Label(filewin, text="This software is not in anyway sold to anyone and serves as")
            label.pack()
            label = tk.Label(filewin, text="academic requirement only for MSCPE program in MAPUA University")
            label.pack()
            label = tk.Label(filewin, text="Written by Raymart O. Villena")
            label.pack()
            label = tk.Label(filewin, text="email:raymart.o.villena@gmail.com")
            label.pack()
            print("nionoe")

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
      
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    shared_file_path = ""
    future_delete = False

    def create_buttons(self):
        home_dir = "/home/admin/PyCamGUI"
        def open_image():
            file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
            if file_path:
                display_image(file_path)
                global shared_file_path
                global future_delete
                shared_file_path = file_path
                future_delete = False
                classify_pls()

        def display_image(file_path):
            image = Image.open(file_path)
            zoom = 0.10
            pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
            photo = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
            image_label.config(image=photo)
            image_label.photo = photo
            status_label.config(text=f"Image loaded: {file_path}")
            image_label.grid(row=1, column=0, padx=10, pady=2)

        def classify_pls():
            pred_label,pred_accuracy,time = classify(shared_file_path)
            classification.set(f"Classification: {pred_label}, with Accuracy: {np.round(pred_accuracy, 2)}% in {time}sec.")


        def save_pls():
            shutil.copyfile(shared_file_path, home_dir+'/saved_images/'+classification.get()+'.jpg')
            classification.set(f"Saved in saved_images folder!")

        def exit_pls():
            global future_delete
            try:
                if future_delete:
                    os.remove(shared_file_path)
            except:
                exit()
            try:
                cam_stop()
            except:
                exit()
            exit()

        def capture_pls():
            global shared_file_path
            cam_preview()
            file_path = cam_capture_file(peeled=False,wait_time=1)
            display_image(file_path)
            shared_file_path = file_path
            classify_pls()
            cam_stop()
            global future_delete
            future_delete = True

        def capture_pls_peeled():
            global shared_file_path
            cam_preview()
            file_path = cam_capture_file(peeled=True,wait_time=1)
            display_image(file_path)
            shared_file_path = file_path
            classify_pls()
            cam_stop()
            global future_delete
            future_delete = True

        def preview_pls():
            cam_preview_show()
            time.sleep(10)
            cam_stop()

        classification = StringVar()

        frm_image = tk.Frame(self.root, relief="ridge", width=800, height=300, background="#d1e3ff", padx=155)
        image_label = tk.Label(frm_image, textvariable = classification , compound="top", pady=10)

        status_label = tk.Label(self.root, text="Please open or capture image first.", padx=10, pady=1)
        
        frm_buttons = tk.Frame(self.root, relief=tk.RAISED, bd=2)
        
        button_open = tk.Button(frm_buttons, text= "Open file", command = open_image)
        button_preview = tk.Button(frm_buttons, text= "Preview", command = preview_pls)
        button_capture= tk.Button(frm_buttons, text= "Capture UnPeeled", command = capture_pls)
        button_capture_peeled = tk.Button(frm_buttons, text= "Capture Peeled", command = capture_pls_peeled)
        button_save= tk.Button(frm_buttons, text= "Save", command = save_pls)
        button_exit= tk.Button(frm_buttons, text= "Exit", command = exit_pls)

        button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        button_preview.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        button_capture.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        button_capture_peeled.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
        button_save.grid(row=0, column=4, sticky="ew", padx=5, pady=5)
        button_exit.grid(row=0, column=5, sticky="w", padx=5, pady=5)

        status_label.grid(row=0, column=0)
        frm_image.grid(row=1, column=0)
        frm_buttons.grid(row=2, column=0)

root = Tk()
root.title('Black Garlic Classification System')
root.resizable(False,False)
window = myApp(root)
root.mainloop()