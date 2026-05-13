from views.login_view import LoginView

def auth(email, senha):
    print(email, senha)

class LoginService:
    def __init__(self, events, values):
        self.events = events
        self.values = values

        routes = {
            LoginView.login_btn_signin: lambda: auth(
                self.values[LoginView.login_input_email],
                self.values[LoginView.login_input_senha])
        }

        router_func = routes.get(events)

        if router_func:
            router_func()