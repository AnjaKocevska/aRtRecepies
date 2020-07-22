CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS recipe(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    long_name TEXT NOT NULL,
    long_description TEXT NOT NULL,
    process_image TEXT,
    final_image TEXT,
    anjas_drawing TEXT,
    section TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ingredients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipe (id)
);

CREATE TABLE IF NOT EXISTS instructions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    number INTEGER,
    text TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipe (id)
);