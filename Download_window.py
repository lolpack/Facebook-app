from Tkinter import *
from Welcome_Window import *
from login_window import *
import ttk
import tkMessageBox
import os
import tkFont
from PIL import Image, ImageTk

class download_window():
    """Window used to download photos from facebook"""
    def __init__(self, tkinstance, name):
        self.root = tkinstance
        self.name = name


        self.appwindow = ttk.Frame(self.root, padding = "5 5 5 5", width = 400, height = 500)
        self.root.title("Download Pictures")
        self.appwindow.grid()

        self.photo1 = Image.open('Dummy_photo1.jpg')
        preview1 = ImageTk.PhotoImage(self.photo1)
        self.p1 = ttk.Label(self.appwindow, image=preview1)
        self.p1.grid(column = 1, row = 1)
        self.photol1 = ttk.Label(self.appwindow, text = 'Photo 1')
        self.photol1.grid(column = 1, row = 2)

        self.photo2 = Image.open('Dummy_photo1.jpg')
        preview2 = ImageTk.PhotoImage(self.photo2)
        self.p2 = ttk.Label(self.appwindow, image=preview2)
        self.p2.grid(column = 2, row = 1)
        self.photol2 = ttk.Label(self.appwindow, text = 'Photo 2')
        self.photol2.grid(column = 2, row = 2)

        self.photo3 = Image.open('Dummy_photo1.jpg')
        preview3 = ImageTk.PhotoImage(self.photo3)
        self.p3 = ttk.Label(self.appwindow, image = preview3)
        self.p3.grid(column = 3, row = 1)
        self.photol3 = ttk.Label(self.appwindow, text = 'Photo 3')
        self.photol3.grid(column = 3, row = 2)

        self.return_ = ttk.Button(self.appwindow, text="Return to Mainwindow", command = self.return_menu)
        self.return_.grid(column = 1, row = 3)

        self.refresh = ttk.Button(self.appwindow, text = "Refresh Photos", command = self.refresh_pics)
        self.refresh.grid(column =2, row =3)

        self.quit_ = ttk.Button(self.appwindow, text = "Quit", command = self.quit_)
        self.quit_.grid(column =3, row =3)

    def refresh_pics(self):
        pass

    def return_menu(self):
        #self.appwindow.destroy()
        #mainwindow(self.root)
        pass
    
    def quit_(self):
        quit()
        
