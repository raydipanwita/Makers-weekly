-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS my_posts;
DROP SEQUENCE IF EXISTS my_posts_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS my_posts_seq;
CREATE TABLE my_posts (
    id SERIAL PRIMARY KEY,
    messages VARCHAR(255),
    time VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO my_posts (messages, time) VALUES ('Today I am trying something new', 'April 2022');
INSERT INTO my_posts (messages, time) VALUES ('Breakie time', 'May 2022');
