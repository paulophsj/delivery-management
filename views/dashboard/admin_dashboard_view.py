import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class AdminDashboardView:
    dashboard_admin_key_view = "-DASHBOARD_ADMIN_KEY_VIEW-"
    dashboard_admin_btn_pedidos = "-DASHBOARD_ADMIN_BTN_PEDIDOS-"
    dashboard_admin_btn_cardapio = "-DASHBOARD_ADMIN_BTN_CARDAPIO-"
    dashboard_admin_btn_perfil = "-DASHBOARD_ADMIN_BTN_PERFIL-"
    dashboard_admin_txt_nome = "-DASHBOARD_ADMIN_TXT_NOME-"
    dashboard_admin_txt_saldo = "-DASHBOARD_ADMIN_TXT_SALDO-"

    def __init__(self):
        pass

    def render(self):

        header = [
            [sg.Column([
                [sg.Text(f"{self.dashboard_admin_txt_nome}",
                         font="Arial 18 bold",
                         pad=(0, (0, 4)),
                         key=self.dashboard_admin_txt_nome)],
                [sg.Text("O que deseja fazer hoje?", pad=(0, (0, 8)))],
                [sg.Text("💰 Saldo disponível: R$ 0,00",
                         font="Arial 13 bold",
                         text_color="green",
                         pad=(0, (0, 24)),
                         key=self.dashboard_admin_txt_saldo)],
            ], element_justification="center", expand_x=True)],
        ]

        btn_size = (20, 5)
        btn_font = "Arial 13 bold"
        btn_color = ("White", "Brown")

        botoes = [
            [
                sg.Button("🛵\nAcompanhar\nPedidos",
                          key=self.dashboard_admin_btn_pedidos,
                          size=btn_size,
                          font=btn_font,
                          button_color=btn_color,
                          pad=(12, 0)),
                sg.Button("📋\nGerenciar\nCardápio",
                          key=self.dashboard_admin_btn_cardapio,
                          size=btn_size,
                          font=btn_font,
                          button_color=btn_color,
                          pad=(12, 0)),
                sg.Button("👤\nGerenciar\nPerfil",
                          key=self.dashboard_admin_btn_perfil,
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
            key=self.dashboard_admin_key_view,
            element_justification="center",
            expand_y=True,
            expand_x=True,
            visible=False,
        )