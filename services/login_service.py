from views.login_view import LoginView
from utils.file_util import load_data, users_path
from utils.user_type_util import UserType

from app_controller import app

def auth(email, senha):
    users = load_data(users_path)

    find_user = next(
        (user for user in users if user["email"] == email),
        None
    )

    if find_user == None:
        return # tratativa de erro posterior
    
    if find_user["senha"] != senha:
        app.throw_error("Senha incorreta!")
        return
    
    if find_user["role"] == UserType.CLIENTE.value:
        app.towards("") # rota para cliente
    elif find_user["role"] == UserType.ADMIN.value:
        app.towards("") # rota para administrador
    else:
        app.towards("") # rota de role nao encontrada

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