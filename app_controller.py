import PySimpleGUI as sg

from views.index_view import IndexView
from views.login_view import LoginView
from views.error_view import ErrorView


class AppController:
    window: sg.Window
    current_page: str

    def __init__(self, current: str, window = None):
        if window is not None:
            self.window = window

        self.current_page = current

    def towards(self, towards: str):
        self.window[self.current_page].update(visible=False)
        self.window[towards].update(visible=True)
        self.current_page = towards

    def throw_error(self, message: str):
        error_window = sg.Window(
            "Erro",
            [[ErrorView().render(message)]],
            size=(400,100),
            modal=True,
            element_justification="center"
        )

        while True:
            event, values = error_window.read()

            if event == sg.WINDOW_CLOSED:
                break

        error_window.close()


render_layouts = [[
    IndexView().render(),
    LoginView().render()
]]

window = sg.Window("Hamburgueria", render_layouts)

app = AppController(IndexView.index_key_view, window) # classes subsequentes utilizam o app para controlar a window