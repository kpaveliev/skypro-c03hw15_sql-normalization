-- supporting tables
CREATE TABLE outcome_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT
);

CREATE TABLE outcome_subtypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subtype TEXT
);

-- main table
CREATE TABLE outcomes (
    id INTEGER PRIMARY KEY,
    month INTEGER,
    year INTEGER,
    age_upon_outcome TEXT,
    animal_id TEXT,
    type_id INTEGER,
    subtype_id INTEGER,
    FOREIGN KEY (animal_id) REFERENCES animals (id),
    FOREIGN KEY (type_id) REFERENCES outcome_types (id),
    FOREIGN KEY (subtype_id) REFERENCES outcome_subtypes (id)
);



