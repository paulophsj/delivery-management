from components.router_component import RouterComponent

from app_controller import app

def forwards():
    if app.routing_index < len(app.routing) - 1:
        app.routing_index += 1
        next_page = app.routing[app.routing_index]

        app.window[app.current_page].update(visible=False)
        app.window[next_page].update(visible=True)
        app.current_page = next_page


def backwards():
    if app.routing_index > 0:
        app.routing_index -= 1
        previous_page = app.routing[app.routing_index]

        app.window[app.current_page].update(visible=False)
        app.window[previous_page].update(visible=True)
        app.current_page = previous_page

class RouterService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            RouterComponent.router_btn_forward: lambda : forwards(),
            RouterComponent.router_btn_back: lambda : backwards()
        }

        router_func = routes.get(events)

        if router_func:
            router_func()