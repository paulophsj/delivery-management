import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class RegisterView:
    register_key_view = "-REGISTER_VIEW-"

    def __init__(self):
        pass