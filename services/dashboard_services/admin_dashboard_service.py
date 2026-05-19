from views.dashboard.admin_dashboard_view import AdminDashboardView
from views.dashboard.admin.admin_cardapio_view import AdminCardapioView

from app_controller import app

def go_to_admin_cardapio():
    app.towards(AdminCardapioView.admin_cardapio_key_view)

class AdminDashboardService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            AdminDashboardView.dashboard_admin_btn_cardapio: lambda : go_to_admin_cardapio()
        }

        router_fun = routes.get(events)

        if router_fun:
            router_fun()