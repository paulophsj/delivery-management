import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class LoginView:
    login_key_view = "-LOGIN_KEY_VIEW-"
    login_input_email = "-LOGIN_INPUT_EMAIL-"
    login_input_senha = "-LOGIN_INPUT_SENHA-"
    login_btn_signin = "-LOGIN_BTN_SIGNIN-"

    def __init__(self):
        pass

    def render(self):

        header = [
            [sg.Text("Bem-vindo",
                     pad=(0, (0, 2)))],
            [sg.Text("Acesse sua conta para continuar",
                     pad=(0, (0, 16)))],
        ]

        form = [
            [sg.Text("E-mail", pad=(0, (0, 4)))],
            [sg.Input(
                key=self.login_input_email,
                size=(32, 1),
                enable_events=True,
                expand_x=True,
            )],
            [sg.Text("Senha", pad=(0, (0, 4)))],
            [sg.Input(
                password_char="•",
                key=self.login_input_senha,
                enable_events=True,
                size=(32, 1),
                expand_x=True
            )],
        ]

        btn_row = [
            [sg.Button(
                "  Entrar  ",
                key=self.login_btn_signin,
                size=(28, 1),
                font="Arial 15",
                button_color=("White", "Brown"),
                border_width=1,
                pad=(0, (40, 12)),
            )]
        ]

        card_layout = header + form + btn_row

        return sg.Column(
            [[sg.Frame(
                "",
                card_layout,
                pad=(24, 24),
                relief=sg.RELIEF_FLAT,
                border_width=1,
            )]],
            key=self.login_key_view,
            element_justification="center",
            expand_y=True,
            expand_x=True,
            visible=False,
        )