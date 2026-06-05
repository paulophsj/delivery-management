from views.dashboard.profile_form_view import ProfileFormView

from utils.file_util import users_path, users_fieldnames, load_data, save_all

from enums.modal_type_enum import ModalType

from app_controller import app


def abrir_perfil():
    if app.current_user is None:
        return app.show_modal("Faça login para gerenciar o perfil.", ModalType.ERRO)

    dados = ProfileFormView.open(app.current_user)

    if dados is None:
        return

    users = load_data(users_path)
    usuario = next((u for u in users if u["email"] == app.current_user["email"]), None)

    if usuario is None:
        return app.show_modal("Usuário não encontrado.", ModalType.ERRO)

    usuario["name"] = dados["name"]
    usuario["senha"] = dados["senha"]
    save_all(users_path, users_fieldnames, users)

    app.current_user["name"] = dados["name"]
    app.current_user["senha"] = dados["senha"]
    app.set_user(dados["name"])

    app.show_modal("Perfil atualizado com sucesso!", ModalType.SUCESSO)
