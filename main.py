# Kivy imports
from kivymd.app import MDApp
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch

# Project imports
from libs.uix.root import Root

# Remove multi click
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Other imports
from pyautogui import size

class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = False

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Title
        self.title = "Simple Password Manager"

        # Window size and pos
        self.sizex = 450
        self.sizey = 550
        Window.size = (self.sizex, self.sizey)
        Window.left = (size()[0] - self.sizex)/2
        Window.top = (size()[1] - self.sizey)/2

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

        # Color & Themes
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.05

    def open_settings(self, *largs):
        pass

    def build(self):
        self.root = Root()
        self.root.push("home")

if __name__ == "__main__":
    MainApp().run()
