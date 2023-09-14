from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from kivymd.uix.button import MDIconButton
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import TwoLineListItem

class EditButton(MDIconButton, ButtonBehavior):
    pass

class HomeScreen(Screen):
    def __init__(self):
        super().__init__()

        self.app = MDApp.get_running_app()

    def add_item(self):
        item_text = self.ids.item_input.text.strip()
        if item_text:
            item = TwoLineListItem(
                id=item_text,
                text=item_text,
                secondary_text="Password",
                on_release=lambda _: self.goto('edit'),
            )
            self.ids.item_list.add_widget(item)
            self.ids.item_input.text = ""

    def edit_item(self, item):
        self.ids.item_input.text = item.text
    
    def goto(self, screen, side='left'):
        self.manager.push(screen, side)
