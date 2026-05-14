from views.index_view import IndexView
from views.login_view import LoginView
from views.register_view import RegisterView

from app_controller import app


def go_to_login():
    app.towards(LoginView.login_key_view)

def go_to_register():
    app.towards(RegisterView.register_key_view)


class IndexService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            IndexView.index_btn_login: lambda: go_to_login(),
            IndexView.index_btn_cadastro: lambda: go_to_register()
        }

        router_fun = routes.get(events)

        if router_fun:
            router_fun() # chama o nome da funcao e executa