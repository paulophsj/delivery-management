import PySimpleGUI as sg
from utils.pagination import Pagination
from pages import index

layout = [
    [index.index_layout]
]

window = Pagination(sg.Window("Gerenciador de Hamburgueria", layout,resizable=True, element_justification="center"))

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-START_CLIENTE_BTN-":
        window.navigate("-INDEX_PAGE-", "-DASHBOARD_PAGE-")

window.close()