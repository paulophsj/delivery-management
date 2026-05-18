import PySimpleGUI as sg

from components.router_component import RouterComponent
from components.modal_component import ModalComponent

from views.index_view import IndexView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.dashboard.admin_dashboard_view import AdminDashboardView
from views.dashboard.client_dashboard_view import ClientDashboardView

from enums.modal_type_enum import ModalType


class AppController:
    window: sg.Window
    current_page: str
    routing: list[str]
    routing_index: int

    def __init__(self, current: str, window: sg.Window = None):
        if window is not None:
            self.window = window

        self.current_page = current
        self.routing = [current]
        self.routing_index = 0

    def towards(self, towards: str):
        self.routing = self.routing[:self.routing_index + 1]

        self.window[self.current_page].update(visible=False)
        self.window[towards].update(visible=True)
        self.current_page = towards
        self.routing.append(towards)
        self.routing_index += 1

    def set_user(self, nome: str):
        self.window[AdminDashboardView.dashboard_admin_txt_nome].update(f"Olá, {nome}!")
        self.window[ClientDashboardView.dashboard_client_txt_nome].update(f"Olá, {nome}!")

    def show_modal(self, message: str, type: ModalType):
        modal = sg.Window(
            "Modal",
            [
                [sg.VPush()],
                [ModalComponent().render(message, type)],
                [sg.VPush()]
            ],
            modal=True,
            element_justification="center"
        )

        while True:
            event, values = modal.read()

            if event == sg.WINDOW_CLOSED:
                break

        modal.close()


render_layouts = [
    [RouterComponent().render()],
    [sg.VPush()],
    [
        IndexView().render(),
        LoginView().render(),
        RegisterView().render(),
        AdminDashboardView().render(),
        ClientDashboardView().render()
    ],
    [sg.VPush()]
]

window = sg.Window(
    "Hamburgueria",
    render_layouts,
    finalize=True,
    resizable=True,
    element_justification="center"
    )
window.maximize()

app = AppController(IndexView.index_key_view, window) # classes subsequentes utilizam o app para controlar a window