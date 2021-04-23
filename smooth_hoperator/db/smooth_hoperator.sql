DROP TABLE IF EXISTS brewers;
DROP TABLE IF EXISTS beers;

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
    buy_cost INT,
    sell_price INT,
    brewer_id INT REFERENCES brewers(id) ON DELETE CASCADE
);