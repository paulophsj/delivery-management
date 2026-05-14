import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class RegisterView:
    register_key_view = "-REGISTER_KEY_VIEW-"
    register_input_senha = "-REGISTER_INPUT_SENHA-"
    register_input_email = "-REGISTER_INPUT_EMAIL-"
    register_input_confirmar_senha = "-REGISTER_INPUT_CONFIRMAR_SENHA-"
    register_input_nome = "-REGISTER_INPUT_NOME-"
    register_btn_signup = "-REGISTER_BTN_SIGNUP-"

    def __init__(self):
        pass

    def render(self):

        header = [
            [sg.Text(
                "Crie sua conta",
                pad=(0, (0, 2))
            )],
            [sg.Text(
                "Preencha os dados para se cadastrar",
                pad=(0, (0, 16))
            )],
        ]

        form = [
            [sg.Text("Nome", pad=(0, (0, 4)))],
            [sg.Input(
                key=self.register_input_nome,
                size=(32, 1),
                enable_events=True,
                expand_x=True,
            )],

            [sg.Text("E-mail", pad=(0, (0, 4)))],
            [sg.Input(
                key=self.register_input_email,
                size=(32, 1),
                enable_events=True,
                expand_x=True,
            )],

            [sg.Text("Senha", pad=(0, (0, 4)))],
            [sg.Input(
                password_char="•",
                key=self.register_input_senha,
                enable_events=True,
                size=(32, 1),
                expand_x=True,
            )],

            [sg.Text("Confirmar senha", pad=(0, (0, 4)))],
            [sg.Input(
                password_char="•",
                key=self.register_input_confirmar_senha,
                enable_events=True,
                size=(32, 1),
                expand_x=True,
            )],
        ]

        btn_row = [
            [sg.Button(
                "  Cadastrar  ",
                key=self.register_btn_signup,
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
            key=self.register_key_view,
            element_justification="center",
            expand_y=True,
            expand_x=True,
            visible=False,
        )