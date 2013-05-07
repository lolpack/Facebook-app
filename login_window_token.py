from Tkinter import *
import ttk
import os
from PIL import Image, ImageTk
import facebook
import webbrowser


        
class loginwindow():

    def __init__(self, tkinstance, switch_module):
        """Creates global variable for tkinstance and switch module. Draws loginwindow"""
        self.tkinstance = tkinstance
        self.draw_window()
        self.switch = switch_module

    def launchwindow(self):
        """When called it destorys this window and runs the main welcome window"""
        token = str(self.token.get())
        self.mainframe.destroy()
        next_window = self.switch()
        next_window.run_welcome(self.root, token, self.switch)
        
    def openurl(self):
        """Opens a web browser to the Facebook developer page (for convience) will hopefully be replaced by a more user friendly
        feature that can just take the user name and password"""
        webbrowser.open("https://developers.facebook.com/tools/explorer")


    def draw_window(self):
        """Draws the GUI itself"""
        self.root = self.tkinstance
        self.mainframe = ttk.Frame(self.root, relief = "ridge", padding= "5 5 5 5") #Creates mainframe object with a little style
        self.root.title("Facebook Login")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) 
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.token = ttk.Entry(self.mainframe, width=20)
        self.token.grid(column=2, row=2, sticky=(W, E))


        self.fb = Image.open('icon_fb.png')
        photo = ImageTk.PhotoImage(self.fb)
        self.fb = ttk.Label(self.mainframe, image=photo)
        self.fb.image = photo 
        self.fb.grid(column=3, row=1, rowspan=2)

        button = ttk.Button(self.mainframe, text="Get Photos!", command=self.launchwindow).grid(column=1, row=3, sticky=S)

        Label(self.mainframe, text="Access_Token").grid(column=1, row=2, sticky=E)
        launchwebsite = ttk.Button(self.mainframe, text="Get your access token from Facebook", command = self.openurl)
        launchwebsite.grid(column=1, row=1, columnspan = 2, sticky=E)

        self.quit = ttk.Button(self.mainframe, text = 'Quit', command=self.quit_)
        self.quit.grid(column= 3, row=3, sticky = (S,E))
        
        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.token.focus()
        self.root.bind('<Return>', self.launchwindow)

        
    def run(self):
        self.root.call('wm', 'attributes', '.', '-topmost', '1') #forces tk frame to be top window
        self.root.call('wm', 'attributes', '.', '-topmost', '0')
        self.root.mainloop() #runs mainloop for the app

    def quit_(self):
        quit()
