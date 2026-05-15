from app_controller import app
from enums.modal_type_enum import ModalType
from views.register_view import RegisterView

from utils.file_util import load_data, write_file, users_path
from enums.user_type_enum import UserType

def register(nome, email, senha, confirmar_senha):
    if not all([nome, email, senha, confirmar_senha]):
        return app.show_modal("Todos os campos devem ser preenchidos.", ModalType.ERRO)

    if "@" not in email or ".com" not in email:
        return app.show_modal("O email deve estar no formato válido", ModalType.ERRO)

    users = load_data(users_path)
    
    exists_user = next(
        (user for user in users if user["email"] == email),
        None
    )

    if exists_user is not None:
        return app.show_modal("Já existe um usuário com esse email.", ModalType.ERRO)

    if senha != confirmar_senha:
        return app.show_modal("As senhas não coincidem.", ModalType.ERRO)
    
    write_file(users_path, [nome,email,senha,UserType.CLIENTE.value])
    return app.show_modal("Cadastrado com sucesso!", ModalType.SUCESSO)

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