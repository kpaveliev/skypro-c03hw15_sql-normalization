-- populate breeds
INSERT INTO animal_breeds (breed)
SELECT DISTINCT animals_old.breed
FROM animals_old;

-- populate species table
INSERT INTO animal_species (specie)
SELECT DISTINCT animals_old.animal_type
FROM animals_old;

-- populate colors table
INSERT INTO animal_colors (color)
SELECT DISTINCT animals_old.color1 FROM animals_old
UNION
SELECT DISTINCT animals_old.color2 FROM animals_old;

-- populate animals table
INSERT INTO animals (id, name, date_of_birth, specie_id, breed_id, main_color_id, second_color_id)
SELECT DISTINCT animals_old.animal_id, animals_old.name, animals_old.date_of_birth,
                animal_species.id, animal_breeds.id, main_color.id, second_color.id
FROM animals_old
LEFT JOIN animal_breeds ON animal_breeds.breed = animals_old.breed
LEFT JOIN animal_species ON animal_species.specie = animals_old.animal_type
LEFT JOIN animal_colors main_color ON main_color.color = animals_old.color1
LEFT JOIN animal_colors second_color ON second_color.color = animals_old.color2;