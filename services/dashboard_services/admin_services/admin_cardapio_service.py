from views.dashboard.admin.admin_cardapio_view import AdminCardapioView
from utils.file_util import produtos_path, load_data

from app_controller import app

def buscar_produto(nome: str):
    produtos = load_data(produtos_path)

    if len(nome) >= 3:
        produtos_encontrados = [int(p["id_produto"]) for p in produtos if nome in p["nome_produto"]]

        for p in produtos:
            id_p = int(p["id_produto"])
            visivel = id_p in produtos_encontrados
            app.window[AdminCardapioView.admin_cardapio_id_produto(id_p)].update(visible=visivel)

    else:
        for p in produtos:
            id_p = int(p["id_produto"])
            app.window[AdminCardapioView.admin_cardapio_id_produto(id_p)].update(visible=True)

class AdminCardapioService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            AdminCardapioView.admin_cardapio_input_pesquisa: lambda : buscar_produto(
                self.values[AdminCardapioView.admin_cardapio_input_pesquisa]
            )
        }

        router_fun = routes.get(events)

        if router_fun:
            router_fun()