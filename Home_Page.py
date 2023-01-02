from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import PIL
from menu.menu import Menu
from download.download import Download
user_name = os.getlogin()

class Home_Page(Screen):
    Builder.load_file("screens/Home_Page.kv")
    xMenu = Menu()
    xDownload = Download()

    def selected(self, filename):
        global path
        for path in filename:
            self.video.source = path
            print(path)


