import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class LoginView:
    login_key_view = "-LOGIN_VIEW-"

    def __init__(self):
        pass

    def render(self):
        return sg.Column([
            [sg.Text("LOGIN PAGE")]
        ], key=self.login_key_view, expand_y=True, visible=False)