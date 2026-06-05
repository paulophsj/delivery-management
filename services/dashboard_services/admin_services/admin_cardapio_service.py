import PySimpleGUI as sg

from views.dashboard.admin.admin_cardapio_view import AdminCardapioView
from views.dashboard.admin.admin_produto_form_view import AdminProdutoFormView

from utils.file_util import (
    produtos_path,
    produtos_fieldnames,
    load_data,
    save_all,
    append_row,
    next_id,
)
from utils.image_util import carregar_imagem

from enums.modal_type_enum import ModalType

from app_controller import app


def buscar_produto(nome: str):
    produtos = load_data(produtos_path)

    if len(nome) >= 3:
        encontrados = [int(p["id_produto"]) for p in produtos if nome.lower() in p["nome_produto"].lower()]

        for p in produtos:
            id_p = int(p["id_produto"])
            app.window[AdminCardapioView.admin_cardapio_id_produto(id_p)].update(visible=id_p in encontrados)
    else:
        for p in produtos:
            id_p = int(p["id_produto"])
            app.window[AdminCardapioView.admin_cardapio_id_produto(id_p)].update(visible=True)


def adicionar_produto():
    dados = AdminProdutoFormView.open()

    if dados is None:
        return

    produtos = load_data(produtos_path)
    novo_id = next_id(produtos, "id_produto")

    novo_produto = {
        "id_produto": str(novo_id),
        "nome_produto": dados["nome_produto"],
        "descricao": dados["descricao"],
        "preco_produto": dados["preco_produto"],
        "preco_promocional": dados["preco_promocional"],
        "url_imagem": dados["url_imagem"],
        "disponivel": "true",
        "num_pedidos": "0",
    }

    append_row(produtos_path, produtos_fieldnames, novo_produto)

    img = carregar_imagem(novo_produto["url_imagem"])
    card = AdminCardapioView.build_card(novo_produto, img)

    container = app.window[AdminCardapioView.admin_cardapio_key_view]
    app.window.extend_layout(container, [[sg.Column([[card]], expand_x=True)]])

    if hasattr(container, "contents_changed"):
        container.contents_changed()
    app.window.refresh()

    app.show_modal("Produto adicionado com sucesso!", ModalType.SUCESSO)


def editar_produto(id_produto: str):
    produtos = load_data(produtos_path)

    produto = next((p for p in produtos if p["id_produto"] == id_produto), None)
    if produto is None:
        return app.show_modal("Produto não encontrado.", ModalType.ERRO)

    url_antiga = produto.get("url_imagem")
    dados = AdminProdutoFormView.open(produto)

    if dados is None:
        return

    produto.update(dados)
    save_all(produtos_path, produtos_fieldnames, produtos)

    app.window[AdminCardapioView.admin_cardapio_nome_produto(id_produto)].update(produto["nome_produto"])
    app.window[AdminCardapioView.admin_cardapio_desc_produto(id_produto)].update(produto["descricao"])
    app.window[AdminCardapioView.admin_cardapio_preco_produto(id_produto)].update(
        AdminCardapioView.format_preco(produto)
    )

    if produto["url_imagem"] != url_antiga:
        img = carregar_imagem(produto["url_imagem"])
        app.window[AdminCardapioView.admin_cardapio_img_produto(id_produto)].update(data=img)

    app.show_modal("Produto atualizado com sucesso!", ModalType.SUCESSO)


def excluir_produto(id_produto: str):
    confirmar = sg.popup_yes_no("Tem certeza que deseja excluir este produto?", title="Excluir Produto")

    if confirmar != "Yes":
        return

    produtos = load_data(produtos_path)
    produtos = [p for p in produtos if p["id_produto"] != id_produto]
    save_all(produtos_path, produtos_fieldnames, produtos)

    app.window[AdminCardapioView.admin_cardapio_id_produto(id_produto)].update(visible=False)

    app.show_modal("Produto excluído com sucesso!", ModalType.SUCESSO)


def _extrair_id(events: str, prefixo: str) -> str:
    return events[len(prefixo):].rstrip("-")


class AdminCardapioService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        if events == AdminCardapioView.admin_cardapio_input_pesquisa:
            buscar_produto(values[AdminCardapioView.admin_cardapio_input_pesquisa])

        elif events == AdminCardapioView.admin_cardapio_btn_adicionar:
            adicionar_produto()

        elif events.startswith("-ADMIN_CARDAPIO_BTN_EDITAR_"):
            editar_produto(_extrair_id(events, "-ADMIN_CARDAPIO_BTN_EDITAR_"))

        elif events.startswith("-ADMIN_CARDAPIO_BTN_EXCLUIR_"):
            excluir_produto(_extrair_id(events, "-ADMIN_CARDAPIO_BTN_EXCLUIR_"))
