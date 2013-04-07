from Tkinter import *
from Welcome_Window import *
import ttk
import tkMessageBox
import os
from PIL import Image, ImageTk




        
class loginwindow():
    """This is the login window. This authenticates the username9 and password with Facebook"""
    def authenticate(self, *args):
        if str(self.usrn.get()) == "Username":
            if str(self.pasw.get()) == "Password":
                self.launchwindow()
        else:
            self.root.bell()
            tkMessageBox.showinfo("Login Failed", "The Username and Password combination you entered is incorrect")

    def launchwindow(self):
        self.mainframe.destroy()
        mainwindow(self.root)

            
    def rememberpass(self, *args):
        output = "Username:" + str(self.usrn.get()) + '\n' + "Password:" + str(self.pasw.get())
        passfile = open('login_info.txt', 'w')
        passfile.write(output)
        passfile.close



    def savedpass(self):
        if os.path.isfile('login_info.txt'):
            savedpass = open('login_info.txt', 'r')
            Uname = savedpass.readline()
            Pword = savedpass.readline()
            Uname.lstrip('Username:')
            Pword.lstrip('Password:')
            if Uname == 'Username':
                if Pword == 'Password':
                    self.launchwindow()
            else:
                self.root.bell()
                tkMessageBox.showinfo("Login Failed", "The saved Username and Password is incorrect. Please enter Username and Password below")
                #self.authenticate()
        else:
            self.authenticate()



    def __init__(self, tkinstance):
       
        self.root = tkinstance
        self.mainframe = ttk.Frame(self.root, relief = "ridge", padding= "5 5 5 5")
        self.root.title("Facebook Login")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.usrn = ttk.Entry(self.mainframe, width=9)
        self.usrn.grid(column=1, row=1, sticky=(W, E))

        self.pasw = ttk.Entry(self.mainframe, width=9, show="*")
        self.pasw.grid(column=1, row=2, sticky=(W, E))

        self.fb = Image.open('icon_fb.png')
        photo = ImageTk.PhotoImage(self.fb)
        self.fb = ttk.Label(self.mainframe, image=photo)
        self.fb.image = photo
        self.fb.grid(column=3, row=1, rowspan=2)

        rempass = Checkbutton(self.mainframe, text= "Remember Password", command=self.rememberpass)
        rempass.grid(column=1, row=3, sticky=W)

        button = ttk.Button(self.mainframe, text="Login", command=self.savedpass).grid(column=3, row=3, sticky=S)

        Label(self.mainframe, text="Username").grid(column=2, row=1, sticky=E)
        Label(self.mainframe, text="Password").grid(column=2, row=2, sticky=E)

        self.quit = ttk.Button(self.mainframe, text = 'Quit', command=self.quit_)
        self.quit.grid(column= 3, row=4, sticky = (S,E))
        
        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.usrn.focus()
        self.root.bind('<Return>', self.authenticate)

        
    def run(self):
        self.root.mainloop()

    def quit_(self):
        quit()
