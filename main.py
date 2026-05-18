from app_controller import app
from services.index_service import IndexService
from services.login_service import LoginService
from services.register_service import RegisterService
from services.router_service import RouterService
import PySimpleGUI as sg

while True:
    events, values = app.window.read()

    if events == sg.WINDOW_CLOSED:
        break

    match str(events):
        case e if e.startswith("-ROUTER"):
            RouterService(events, values)

        case e if e.startswith("-INDEX"):
            IndexService(events, values)

        case e if e.startswith("-LOGIN"):
            LoginService(events, values)

        case e if e.startswith("-REGISTER"):
            RegisterService(events, values)

app.window.close()