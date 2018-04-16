import web

from Models import RegisterModel

web.config.debug = False

urls = (
    '/', 'Index',
    '/register', 'Register',
    '/login', 'Login',
    '/login-check', 'CheckLogin',
    '/logout', 'Logout',
    '/save-user-registration', 'SaveUserRegistration',
)

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("session"), initializer={'user': None})
session_data = session._initializer


render = web.template.render('Views/templates/', base='main_layout', globals= {"session": session_data, 'current_user': session_data['user']})


class Index:
    def GET(self):
        return render.home()


class Login:
    def GET(self):
        return render.login()


class CheckLogin:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        isUser = reg_model.check_login(data)

        if isUser:
            session_data['user'] = isUser
            return isUser
        else:
            return "error"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"


class Register:
    def GET(self):
        return render.register()



class SaveUserRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


if __name__ == "__main__":
    app.run()