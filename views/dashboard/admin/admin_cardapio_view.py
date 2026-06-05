import PySimpleGUI as sg

from config import white_theme
from utils.file_util import produtos_path, load_data
from utils.image_util import carregar_imagem

sg.theme_add_new("White", white_theme)
sg.theme("White")

CARD_WIDTH = 500


class AdminCardapioView:
    admin_cardapio_key_view = "-ADMIN_CARDAPIO_KEY_VIEW-"
    admin_cardapio_input_pesquisa = "-ADMIN_CARDAPIO_INPUT_PESQUISA-"
    admin_cardapio_btn_adicionar = "-ADMIN_CARDAPIO_BTN_ADICIONAR-"

    admin_cardapio_id_produto = staticmethod(lambda id: f"-ADMIN_CARDAPIO_CARD_{id}-")
    admin_cardapio_nome_produto = staticmethod(lambda id: f"-ADMIN_CARDAPIO_NOME_{id}-")
    admin_cardapio_desc_produto = staticmethod(lambda id: f"-ADMIN_CARDAPIO_DESC_{id}-")
    admin_cardapio_preco_produto = staticmethod(lambda id: f"-ADMIN_CARDAPIO_PRECO_{id}-")
    admin_cardapio_img_produto = staticmethod(lambda id: f"-ADMIN_CARDAPIO_IMG_{id}-")
    admin_cardapio_btn_editar = staticmethod(lambda id: f"-ADMIN_CARDAPIO_BTN_EDITAR_{id}-")
    admin_cardapio_btn_excluir = staticmethod(lambda id: f"-ADMIN_CARDAPIO_BTN_EXCLUIR_{id}-")

    def __init__(self):
        self._produtos = load_data(produtos_path)
        self._images = [carregar_imagem(p.get("url_imagem")) for p in self._produtos]

    @staticmethod
    def format_preco(produto):
        preco = produto.get("preco_produto", "0").replace(".", ",")
        promocional = produto.get("preco_promocional")

        if promocional:
            return f"R$ {promocional.replace('.', ',')}   (de R$ {preco})"

        return f"R$ {preco}"

    @staticmethod
    def build_card(produto, img):
        id_p = produto.get("id_produto")

        return sg.pin(
            sg.Frame("", [
                [
                    sg.Column([
                        [sg.Text(
                            produto.get("nome_produto"),
                            key=AdminCardapioView.admin_cardapio_nome_produto(id_p),
                            font=("Any", 11, "bold"),
                            expand_x=True
                        )],
                        [sg.Multiline(
                            produto.get("descricao", ""),
                            key=AdminCardapioView.admin_cardapio_desc_produto(id_p),
                            size=(50, 3),
                            disabled=True,
                            no_scrollbar=True,
                            border_width=0,
                            expand_x=True,
                            background_color=sg.theme_background_color()
                        )],
                        [sg.Text(
                            AdminCardapioView.format_preco(produto),
                            key=AdminCardapioView.admin_cardapio_preco_produto(id_p),
                            text_color="green",
                            font=("Any", 14, "bold")
                        )],
                        [
                            sg.Button(
                                "✏️ Editar",
                                key=AdminCardapioView.admin_cardapio_btn_editar(id_p),
                                button_color=("White", "Brown"),
                                border_width=0
                            ),
                            sg.Button(
                                "🗑️ Excluir",
                                key=AdminCardapioView.admin_cardapio_btn_excluir(id_p),
                                button_color=("White", "#8B0000"),
                                border_width=0
                            )
                        ]
                    ], vertical_alignment="center", expand_x=True, expand_y=True),
                    sg.Push(),
                    sg.Column([
                        [sg.Image(
                            data=img,
                            key=AdminCardapioView.admin_cardapio_img_produto(id_p)
                        )]
                    ], vertical_alignment="center")
                ]
            ],
                relief=sg.RELIEF_SOLID, border_width=1, expand_x=True,
                key=AdminCardapioView.admin_cardapio_id_produto(id_p)),
            expand_x=True
        )

    def render(self):
        elements = [
            self.build_card(p, img)
            for img, p in zip(self._images, self._produtos)
            if p
        ]

        rows = [
            [
                sg.Column([[elements[i]]], expand_x=True, pad=(0, 0)),
                sg.Column([[elements[i + 1]]], expand_x=True, pad=(0, 0))
                if i + 1 < len(elements) else sg.Column([[]], expand_x=True, pad=(0, 0)),
            ]
            for i in range(0, len(elements), 2)
        ]

        return sg.Column([
            [
                sg.Text("Pesquise pelo nome: "),
                sg.Input(key=self.admin_cardapio_input_pesquisa, enable_events=True),
                sg.Push(),
                sg.Button(
                    "➕ Adicionar Produto",
                    key=self.admin_cardapio_btn_adicionar,
                    button_color=("White", "Brown"),
                    border_width=0,
                    font="Arial 12 bold"
                )
            ],
            *rows
        ], scrollable=True, expand_y=True, expand_x=True, visible=False,
            vertical_scroll_only=True, key=self.admin_cardapio_key_view)
