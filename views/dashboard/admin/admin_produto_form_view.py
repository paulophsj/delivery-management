import PySimpleGUI as sg

from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")


class AdminProdutoFormView:
    form_input_nome = "-FORM_PRODUTO_NOME-"
    form_input_descricao = "-FORM_PRODUTO_DESCRICAO-"
    form_input_preco = "-FORM_PRODUTO_PRECO-"
    form_input_promocional = "-FORM_PRODUTO_PROMOCIONAL-"
    form_input_url = "-FORM_PRODUTO_URL-"
    form_btn_salvar = "-FORM_PRODUTO_SALVAR-"
    form_btn_cancelar = "-FORM_PRODUTO_CANCELAR-"

    @staticmethod
    def open(produto=None):
        """Abre um formulário modal. Retorna um dict com os dados validados
        ou None caso o usuário cancele/feche a janela."""
        produto = produto or {}
        titulo = "Editar Produto" if produto else "Novo Produto"

        layout = [
            [sg.Text(titulo, font=("Arial", 16, "bold"), pad=(0, (0, 12)))],

            [sg.Text("Nome")],
            [sg.Input(produto.get("nome_produto", ""),
                      key=AdminProdutoFormView.form_input_nome, size=(40, 1))],

            [sg.Text("Descrição")],
            [sg.Multiline(produto.get("descricao", ""),
                          key=AdminProdutoFormView.form_input_descricao, size=(40, 4))],

            [sg.Text("Preço (ex: 19.90)")],
            [sg.Input(produto.get("preco_produto", ""),
                      key=AdminProdutoFormView.form_input_preco, size=(40, 1))],

            [sg.Text("Preço promocional (opcional)")],
            [sg.Input(produto.get("preco_promocional", ""),
                      key=AdminProdutoFormView.form_input_promocional, size=(40, 1))],

            [sg.Text("URL da imagem")],
            [sg.Input(produto.get("url_imagem", ""),
                      key=AdminProdutoFormView.form_input_url, size=(40, 1))],

            [
                sg.Push(),
                sg.Button("Salvar", key=AdminProdutoFormView.form_btn_salvar,
                          button_color=("White", "Brown"), border_width=0,
                          font="Arial 12 bold", pad=((0, 8), (16, 0))),
                sg.Button("Cancelar", key=AdminProdutoFormView.form_btn_cancelar,
                          button_color=("White", "#420B09"), border_width=0,
                          font="Arial 12 bold", pad=(0, (16, 0)))
            ]
        ]

        window = sg.Window(titulo, layout, modal=True, finalize=True,
                           element_justification="left")

        resultado = None

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, AdminProdutoFormView.form_btn_cancelar):
                break

            if event == AdminProdutoFormView.form_btn_salvar:
                nome = values[AdminProdutoFormView.form_input_nome].strip()
                descricao = values[AdminProdutoFormView.form_input_descricao].strip()
                preco = values[AdminProdutoFormView.form_input_preco].strip().replace(",", ".")
                promocional = values[AdminProdutoFormView.form_input_promocional].strip().replace(",", ".")
                url = values[AdminProdutoFormView.form_input_url].strip()

                if not all([nome, preco, url]):
                    sg.popup_error("Nome, preço e URL da imagem são obrigatórios.")
                    continue

                try:
                    float(preco)
                except ValueError:
                    sg.popup_error("O preço deve ser um número válido (ex: 19.90).")
                    continue

                if promocional:
                    try:
                        float(promocional)
                    except ValueError:
                        sg.popup_error("O preço promocional deve ser um número válido.")
                        continue

                resultado = {
                    "nome_produto": nome,
                    "descricao": descricao,
                    "preco_produto": preco,
                    "preco_promocional": promocional,
                    "url_imagem": url,
                }
                break

        window.close()
        return resultado
