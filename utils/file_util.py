import csv
import os

produtos_path = "./data/produtos.csv"
users_path = "./data/users.csv"
vendas_path = "./data/vendas.csv"

produtos_fieldnames = [
    "id_produto",
    "nome_produto",
    "descricao",
    "preco_produto",
    "preco_promocional",
    "url_imagem",
    "disponivel",
    "num_pedidos",
]

vendas_fieldnames = [
    "id_venda",
    "cliente_email",
    "cliente_nome",
    "itens",
    "total",
    "status",
    "data",
]

users_fieldnames = [
    "name",
    "email",
    "senha",
    "role",
]

def load_data(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []

    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_file(path, data):
    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def append_row(path, fieldnames, row):
    file_is_empty = not os.path.exists(path) or os.path.getsize(path) == 0

    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if file_is_empty:
            writer.writeheader()

        writer.writerow(row)

def save_all(path, fieldnames, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def next_id(rows, id_field):
    ids = [int(r[id_field]) for r in rows if r.get(id_field)]
    return max(ids) + 1 if ids else 1
