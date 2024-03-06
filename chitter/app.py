import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.my_posts_repository import MyPostsRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/posts')
def get_posts():
    connection = get_flask_database_connection(app)
    mypostsrepo = MyPostsRepository(connection)
    myposts = mypostsrepo.all()
    return render_template('chitter.html', myposts=myposts)

# == Example Code Below ==

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))