from login_window_token import loginwindow
from Welcome_Window import mainwindow
from Upload_window import *
from Download_window import download_window
from Tkinter import *

class Switch:
    def __init__(self, *args):
        pass
        
    def run_download(self, *args):
        Down = download_window(*args)
        Down
        
    def run_welcome(self, *args):
        Main = mainwindow(*args)
        Main
        
    def run_login(self, *args):
        Window = loginwindow(*args)
        Window.run()

    def run_upload(self, *args):
        Up = uploadwindow(*args)
        Up
