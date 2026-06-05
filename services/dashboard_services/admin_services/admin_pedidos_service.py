import PySimpleGUI as sg

from views.dashboard.admin.admin_pedidos_view import AdminPedidosView

from utils.file_util import (
    vendas_path,
    vendas_fieldnames,
    load_data,
    save_all,
)

from app_controller import app


def calcular_saldo(vendas=None) -> float:
    vendas = vendas if vendas is not None else load_data(vendas_path)
    return sum(float(v.get("total") or 0) for v in vendas)


def _atualizar_status(vendas, id_venda, novo_status):
    venda = next((v for v in vendas if v["id_venda"] == id_venda), None)
    if venda is None:
        return

    venda["status"] = novo_status
    save_all(vendas_path, vendas_fieldnames, vendas)


def abrir_pedidos():
    vendas = load_data(vendas_path)
    window = AdminPedidosView.window(vendas, calcular_saldo(vendas))

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, AdminPedidosView.admin_pedidos_btn_fechar):
            break

        if isinstance(event, str) and event.startswith("-ADMIN_PEDIDOS_ATUALIZAR_"):
            id_venda = event[len("-ADMIN_PEDIDOS_ATUALIZAR_"):].rstrip("-")
            novo_status = values[AdminPedidosView.admin_pedidos_combo_status(id_venda)]

            _atualizar_status(vendas, id_venda, novo_status)

            window[AdminPedidosView.admin_pedidos_txt_saldo].update(
                f"💰 Saldo disponível: R$ {calcular_saldo(vendas):.2f}".replace(".", ",")
            )
            sg.popup_ok(f"Pedido #{id_venda} atualizado para {novo_status}.", title="Status atualizado")

    window.close()

    if hasattr(app, "refresh_admin_saldo"):
        app.refresh_admin_saldo()


class AdminPedidosService:
    def __init__(self, events, values):
        self.events = events
        self.values = values
