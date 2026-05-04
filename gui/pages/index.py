import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new('White', white_theme)
sg.theme('White')

index_layout = sg.Column([
    [sg.Text(
        "🍔",
        font=(None, 37),
        text_color="Brown",
        justification="center",
        expand_x=True
    )],

    [sg.Text(
        "Hamburgueria",
        font="Arial 18 bold",
        text_color="Brown",
        justification="center",
        expand_x=True
    )],

    [sg.Text(
        "Gerenciador",
        font="Arial 10",
        text_color="Black",
        justification="center",
        expand_x=True
    )],

    [sg.HorizontalSeparator(
        color="Orange",
        pad=((60, 60), (10, 10))
    )],

    [sg.Text(
        "Selecione abaixo o seu perfil de acesso para continuar",
        justification="center"
    )],

    [sg.Button(
        "Cliente",
        font="Arial 15",
        border_width=0,
        button_color=("White", "Brown"),
        key="-START_CLIENTE_BTN-",
        expand_x=True
    )],

    [sg.Button(
        "Administrador",
        font="Arial 15",
        border_width=0,
        button_color=("White", "#420B09"),
        key="-START_ADM_BTN-",
        expand_x=True
    )]
], key="-INDEX_PAGE-", expand_y=True)