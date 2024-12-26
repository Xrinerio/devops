CREATE TABLE IF NOT EXISTS mydb (
    id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    username TEXT NOT NULL, -- Content of the note
    email TEXT NOT NULL UNIQUE     -- Date associated with the note
);