import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:

    def __init__(self):
        self.myClient = MongoClient()
        self.db = self.myClient.codeWizard
        self.users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        data.password = hashed
        data.avatar = ""
        data.background = ""
        data.about = ""
        data.hobbies = ""
        data.birthday = ""
        self.users.insert_one(data)
        return True
        # if bcrypt.checkpw( '123456'.encode(), data.password):
        #     print("Matched")

    def check_login(self, data):

        self.users = self.db.users
        user = self.users.find_one({"username": data.username})

        if user:
            if bcrypt.checkpw(data.password.encode(), user['password']):

                return user
            else:
                return False
        else:
            return False
