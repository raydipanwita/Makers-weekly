"""
# USER STORY
"""

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

# Nouns:
message
chitter
peeps
reverse chronological order
time of the peep made
sign up

# Verbs
let people know what I am doing
I can see
appreciate the context of peep
post messages 

1. Design and create the Table
If the table is already created in the database, you can skip this step.

Otherwise, follow this recipe to design and create the SQL schema for your table.

In this template, we'll use an example table students

# EXAMPLE

Table: my_posts

Columns:
id | my_messages | time

Table: other_posts

Columns:
id | other_meesages | time


2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

-- EXAMPLE
-- (file: spec/seeds_chitter.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql

3. Define the class names
Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

# EXAMPLE
# Table name: my_posts

# Model class
# (in lib/my_posts.py)
class MyPosts


# Repository class
# (in lib/my_posts_repository.py)
class MyPostsRepository

4. Implement the Model class
Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

# EXAMPLE
# Table name: my_posts

# Model class
# (in lib/my_posts.py)

class MyPosts:
    def __init__(self, id, messages, time):
        self.id = 0
        self.messages = ""
        self.time = ""

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'
You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.

5. Define the Repository Class interface
Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# EXAMPLE
# Table name: my_posts

# Repository class
# (in lib/my_posts.py)

class MyPostsRepository():

    # Selecting all records
    # No arguments

    def all():
        # Executes the SQL query:
        # SELECT id, messages, time FROM my_posts;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)

    def find(id):
        # Executes the SQL query:
        # SELECT id, messages, time FROM my_posts WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(my_posts)
    # 

    # def update(my_posts)
    # 

    # def delete(my_posts)
    # 
6. Write Test Examples
Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

# EXAMPLES

# 1
# Get all my_posts

repo = MyPostsRepository()

myposts = repo.all()

len(myposts) # =>  2

myposts[0].id # =>  1
myposts[0].messages # =>  'Today I am trying something new'
myposts[0].time # =>  'April 2022'

myposts[1].id # =>  2
myposts[1].messsages # =>  'Breakie time'
myposts[1].time # =>  'May 2022'

# 2
# Get a single my_posts

repo = MyPostsRepository()

myposts = repo.find(1)

myposts.id # =>  1
myposts.name # =>  'Today I am trying something new'
myposts.cohort_name # =>  'April 2022'

# Add more examples for each method
Encode this example as a test.

7. Test-drive and implement the Repository class behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

