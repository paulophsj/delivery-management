import os
import sys

_tcl_base = os.path.join(sys.base_prefix, "tcl")
os.environ.setdefault("TCL_LIBRARY", os.path.join(_tcl_base, "tcl8.6"))
os.environ.setdefault("TK_LIBRARY", os.path.join(_tcl_base, "tk8.6"))

from app_controller import app
from services.index_service import IndexService
from services.login_service import LoginService
from services.register_service import RegisterService
from services.router_service import RouterService
from services.dashboard_services.admin_dashboard_service import AdminDashboardService
from services.dashboard_services.client_dashboard_service import ClientDashboardService
from services.dashboard_services.admin_services.admin_cardapio_service import AdminCardapioService
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

        case e if e.startswith("-DASHBOARD_ADMIN"):
            AdminDashboardService(events, values)

        case e if e.startswith("-DASHBOARD_CLIENT"):
            ClientDashboardService(events, values)

        case e if e.startswith("-ADMIN_CARDAPIO"):
            AdminCardapioService(events, values)

app.window.close()