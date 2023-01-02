import threading, os, time
from pytube import YouTube
from multiprocessing import Process
from threading import Thread
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
#yt.streams.get_highest_resolution().download()
class Download():
    def test(self, app):
        menu_items = [
            {
                "text": "Müzik indir.",
                "viewclass": "OneLineListItem",
                "on_press": lambda : self.download_music_process(app),
            },
            {
                "text": "Video indir.",
                "viewclass": "OneLineListItem",
                "on_press": lambda : self.download_video_process(app),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=app.root.ids.download,
            items=menu_items,
            width_mult=2,
        )
        self.menu.open()

    def download_music_process(self, app):
        global url
        url = app.root.ids.url_text.text
        x = Process(target = self.download_music)
        x.start()

    def download_video_process(self, app):
        global url
        url = app.root.ids.url_text.text
        a = Process(target = self.download_video)
        a.start()

    def download_music(self):
        print("müzik_indirme_başladı")
        yt = YouTube(url)
        yt.streams.get_audio_only().download()
        print("müzik_indirme_bitti")

    def download_video(self):
        print("video_indirme_başladı")
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download()
        print("video_indirme_bitti")
