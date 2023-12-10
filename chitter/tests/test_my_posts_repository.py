from lib.my_posts_repository import *
from lib.my_posts import *

"""
When I call all
returns all posts
"""

def test_gets_all_post(db_connection):
    db_connection.seed("seeds/chitter.sql") # Seed our database with some test data
    repository = MyPostsRepository(db_connection) # Create a new ArtistRepository

    myposts = repository.all()

    assert myposts == [
        MyPosts(1, "Today I am trying something new", "April 2022"),
        MyPosts(2, "Breakie time", "May 2022"),
    ]