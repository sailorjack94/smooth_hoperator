DROP TABLE IF EXISTS beers;
DROP TABLE IF EXISTS brewers;


CREATE TABLE brewers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

CREATE TABLE beers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    style VARCHAR(255),
    stock INT,
    buy_price FLOAT,
    sell_price FLOAT,
    brewer_id INT REFERENCES brewers(id) ON DELETE CASCADE
);