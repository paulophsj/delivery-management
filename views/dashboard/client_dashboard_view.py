import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class ClientDashboardView:
    dashboard_client_key_view = "-DASHBOARD_CLIENT_KEY_VIEW-"
    dashboard_client_btn_novo_pedido = "-DASHBOARD_CLIENT_BTN_NOVO_PEDIDO-"
    dashboard_client_btn_perfil = "-DASHBOARD_CLIENT_BTN_PERFIL-"
    dashboard_client_txt_nome = "-DASHBOARD_CLIENT_TXT_NOME-"

    def __init__(self):
        pass

    def render(self):

        header = [
            [sg.Column([
                [sg.Text(f"{self.dashboard_client_txt_nome}",
                         font="Arial 18 bold",
                         pad=(0, (0, 4)),
                         key=self.dashboard_client_txt_nome)],
                [sg.Text("O que deseja fazer hoje?", pad=(0, (0, 24)))]
            ],
                element_justification = "center", expand_x = True)]
        ]

        btn_size = (20, 5)
        btn_font = "Arial 13 bold"
        btn_color = ("White", "Brown")

        botoes = [
            [
                sg.Button("🍔\nFazer um\nNovo Pedido",
                          key=self.dashboard_client_btn_novo_pedido,
                          size=btn_size,
                          font=btn_font,
                          button_color=btn_color,
                          pad=(12, 0)),
                sg.Button("👤\nGerenciar\nPerfil",
                          key=self.dashboard_client_btn_perfil,
                          size=btn_size,
                          font=btn_font,
                          button_color=btn_color,
                          pad=(12, 0)),
            ]
        ]

        card_layout = header + botoes

        return sg.Column(
            [[sg.Frame(
                "",
                card_layout,
                pad=(32, 32),
                relief=sg.RELIEF_FLAT,
                border_width=1,
            )]],
            key=self.dashboard_client_key_view,
            element_justification="center",
            expand_y=True,
            expand_x=True,
            visible=False,
        )