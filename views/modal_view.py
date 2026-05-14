import PySimpleGUI as sg
from config import white_theme
from enums.modal_type_enum import ModalType

sg.theme_add_new("White", white_theme)
sg.theme("White")

class ModalView:
    modal_key_view = "-MODAL_KEY_VIEW-"

    def __init__(self):
        pass

    def render(self, message: str, type: ModalType):
        return sg.Column([
            [sg.Text(
                    message,
                    text_color=(
                        "green" if type.value == ModalType.SUCESSO.value 
                        else "red" if type.value == ModalType.ERRO.value 
                        else "gray"),
                    font=("Arial", 16, "bold"),
                    justification="center",
                    expand_x=True
                )]
        ],key=self.modal_key_view)