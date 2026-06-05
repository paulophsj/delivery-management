import json

import PySimpleGUI as sg

from config import white_theme
from enums.order_status_enum import OrderStatus

sg.theme_add_new("White", white_theme)
sg.theme("White")

STATUS_OPCOES = [s.value for s in OrderStatus]


class AdminPedidosView:
    admin_pedidos_btn_fechar = "-ADMIN_PEDIDOS_BTN_FECHAR-"
    admin_pedidos_txt_saldo = "-ADMIN_PEDIDOS_TXT_SALDO-"

    admin_pedidos_combo_status = staticmethod(lambda id: f"-ADMIN_PEDIDOS_COMBO_{id}-")
    admin_pedidos_btn_atualizar = staticmethod(lambda id: f"-ADMIN_PEDIDOS_ATUALIZAR_{id}-")

    @staticmethod
    def _resumo_itens(venda):
        try:
            itens = json.loads(venda.get("itens") or "[]")
        except (ValueError, TypeError):
            itens = []

        linhas = []
        for item in itens:
            linha = f"  • {item['qtd']}x {item['nome']}"
            if item.get("obs"):
                linha += f"  (obs: {item['obs']})"
            linhas.append(linha)

        return "\n".join(linhas) if linhas else "  (sem itens)"

    @staticmethod
    def _build_card(venda):
        id_v = venda.get("id_venda")
        total = float(venda.get("total") or 0)

        return sg.Frame("", [
            [
                sg.Text(f"Pedido #{id_v}", font=("Any", 12, "bold")),
                sg.Push(),
                sg.Text(venda.get("data", ""), font=("Any", 9))
            ],
            [sg.Text(f"Cliente: {venda.get('cliente_nome', '')}", font=("Any", 10))],
            [sg.Text(AdminPedidosView._resumo_itens(venda), font=("Any", 10))],
            [sg.Text(f"Total: R$ {total:.2f}".replace(".", ","),
                     text_color="green", font=("Any", 11, "bold"))],
            [
                sg.Text("Status:"),
                sg.Combo(STATUS_OPCOES,
                         default_value=venda.get("status", OrderStatus.EM_ANDAMENTO.value),
                         key=AdminPedidosView.admin_pedidos_combo_status(id_v),
                         readonly=True, size=(16, 1)),
                sg.Button("Atualizar",
                          key=AdminPedidosView.admin_pedidos_btn_atualizar(id_v),
                          button_color=("White", "Brown"), border_width=0)
            ]
        ], relief=sg.RELIEF_SOLID, border_width=1, expand_x=True)

    @staticmethod
    def window(vendas, saldo):
        vendas_ordenadas = sorted(vendas, key=lambda v: int(v.get("id_venda") or 0), reverse=True)

        cards = [[AdminPedidosView._build_card(v)] for v in vendas_ordenadas]

        lista_col = sg.Column(
            cards if cards else [[sg.Text("Nenhum pedido registrado ainda.")]],
            scrollable=True, vertical_scroll_only=True, expand_y=True, expand_x=True, size=(640, 520)
        )

        layout = [
            [sg.Text("Acompanhar Pedidos", font=("Arial", 18, "bold"))],
            [sg.Text(f"💰 Saldo disponível: R$ {saldo:.2f}".replace(".", ","),
                     key=AdminPedidosView.admin_pedidos_txt_saldo,
                     font=("Arial", 13, "bold"), text_color="green")],
            [lista_col],
            [sg.Push(),
             sg.Button("Fechar", key=AdminPedidosView.admin_pedidos_btn_fechar, border_width=0)]
        ]

        return sg.Window("Pedidos", layout, modal=True, finalize=True,
                         resizable=True, element_justification="left")
