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
    def __init__(self, tkinstance, name):
        self.root = tkinstance
        self.name = name

        self.window = ttk.Frame(self.root, padding = '5 5 5 5', width = 200, height = 300)
        self.root.title('Upload Pictures')
        self.window.grid(column = 1, row = 1)
        text = "Hi " + str(name) + ',' + '\n' + 'choose a photo to upload'
        Label(self.window, text=text, font = ("Heveltica", 24)).grid(column=1, row=1, columnspan=2)

        self.Upload = ttk.Button(self.window, text = 'Upload', command = self.upload)
        self.Upload.grid(column = 1, row = 2)
        
        self.quit_ = ttk.Button(self.window, text = 'Quit', command = self.quit_)
        self.quit_.grid(column = 2, row = 2)


    def upload(self):
        filename = askopenfilename()
        print filename
        
    def quit_(self):
        quit()
        
