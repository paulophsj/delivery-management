import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class ErrorView:
    error_key_view = "-ERROR_KEY_VIEW-"

    def __init__(self):
        pass

    def render(self, message):
        return sg.Column([
            [sg.Text(
                    message,
                    text_color="red",
                    font=("Arial", 16, "bold"),
                    justification="center",
                    expand_x=True
                )]
        ],key=self.error_key_view)