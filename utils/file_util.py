import csv

produtos_path = "./data/produtos.csv"
users_path = "./data/users.csv"
vendas_path = "./data/vendas.csv"

def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_file(path, data):
    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)