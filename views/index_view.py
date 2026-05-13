import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")


class IndexView:
    index_key_view = "-INDEX_VIEW-"
    index_btn_login = "-INDEX_BTN_LOGIN-"
    index_btn_cadastro = "-INDEX_BTN_CADASTRO-"

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
                "Login",
                font="Arial 15",
                border_width=0,
                button_color=("White", "Brown"),
                key=self.index_btn_login,
                expand_x=True
            )],

            [sg.Button(
                "Cadastro",
                font="Arial 15",
                border_width=0,
                button_color=("White", "#420B09"),
                key=self.index_btn_cadastro,
                expand_x=True
            )]
        ], key=self.index_key_view, expand_y=True)
