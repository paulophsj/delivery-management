import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")


class IndexView:
    index_key_view = "-INDEX_VIEW-"
    index_btn_start_client = "-INDEX_BTN_START_CLIENT-"
    index_btn_start_admin = "-INDEX_BTN_START_ADMIN-"

    def __init__(self):
        pass

    def render(self):
        return sg.Column([
            [sg.Text(
                "🍔",
                font=(None, 37),
                text_color="Brown",
                justification="center",
                expand_x=True
            )],

            [sg.Text(
                "Hamburgueria",
                font="Arial 18 bold",
                text_color="Brown",
                justification="center",
                expand_x=True
            )],

            [sg.Text(
                "Gerenciador",
                font="Arial 10",
                text_color="Black",
                justification="center",
                expand_x=True
            )],

            [sg.HorizontalSeparator(
                color="Orange",
                pad=((60, 60), (10, 10))
            )],

            [sg.Text(
                "Selecione abaixo o seu perfil de acesso para continuar",
                justification="center"
            )],

            [sg.Button(
                "Cliente",
                font="Arial 15",
                border_width=0,
                button_color=("White", "Brown"),
                key=self.index_btn_start_client,
                expand_x=True
            )],

            [sg.Button(
                "Administrador",
                font="Arial 15",
                border_width=0,
                button_color=("White", "#420B09"),
                key=self.index_btn_start_admin,
                expand_x=True
            )]
        ], key=self.index_key_view, expand_y=True)
