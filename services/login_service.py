from views.login_view import LoginView
from views.dashboard.admin_dashboard_view import AdminDashboardView
from views.dashboard.client_dashboard_view import ClientDashboardView

from utils.file_util import load_data, users_path

from enums.user_type_enum import UserType
from enums.modal_type_enum import ModalType

from app_controller import app

def auth(email: str, senha: str):
    if not all([email, senha]):
        return app.show_modal("Todos os campos devem ser preenchidos", ModalType.ERRO)

    if "@" not in email or ".com" not in email:
        return app.show_modal("O email deve estar no formato válido", ModalType.ERRO)

    users = load_data(users_path)

    find_user = next(
        (u for u in users if u["email"] == email),
        None
    )

    if find_user is None:
        return app.show_modal("Usuário não encontrado.", ModalType.ERRO)
    
    if find_user["senha"] != senha:
        return app.show_modal("Senha incorreta!", ModalType.ERRO)

    app.set_user(find_user["name"])

    if find_user["role"] == UserType.CLIENTE.value:
        return app.towards(ClientDashboardView.dashboard_client_key_view)
    elif find_user["role"] == UserType.ADMIN.value:
        return app.towards(AdminDashboardView.dashboard_admin_key_view)
    else:
        return app.towards("") # rota de role nao encontrada

class LoginService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            LoginView.login_btn_signin: lambda: auth(
                self.values[LoginView.login_input_email],
                self.values[LoginView.login_input_senha])
        }

        router_func = routes.get(events)

        if router_func:
            router_func()