import pymongo
from pymongo import MongoClient
import datetime
import humanize


class PostsModel:

    def __init__(self):
        self.myClient = MongoClient()
        self.db = self.myClient.codeWizard
        self.posts = self.db.posts

    def insert_post(self, data):
        self.posts.insert_one(data)
        return True

    def all_post(self):
        all_post = self.posts.find()
        new_post = []
        for post in all_post:
            post['timestamp'] = humanize.naturaltime(datetime.datetime.now() - post['created_on'])
            new_post.append(post)

        return new_post


    # def all_post(self, username):
    #     all_post = self.posts.find({"username": username})
    #     new_post = []
    #     for post in all_post:
    #         post['timestamp'] = humanize.naturaltime(datetime.datetime.now() - post['created_on'])
    #         new_post.append(post)
    #
    #     return new_post
