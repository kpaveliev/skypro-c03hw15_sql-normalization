-- supporting tables
CREATE TABLE animal_breeds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed TEXT
);

CREATE TABLE animal_species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    specie TEXT
);

CREATE TABLE animal_colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT
);

-- main table
CREATE TABLE animals (
    id TEXT PRIMARY KEY,
    name TEXT,
    date_of_birth DATETIME,
    specie_id INTEGER,
    breed_id INTEGER,
    main_color_id INTEGER,
    second_color_id INTEGER,
    FOREIGN KEY (specie_id) REFERENCES animal_species (id),
    FOREIGN KEY (breed_id) REFERENCES animal_breeds (id),
    FOREIGN KEY (main_color_id) REFERENCES animal_colors (id),
    FOREIGN KEY (second_color_id) REFERENCES animal_colors (id)
);

