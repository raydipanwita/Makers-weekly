from lib.my_posts import *

class MyPostsRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from my_posts')
        myposts = []
        for row in rows:
            posts = MyPosts(row["id"], row["messages"], row["time"])
            myposts.append(posts)
        return myposts
        