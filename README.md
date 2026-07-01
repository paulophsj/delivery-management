# Delivery Management — Hamburgueria

Aplicação desktop (GUI) de gerenciamento de uma hamburgueria/delivery, construída em Python com **PySimpleGUI**. Permite cadastro e login de usuários, gestão de cardápio/produtos pelo administrador, realização de pedidos pelo cliente e acompanhamento de vendas.

## Funcionalidades

- Cadastro e login de usuários (cliente e administrador)
- **Administrador:** gerenciar cardápio (criar/editar/remover produtos), acompanhar pedidos e visualizar o saldo de vendas
- **Cliente:** navegar pelo cardápio, montar e enviar pedidos, editar o perfil
- Persistência de dados em arquivos CSV (sem necessidade de banco de dados)

## Requisitos

- **Python 3.13** (o projeto está configurado para essa versão)
- `pip` para instalação das dependências
- Ambiente com suporte a interface gráfica (Tkinter/Tcl-Tk). No Windows, o Tcl/Tk já acompanha a instalação oficial do Python.

## Dependências

Listadas em [`requirements.txt`](requirements.txt):

| Biblioteca   | Uso                                              |
| ------------ | ------------------------------------------------ |
| PySimpleGUI  | Interface gráfica da aplicação                   |
| requests     | Download de imagens de produtos a partir de URLs |
| Pillow       | Tratamento e exibição das imagens                |

> As demais bibliotecas usadas (`csv`, `json`, `os`, `sys`, `datetime`, `enum`, `io`) fazem parte da biblioteca padrão do Python.

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/paulophsj/delivery-management.git
cd delivery-management
```

### 2. Criar e ativar um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python main.py
```

A janela da aplicação será aberta maximizada.

## Estrutura do projeto

```
delivery-management/
├── main.py                 # Ponto de entrada / loop de eventos da aplicação
├── app_controller.py       # Controle de janela, navegação e estado global
├── config.py               # Tema visual da interface
├── components/             # Componentes reutilizáveis de UI (router, modal, etc.)
├── views/                  # Telas da aplicação (index, login, cadastro, dashboards)
│   └── dashboard/          # Telas de admin e cliente
├── services/               # Regras de negócio e tratamento de eventos por tela
│   └── dashboard_services/ # Serviços dos dashboards (admin e cliente)
├── enums/                  # Enums (tipo de usuário, status de pedido, tipo de modal)
├── utils/                  # Utilitários (leitura/escrita de CSV, imagens, layout)
└── data/                   # Persistência em CSV (usuários, produtos, vendas)
```

## Persistência de dados

Os dados são armazenados em arquivos CSV dentro da pasta `data/`:

- `users.csv` — usuários cadastrados
- `produtos.csv` — produtos do cardápio
- `vendas.csv` — vendas/pedidos realizados
