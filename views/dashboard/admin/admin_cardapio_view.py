import PySimpleGUI as sg
from PySimpleGUI import VPush

from config import white_theme
from utils.file_util import produtos_path, load_data
from utils.image_util import carregar_imagem

sg.theme_add_new("White", white_theme)
sg.theme("White")


class AdminCardapioView:
    admin_cardapio_key_view = "-ADMIN_CARDAPIO_KEY_VIEW-"

    def __init__(self):
        self._load_produtos()
        self._load_images()

    def _load_produtos(self):
        self._produtos = load_data(produtos_path)

    def _load_images(self):
        self._images = [
            carregar_imagem(p.get("url_imagem"))
            if p
            else None
            for p in self._produtos
        ]

    def render(self):
        CARD_WIDTH = 500

        elements = [
            sg.Frame("", [
                [
                    sg.Column([
                        [sg.Text(p.get("nome_produto"), size=(25, 1), font=("Any", 11, "bold"))],
                        [sg.Multiline(
                            p.get("descricao", ""),
                            size=(100, 3),
                            disabled=True,
                            no_scrollbar=True,
                            border_width=0,
                            background_color=sg.theme_background_color()
                        )],
                        [
                            sg.Text("R$" + p.get("preco_produto").replace(".", ","), font=("Any", 10, "overstrike")),
                            sg.Text("R$" + p.get("preco_promocional").replace(".", ","), text_color="green",
                                    font=("Any", 15, "bold"))
                        ] if p.get("preco_promocional") else [
                            sg.Text("R$" + p.get("preco_produto").replace(".", ","), text_color="green",
                                    font=("Any", 15, "bold"))
                        ]
                    ], size=(CARD_WIDTH, 150), vertical_alignment="center", expand_y=True),
                    sg.Column([
                        [sg.Image(data=img)]
                    ], vertical_alignment="center")
                ]
            ], relief=sg.RELIEF_SOLID, border_width=1)
            for img, p in zip(self._images, self._produtos)
            if img and p
        ]

        rows = [elements[i:i + 2] for i in range(0, len(elements), 2)]

        return sg.Column(rows, scrollable=True, expand_y=True, visible=True, vertical_scroll_only=True)
