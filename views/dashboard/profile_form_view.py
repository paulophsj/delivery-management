import PySimpleGUI as sg

from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")


class ProfileFormView:
    profile_input_nome = "-PROFILE_INPUT_NOME-"
    profile_input_senha = "-PROFILE_INPUT_SENHA-"
    profile_btn_salvar = "-PROFILE_BTN_SALVAR-"
    profile_btn_cancelar = "-PROFILE_BTN_CANCELAR-"

    @staticmethod
    def open(user):
        """Formulário modal para editar nome e senha.
        Retorna {'name', 'senha'} ou None caso o usuário cancele/feche."""
        user = user or {}

        layout = [
            [sg.Text("Gerenciar Perfil", font=("Arial", 16, "bold"), pad=(0, (0, 12)))],

            [sg.Text(f"E-mail: {user.get('email', '')}", font=("Any", 10))],

            [sg.Text("Nome", pad=(0, (8, 4)))],
            [sg.Input(user.get("name", ""),
                      key=ProfileFormView.profile_input_nome, size=(38, 1))],

            [sg.Text("Senha", pad=(0, (8, 4)))],
            [sg.Input(user.get("senha", ""), password_char="•",
                      key=ProfileFormView.profile_input_senha, size=(38, 1))],

            [
                sg.Push(),
                sg.Button("Salvar", key=ProfileFormView.profile_btn_salvar,
                          button_color=("White", "Brown"), border_width=0,
                          font="Arial 12 bold", pad=((0, 8), (16, 0))),
                sg.Button("Cancelar", key=ProfileFormView.profile_btn_cancelar,
                          button_color=("White", "#420B09"), border_width=0,
                          font="Arial 12 bold", pad=(0, (16, 0)))
            ]
        ]

        window = sg.Window("Gerenciar Perfil", layout, modal=True, finalize=True,
                           element_justification="left")

        resultado = None

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, ProfileFormView.profile_btn_cancelar):
                break

            if event == ProfileFormView.profile_btn_salvar:
                nome = values[ProfileFormView.profile_input_nome].strip()
                senha = values[ProfileFormView.profile_input_senha].strip()

                if not all([nome, senha]):
                    sg.popup_error("Nome e senha são obrigatórios.")
                    continue

                resultado = {"name": nome, "senha": senha}
                break

        window.close()
        return resultado
