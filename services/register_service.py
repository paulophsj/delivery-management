from app_controller import app
from views.register_view import RegisterView

from utils.file_util import load_data, write_file, users_path
from utils.user_type_util import UserType

def register(nome, email, senha, confirmar_senha):
    if not all([nome, email, senha, confirmar_senha]):
        return app.throw_error("Todos os campos devem ser preenchidos.")

    users = load_data(users_path)
    
    exists_user = next(
        (user for user in users if user["email"] == email),
        None
    )

    if exists_user is not None:
        return app.throw_error("Já existe um usuário com esse email.")

    if senha != confirmar_senha:
        return app.throw_error("As senhas não coincidem.")
    
    write_file(users_path, [nome,email,senha,UserType.CLIENTE.value])
    print("usuário cadastrado com sucesso!")

class RegisterService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            RegisterView.register_btn_signup: lambda: register(
                values[RegisterView.register_input_nome],
                values[RegisterView.register_input_email],
                values[RegisterView.register_input_senha],
                values[RegisterView.register_input_confirmar_senha]
            )
        }

        router_func = routes.get(events)

        if router_func:
            router_func()