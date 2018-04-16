import web
from Models import RegisterModel

urls = (
    '/', 'Index',
    '/register', 'Register',
    '/login', 'Login',
    '/login-check', 'CheckLogin',
    '/save-user-registration', 'SaveUserRegistration',
)

app = web.application(urls, globals())

render = web.template.render('Views/templates/', base='main_layout')


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
            return isUser
        else:
            return "error"


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