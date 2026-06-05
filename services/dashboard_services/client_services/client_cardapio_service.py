import json
from datetime import datetime

import PySimpleGUI as sg

from views.dashboard.client.client_cardapio_view import ClientCardapioView

from utils.file_util import (
    produtos_path,
    produtos_fieldnames,
    vendas_path,
    vendas_fieldnames,
    load_data,
    save_all,
    append_row,
    next_id,
)

from enums.modal_type_enum import ModalType
from enums.order_status_enum import OrderStatus

from app_controller import app


def _formatar_total(total: float) -> str:
    return f"R$ {total:.2f}".replace(".", ",")


def _atualizar_carrinho(window, carrinho):
    if not carrinho:
        texto = "(vazio)"
    else:
        linhas = []
        for item in carrinho:
            linha = f"{item['qtd']}x {item['nome']} - {_formatar_total(item['preco'] * item['qtd'])}"
            if item["obs"]:
                linha += f"\n   obs: {item['obs']}"
            linhas.append(linha)
        texto = "\n".join(linhas)

    total = sum(item["preco"] * item["qtd"] for item in carrinho)

    window[ClientCardapioView.client_cardapio_cart_display].update(texto)
    window[ClientCardapioView.client_cardapio_txt_total].update(f"Total: {_formatar_total(total)}")


def _preco_efetivo(produto) -> float:
    promocional = produto.get("preco_promocional")
    return float(promocional) if promocional else float(produto.get("preco_produto"))


def _finalizar_pedido(carrinho, cliente):
    produtos = load_data(produtos_path)

    itens = [
        {
            "id_produto": item["id_produto"],
            "nome": item["nome"],
            "qtd": item["qtd"],
            "preco": item["preco"],
            "obs": item["obs"],
        }
        for item in carrinho
    ]

    total = sum(item["preco"] * item["qtd"] for item in carrinho)

    vendas = load_data(vendas_path)
    venda = {
        "id_venda": str(next_id(vendas, "id_venda")),
        "cliente_email": cliente.get("email", ""),
        "cliente_nome": cliente.get("name", ""),
        "itens": json.dumps(itens, ensure_ascii=False),
        "total": f"{total:.2f}",
        "status": OrderStatus.EM_ANDAMENTO.value,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    append_row(vendas_path, vendas_fieldnames, venda)

    quantidades = {}
    for item in carrinho:
        quantidades[item["id_produto"]] = quantidades.get(item["id_produto"], 0) + item["qtd"]

    for produto in produtos:
        if produto["id_produto"] in quantidades:
            atual = int(produto.get("num_pedidos") or 0)
            produto["num_pedidos"] = str(atual + quantidades[produto["id_produto"]])

    save_all(produtos_path, produtos_fieldnames, produtos)


def abrir_pedido(cliente):
    produtos = [p for p in load_data(produtos_path) if (p.get("disponivel") or "true").lower() == "true"]
    produtos_por_id = {p["id_produto"]: p for p in produtos}

    window = ClientCardapioView.window(produtos)
    carrinho = []

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, ClientCardapioView.client_cardapio_btn_fechar):
            break

        if event == ClientCardapioView.client_cardapio_btn_limpar:
            carrinho.clear()
            _atualizar_carrinho(window, carrinho)
            continue

        if event == ClientCardapioView.client_cardapio_btn_finalizar:
            if not carrinho:
                sg.popup_error("Adicione ao menos um item ao carrinho.")
                continue

            _finalizar_pedido(carrinho, cliente)
            window.close()
            app.show_modal("Pedido realizado com sucesso!", ModalType.SUCESSO)
            return

        if isinstance(event, str) and event.startswith("-CLIENT_CARDAPIO_ADD_"):
            id_produto = event[len("-CLIENT_CARDAPIO_ADD_"):].rstrip("-")
            produto = produtos_por_id.get(id_produto)
            if produto is None:
                continue

            qtd_raw = values[ClientCardapioView.client_cardapio_input_qtd(id_produto)].strip()
            obs = values[ClientCardapioView.client_cardapio_input_obs(id_produto)].strip()

            try:
                qtd = int(qtd_raw)
            except ValueError:
                qtd = 0

            if qtd < 1:
                sg.popup_error("Informe uma quantidade válida (mínimo 1).")
                continue

            carrinho.append({
                "id_produto": id_produto,
                "nome": produto["nome_produto"],
                "preco": _preco_efetivo(produto),
                "qtd": qtd,
                "obs": obs,
            })
            _atualizar_carrinho(window, carrinho)

    window.close()


class ClientCardapioService:
    def __init__(self, events, values):
        self.events = events
        self.values = values
