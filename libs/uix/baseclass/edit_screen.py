from kivy.uix.screenmanager import Screen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield.textfield import MDTextField
from kivy.properties import StringProperty

import re

class CredInputPL(MDTextField):
    def insert_text(self, substring, from_undo=False):
        password_valid = r'^[A-Za-z\d@$!%*#?&]$'
        s = substring
        if substring == '\n':
            s = ""
        if len(self.text) > 64:
            s = ""
        if not re.match(password_valid, substring):
            s = ""
        return super().insert_text(s, from_undo=from_undo)
    
class PasswordTextFieldL(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class EditScreen(Screen):
    name = ""
    email = ""
    password = ""

    def save_data(self):
        # Retrieve data from the text fields
        self.name = self.ids.name_field.text
        self.email = self.ids.email_field.text
        self.password = self.ids.password_field.ids.text.text

        print(self.name)
        print(self.email)
        print(self.password)
