import web

from Models import RegisterModel, PostsModel

import datetime

web.config.debug = False

urls = (
    '/', 'Index',
    '/register', 'Register',
    '/login', 'Login',
    '/login-check', 'CheckLogin',
    '/logout', 'Logout',
    '/save-user-registration', 'SaveUserRegistration',
    '/save-post-activity', 'SavePostActivity',
)

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("session"), initializer={'user': None})
session_data = session._initializer


render = web.template.render('Views/templates/', base='main_layout', globals= {"session": session_data})
# render = web.template.render('Views/templates/', base='main_layout', globals= {"session": session_data, 'current_user': session_data['user']})


class Index:
    def GET(self):
        # data = type('obj', (object,), {"username": "ratul", "password": "123456"})
        # reg_model = RegisterModel.RegisterModel()
        # isUser = reg_model.check_login(data)
        #
        # if isUser:
        #     session_data['user'] = isUser
        #     post_model = PostsModel.PostsModel()
        #     new_post = post_model.all_post(session_data['user']['username'])

        post_model = PostsModel.PostsModel()
        new_post = post_model.all_post()

        return render.home(new_post)


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
        return True


class SavePostActivity:
    def POST(self):
        data = web.input()
        data.user_id = session_data['user']['_id']
        data.username = session_data['user']['username']
        data.created_on = datetime.datetime.now()
        try:
            post_model = PostsModel.PostsModel()
            post_model.insert_post(data)
            return "success"
        except:
            return "error"


if __name__ == "__main__":
    app.run()