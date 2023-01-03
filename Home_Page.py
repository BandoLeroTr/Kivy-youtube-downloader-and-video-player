from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from Menu.menu import Menu
from Downloader.download import Download

class Home_Page(Screen):
    Builder.load_file("Pages/Home_Page.kv")
    xMenu = Menu()
    xDownload = Download()

    def selected(self, filename):
        global path
        for path in filename:
            self.video.source = path
            print(path)


