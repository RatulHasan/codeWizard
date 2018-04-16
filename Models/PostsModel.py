import pymongo
from pymongo import MongoClient


class PostsModel:

    def __init__(self):
        self.myClient = MongoClient()
        self.db = self.myClient.codeWizard
        self.posts = self.db.posts

    def insert_post(self, data):
        self.posts.insert_one(data)
        return True

    def all_post(self, username):
        all_post = self.posts.find({"username": username})
        # new_post = []
        # for post in all_post:
        #     new_post.append(post)

        return all_post
