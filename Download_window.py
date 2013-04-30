from Tkinter import *
import ttk
import tkMessageBox
import os
import tkFont
from PIL import Image, ImageTk
import facebook
import urllib


class download_window():
    """Window used to download photos from facebook"""
    def __init__(self, tkinstance, name, token, switch_module):
        self.root = tkinstance
        self.name = name
        self.token = token
        self.switch = switch_module
        self.count = 0
        self.refresh_pics(self.count)
        self.addCount() 

        
    def draw_Pics(self):
        """Draws pictures"""
        self.appwindow = ttk.Frame(self.root, padding = "5 5 5 5", width = 400, height = 500)
        self.root.title("Download Pictures")
        self.appwindow.grid()

        self.return_ = ttk.Button(self.appwindow, text="Return to Mainwindow", command = self.return_menu)
        self.return_.grid(column = 1, row = 3)

        self.refresh = ttk.Button(self.appwindow, text = "Refresh Photos", command = self.newPics)
        self.refresh.grid(column =2, row =3)

        self.quit_ = ttk.Button(self.appwindow, text = "Quit", command = self.quit_)
        self.quit_.grid(column =3, row =3)
        
        self.photo1 = Image.open('Down-1.jpg') #The images are saved to the computer with a static name
        self.photo1s = self.photo1.resize( [int(.5 * s) for s in self.photo1.size] ) #Original file size is too big, must resize
        preview1 = ImageTk.PhotoImage(self.photo1s)
        self.p1 = ttk.Label(self.appwindow, image=preview1)
        self.p1.image1 = preview1
        self.p1.grid(column = 1, row = 1)
        self.photol1 = ttk.Label(self.appwindow, text = 'Photo 1')
        self.photol1.grid(column = 1, row = 2)

        self.photo2 = Image.open('Down-2.jpg')
        self.photo2s = self.photo2.resize( [int(.5 * s) for s in self.photo2.size] )
        preview2 = ImageTk.PhotoImage(self.photo2s)
        self.p2 = ttk.Label(self.appwindow, image=preview2)
        self.p2.image2 = preview2
        self.p2.grid(column = 2, row = 1)
        self.photol2 = ttk.Label(self.appwindow, text = 'Photo 2')
        self.photol2.grid(column = 2, row = 2)

        self.photo3 = Image.open('Down-3.jpg')
        self.photo3s = self.photo3.resize( [int(.5 * s) for s in self.photo3.size] )
        preview3 = ImageTk.PhotoImage(self.photo3s)
        self.p3 = ttk.Label(self.appwindow, image = preview3)
        self.p3.image3 = preview3
        self.p3.grid(column = 3, row = 1)
        self.photol3 = ttk.Label(self.appwindow, text = 'Photo 3')
        self.photol3.grid(column = 3, row = 2)
        
       

    def refresh_pics(self, count):
        """Mechanism that actually makes call to facebook for the photos"""
        graph = facebook.GraphAPI(self.token)
        profile = graph.get_object('me')
        photos = graph.get_connections("me", "photos")

        pic1 = photos['data'][count]['source'] #Parse the URL for each picture
        urllib.urlretrieve(pic1, "Down-1.jpg") #Download the URL for each picture (note static name)

        pic2 = photos['data'][count+1]['source']
        urllib.urlretrieve(pic2, "Down-2.jpg")

        pic3 = photos['data'][count+2]['source']
        urllib.urlretrieve(pic3, "Down-3.jpg")

        self.draw_Pics()

    def newPics(self):
        """Get's rid of window so that new pics can be retrieved"""
        self.appwindow.destroy()
        self.refresh_pics(self.count)
        self.addCount()
        
    def return_menu(self):
        """Returns back to main window"""
        self.appwindow.grid_forget()
        Next = self.switch()
        Next.run_welcome(self.root, self.token, self.switch)

    def addCount(self):
        """Allows the app to walk through the JSON response object and get new photos each time by increasing the index"""
        self.count += 3
    
    def quit_(self):
        quit()
        
