from views.dashboard.admin_dashboard_view import AdminDashboardView
from views.dashboard.admin.admin_cardapio_view import AdminCardapioView
from services.dashboard_services.admin_services.admin_pedidos_service import abrir_pedidos
from services.dashboard_services.profile_service import abrir_perfil

from app_controller import app

def go_to_admin_cardapio():
    app.towards(AdminCardapioView.admin_cardapio_key_view)

def go_to_admin_pedidos():
    abrir_pedidos()

class AdminDashboardService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            AdminDashboardView.dashboard_admin_btn_cardapio: lambda : go_to_admin_cardapio(),
            AdminDashboardView.dashboard_admin_btn_pedidos: lambda : go_to_admin_pedidos(),
            AdminDashboardView.dashboard_admin_btn_perfil: lambda : abrir_perfil()
        }

        router_fun = routes.get(events)

        if router_fun:
            router_fun()
