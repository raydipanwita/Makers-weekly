from lib.my_posts import *

def test_constructs_messages():
    my_posts = MyPosts(1, "Today I am trying something new", "April 2022")
    assert my_posts.id == 1
    assert my_posts.messages == "Today I am trying something new"
    assert my_posts.time == "April 2022"