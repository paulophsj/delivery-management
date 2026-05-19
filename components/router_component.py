import PySimpleGUI as sg
from config import white_theme

sg.theme_add_new("White", white_theme)
sg.theme("White")

class RouterComponent:
    router_key_component = "-ROUTER_KEY_COMPONENT-"
    router_btn_back = "-ROUTER_BTN_BACK-"
    router_btn_forward = "-ROUTER_BTN_FORWARD-"

    def __init__(self):
        pass

    def render(self):
        nav_row = sg.Column([
            [
                sg.Button(
                    "←",
                    key=self.router_btn_back,
                    font="Arial 18 bold",
                    button_color=("Brown", "White"),
                    border_width=0,
                    pad=(8, 8),
                ),

                sg.Push(),

                sg.Text(
                    "🍔 Hamburgueria",
                    font=("Arial", 30, "bold"),
                    text_color="Brown",
                    justification="center",
                    expand_x=True
                ),

                sg.Push(),

                sg.Button(
                    "→",
                    key=self.router_btn_forward,
                    font="Arial 18 bold",
                    button_color=("Brown", "White"),
                    border_width=0,
                    pad=(8, 8),
                )
            ]
        ], expand_x=True)

        layout = [[nav_row]]

        return sg.Column(
            [[sg.Frame(
                "",
                layout,
                pad=(0, 0),
                relief=sg.RELIEF_FLAT,
                border_width=0,
                expand_x=True,
            )]],
            key=self.router_key_component,
            element_justification="center",
            expand_x=True,
            expand_y=False,
        )