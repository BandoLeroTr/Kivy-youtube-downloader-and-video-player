from kivymd.app import MDApp
from kivy.core.window import Window
from Home_Page import Home_Page

Window.size = (1200, 700)

class Main(MDApp):
    def build(self):
        return Home_Page()

Main().run()
