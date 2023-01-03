from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDIconButton
#yt.streams.get_highest_resolution().download()
class Menu():
    def popup(self, app):
        menu_items = [
            {
                "text": "Ayarlar",
                "viewclass": "OneLineListItem",
                "on_press": lambda: self.settings(),
            },
            {
                "text": "İndirilenler",
                "viewclass": "OneLineListItem",
            },
            {
                "text": "Klasör Aç",
                "viewclass": "OneLineListItem",
                "on_press": lambda : self.folder(),
            },
        ]
        menu = MDDropdownMenu(
            caller=app.root.ids.button,
            items=menu_items,
            width_mult=4,
        ).open()

    def settings(self):
        popup = Popup(
            title="Ayarlar",
            content = MDBoxLayout(
                MDFloatLayout(
                    MDRaisedButton(
                        pos_hint = {"top":1},
                        md_bg_color = "red",


                    ),
                ),
            ),
        ).open()
