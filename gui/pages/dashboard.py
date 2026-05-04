import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

dashboard_layout = sg.Column([
], key="-DASHBOARD_PAGE-", visible=False)