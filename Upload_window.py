##Upload Window
from Tkinter import *
import ttk
import tkMessageBox
import os
import tkFont
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename
import facebook

class uploadwindow():
    """Represesnts the window to upload photos to Facebook"""
    def __init__(self, tkinstance, name, token, module):
        self.root = tkinstance
        self.name = name
        self.switch = module
        self.token = token
        self.draw_Window()

    def draw_Window(self):
        self.window = ttk.Frame(self.root, padding = '5 5 5 5', width = 200, height = 300)
        self.root.title('Upload Pictures')
        self.window.grid(column = 1, row = 1)
        text = "Hi " + str(self.name) + ',' + '\n' + 'choose a photo to upload'
        Label(self.window, text=text, font = ("Heveltica", 24)).grid(column=1, row=1, columnspan=3, sticky = (E,W))

        self.Browse = ttk.Button(self.window, text = 'Browse', command = self.browse)
        self.Browse.grid(column = 1, row = 2)

        self.return_ = ttk.Button(self.window, text = 'Return to main menu', command = self.mainmenu)
        self.return_.grid(column = 2, row = 2)
        
        self.quit_ = ttk.Button(self.window, text = 'Quit', command = self.quit_)
        self.quit_.grid(column = 3, row = 2)

    def draw_Preview(self):
        self.window1 = ttk.Frame(self.root, padding = '5 5 5 5', width = 200, height = 300)
        self.root.title('Upload Pictures')
        self.window1.grid()

        Title = Label(self.window1, text="Do you want to uplaod this photo?", font = ("Heveltica", 24))
        Title.grid(column=1, row=1, columnspan=3, sticky = (E,W))

        self.photo = Image.open(self.uploadfile) #The images are saved to the computer with a static name
        preview = ImageTk.PhotoImage(self.photo)
        self.p1 = ttk.Label(self.window1, image=preview)
        self.p1.image1 = preview
        self.p1.grid(column = 1, row = 2, columnspan = 3)        

        self.message = Label(self.window1, text = "Would you like to include a message", font = ("Heveltica", 18))
        self.message.grid(column = 1, row = 3, columnspan = 3)

        self.emessage = ttk.Entry(self.window1, width = 15)
        self.emessage.grid(column = 1, row = 4, columnspan = 3)
        
        self.Upload = ttk.Button(self.window1, text = 'Upload', command = self.upload)
        self.Upload.grid(column = 1, row = 5)
        
        self.return_ = ttk.Button(self.window1, text = 'Return to main menu', command = self.mainmenu1)
        self.return_.grid(column = 2, row = 5)
        
        self.quit_ = ttk.Button(self.window1, text = 'Quit', command = self.quit_)
        self.quit_.grid(column = 3, row = 5)

        self.root.bind('<Command-Key-q>', self.quit_)

    def browse(self):
        self.uploadfile = askopenfilename()
        if self.uploadfile:
            self.window.grid_forget()
            self.draw_Preview()
        
    def upload(self):
        self.caption = self.emessage.get()
        with open(self.uploadfile) as upload:
            graph = facebook.GraphAPI(self.token)
            message = str(self.caption)
            upload = graph.put_photo(upload, message)
            tkMessageBox.showinfo("Success!", "Your photo has been uploaded to Facebook! Make sure to approve it")

    def mainmenu(self):
        self.window.grid_forget()
        next_ = self.switch()
        next_.run_welcome(self.root, self.token, self.switch)

    def mainmenu1(self):
        self.window1.grid_forget()
        next_ = self.switch()
        next_.run_welcome(self.root, self.token, self.switch)

        
    def quit_(self):
        quit()
        
