CREATE TABLE product (
    category INTEGER,
    id VARCHAR(40) PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(255),
    model VARCHAR(255),
    description VARCHAR(4000),
    price INTEGER,
    currency VARCHAR(1),
    add_time TIMESTAMP
);
CREATE TABLE laptop(
    id VARCHAR(40) PRIMARY KEY,
    processor VARCHAR(255),
    ram INTEGER,
    display_size FLOAT,
    display_quality VARCHAR(255),
    ssd BOOLEAN,
    storage_size INTEGER,
    graphics BOOLEAN,
    vram INTEGER,
    FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
);
CREATE TABLE tablet(
    id VARCHAR(40) PRIMARY KEY,
    processor VARCHAR(255),
    ram INTEGER,
    display_size FLOAT,
    display_quality VARCHAR(255),
    network BOOLEAN,
    storage_size INTEGER,
    FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
);
CREATE TABLE smartphone(
    id VARCHAR(40) PRIMARY KEY,
    processor VARCHAR(255),
    ram INTEGER,
    display_size FLOAT,
    display_quality VARCHAR(255),
    dual_sim BOOLEAN,
    storage_size INTEGER,
    FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
);
CREATE TABLE review(
    id VARCHAR(40) PRIMARY KEY,
    grade FLOAT,
    description VARCHAR(4000),
    FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
);
CREATE TABLE basket(
    user VARCHAR(40),
    product VARCHAR(40),
    FOREIGN KEY (product) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
    FOREIGN KEY (user) REFERENCES costumers(id) on DELETE CASCADE on UPDATE CASCADE
)



