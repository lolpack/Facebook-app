from Tkinter import *
from Upload_window import *
from Download_window import *
import ttk
import tkMessageBox
import os
import tkFont
from PIL import Image, ImageTk

class mainwindow():
    """This is the welcome window where the user can choose to upload, download or sign out"""
    def __init__(self, tkinstance):
        self.root = tkinstance
        self.name = 'Steve' # This is a dummy name. Will be grabbed from Facebook


        
        
        self.appwindow = ttk.Frame(self.root, padding = "5 5 5 5", width = 400, height = 500)
        self.root.title("Facebook Pictures")
        self.appwindow.grid(column = 0, row = 0, sticky=(N,W,E,S))
        Label(self.appwindow, text="Welcome " + str(self.name), font = ("Heveltica", 24)).grid(column=1, row=1, columnspan=2)

        self.uparwpic = Image.open('arrow-right.png')
        photo_up = ImageTk.PhotoImage(self.uparwpic)
        self.uploadarrow = ttk.Label(self.appwindow, image=photo_up)
        self.uploadarrow.image = photo_up
        self.uploadarrow.grid(column=1, row=2)
        self.uploadbut = ttk.Button(self.appwindow, text="Upload", command=self.upload)
        self.uploadbut.grid(column = 1, row=3, sticky=(E,W))
        
        
        self.downarw = Image.open('arrow-Down.png')
        photo_down = ImageTk.PhotoImage(self.downarw)
        self.downloadarrow = ttk.Label(self.appwindow, image=photo_down)
        self.downloadarrow.image = photo_down
        self.downloadarrow.grid(column=2, row=2)
        self.downloadbut = ttk.Button(self.appwindow, text="Download", command=self.download)
        self.downloadbut.grid(column = 2, row=3, sticky=(E,W))

        self.quit = ttk.Button(self.appwindow, text = 'Quit', command=self.quit_)
        self.quit.grid(column= 1, row=4, columnspan = 2)
        
        self.root.bind('<Command-Key-q>', self.quit_)
        

    def upload(self):
        """Post's pictures to facebook"""
        self.appwindow.destroy()
        uploadwindow(self.root, self.name)
        
        

    def download(self):
        """Downloads pictures from facebook"""
        self.appwindow.destroy()
        download_window(self.root, self.name)

    def quit_(self):
        quit()
    
