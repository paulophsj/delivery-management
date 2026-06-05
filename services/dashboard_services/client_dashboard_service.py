from views.dashboard.client_dashboard_view import ClientDashboardView
from services.dashboard_services.client_services.client_cardapio_service import abrir_pedido
from services.dashboard_services.profile_service import abrir_perfil

from enums.modal_type_enum import ModalType

from app_controller import app


def novo_pedido():
    if app.current_user is None:
        return app.show_modal("Faça login para realizar um pedido.", ModalType.ERRO)

    abrir_pedido(app.current_user)


class ClientDashboardService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            ClientDashboardView.dashboard_client_btn_novo_pedido: lambda: novo_pedido(),
            ClientDashboardView.dashboard_client_btn_perfil: lambda: abrir_perfil()
        }

        router_fun = routes.get(events)

        if router_fun:
            router_fun()
