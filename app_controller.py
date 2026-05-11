from PySimpleGUI import Window

from views.index_view import IndexView
from views.login_view import LoginView


class AppController:
    window: Window
    current_page: str

    def __init__(self, current: str, window = None):
        if window is not None:
            self.window = window

        self.current_page = current

    def towards(self, towards: str):
        self.window[self.current_page].update(visible=False)
        self.window[towards].update(visible=True)
        self.current_page = towards

render_layouts = [[
    IndexView().render(),
    LoginView().render()
]]

window = Window("Hamburgueria", render_layouts)

app = AppController(IndexView.index_key_view, window) # classes subsequentes utilizam o app para controlar a window