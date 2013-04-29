##Upload Window
from Tkinter import *
import ttk
import tkMessageBox
import os
import tkFont
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename

class uploadwindow():
    """Represesnts the window to upload photos to Facebook"""
    def __init__(self, tkinstance, name, token, module):
        self.root = tkinstance
        self.name = name
        self.switch = module
        self.token = token

        self.window = ttk.Frame(self.root, padding = '5 5 5 5', width = 200, height = 300)
        self.root.title('Upload Pictures')
        self.window.grid(column = 1, row = 1)
        text = "Hi " + str(name) + ',' + '\n' + 'choose a photo to upload'
        Label(self.window, text=text, font = ("Heveltica", 24)).grid(column=1, row=1, columnspan=3, sticky = (E,W))

        self.Upload = ttk.Button(self.window, text = 'Browse', command = self.upload)
        self.Upload.grid(column = 1, row = 2)

        self.return_ = ttk.Button(self.window, text = 'Return to main menu', command = self.mainmenu)
        self.return_.grid(column = 2, row = 2)
        
        self.quit_ = ttk.Button(self.window, text = 'Quit', command = self.quit_)
        self.quit_.grid(column = 3, row = 2)


    def upload(self):
        filename = askopenfilename()
        print filename

    def mainmenu(self):
        self.window.grid_forget()
        next_ = self.switch()
        next_.run_welcome(self.root, self.token, self.switch)
        
    def quit_(self):
        quit()
        
