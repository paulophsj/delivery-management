from PySimpleGUI import Window

class Pagination:
    window: Window

    def __init__(self, window: Window):
        self.window = window

    def __getattr__(self, item):
        return getattr(self.window, item)

    def navigate(self, current: str, to: str):
        self.window[current].update(visible=False)
        self.window[to].update(visible=True)