import PySimpleGUI as sg

from config import white_theme
from utils.image_util import carregar_imagem

sg.theme_add_new("White", white_theme)
sg.theme("White")


class ClientCardapioView:
    client_cardapio_cart_display = "-CLIENT_CARDAPIO_CART_DISPLAY-"
    client_cardapio_txt_total = "-CLIENT_CARDAPIO_TXT_TOTAL-"
    client_cardapio_btn_finalizar = "-CLIENT_CARDAPIO_BTN_FINALIZAR-"
    client_cardapio_btn_limpar = "-CLIENT_CARDAPIO_BTN_LIMPAR-"
    client_cardapio_btn_fechar = "-CLIENT_CARDAPIO_BTN_FECHAR-"

    client_cardapio_input_qtd = staticmethod(lambda id: f"-CLIENT_CARDAPIO_QTD_{id}-")
    client_cardapio_input_obs = staticmethod(lambda id: f"-CLIENT_CARDAPIO_OBS_{id}-")
    client_cardapio_btn_add = staticmethod(lambda id: f"-CLIENT_CARDAPIO_ADD_{id}-")

    @staticmethod
    def _build_card(produto):
        id_p = produto.get("id_produto")
        img = carregar_imagem(produto.get("url_imagem"), tamanho=(90, 90))

        promocional = produto.get("preco_promocional")
        preco = promocional if promocional else produto.get("preco_produto")
        preco_str = f"R$ {preco.replace('.', ',')}"

        return sg.Frame("", [
            [
                sg.Image(data=img),
                sg.Column([
                    [sg.Text(produto.get("nome_produto"), font=("Any", 11, "bold"))],
                    [sg.Text(preco_str, text_color="green", font=("Any", 12, "bold"))],
                    [
                        sg.Text("Qtd:"),
                        sg.Input("1", key=ClientCardapioView.client_cardapio_input_qtd(id_p), size=(4, 1)),
                        sg.Text("Obs:"),
                        sg.Input("", key=ClientCardapioView.client_cardapio_input_obs(id_p), size=(28, 1)),
                        sg.Button("Adicionar", key=ClientCardapioView.client_cardapio_btn_add(id_p),
                                  button_color=("White", "Brown"), border_width=0)
                    ]
                ])
            ]
        ], relief=sg.RELIEF_SOLID, border_width=1, expand_x=True)

    @staticmethod
    def window(produtos):
        cardapio = [
            [ClientCardapioView._build_card(p)]
            for p in produtos
        ]

        cardapio_col = sg.Column(
            cardapio if cardapio else [[sg.Text("Nenhum produto disponível no momento.")]],
            scrollable=True, vertical_scroll_only=True, expand_y=True, expand_x=True, size=(620, 520)
        )

        carrinho_col = sg.Column([
            [sg.Text("🛒 Carrinho", font=("Arial", 14, "bold"))],
            [sg.Multiline("", key=ClientCardapioView.client_cardapio_cart_display,
                          size=(40, 22), disabled=True, no_scrollbar=False)],
            [sg.Text("Total: R$ 0,00", key=ClientCardapioView.client_cardapio_txt_total,
                     font=("Arial", 13, "bold"))],
            [
                sg.Button("Finalizar Pedido", key=ClientCardapioView.client_cardapio_btn_finalizar,
                          button_color=("White", "Brown"), border_width=0, font="Arial 12 bold"),
                sg.Button("Limpar", key=ClientCardapioView.client_cardapio_btn_limpar,
                          button_color=("White", "#420B09"), border_width=0)
            ]
        ], vertical_alignment="top")

        layout = [
            [sg.Text("Monte seu pedido", font=("Arial", 18, "bold"))],
            [cardapio_col, sg.VerticalSeparator(), carrinho_col],
            [sg.Push(),
             sg.Button("Fechar", key=ClientCardapioView.client_cardapio_btn_fechar, border_width=0)]
        ]

        return sg.Window("Novo Pedido", layout, modal=True, finalize=True,
                         resizable=True, element_justification="left")
