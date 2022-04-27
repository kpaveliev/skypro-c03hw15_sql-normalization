-- animals
SELECT *
FROM animals_old;

SELECT *
FROM animal_species;

SELECT *
FROM animal_colors;

SELECT *
FROM animal_breeds;

-- outcomes
SELECT *
FROM outcomes;

SELECT *
FROM outcome_types;

SELECT *
FROM outcome_subtypes;

-- all data animals
SELECT animals.id, animals.name, breed.breed, main_color.color, second_color.color
FROM animals
LEFT JOIN animal_breeds breed ON breed.id = animals.breed_id
LEFT JOIN animal_colors main_color ON main_color.id = animals.main_color_id
LEFT JOIN animal_colors second_color ON second_color.id = animals.second_color_id

-- all data outcomes
SELECT outcomes.id, outcomes.year,
       types.type, subtypes.subtype,
       animals.name, species.specie, breeds.breed, main_colors.color
FROM outcomes
    LEFT JOIN outcome_types types ON outcomes.type_id = types.id
    LEFT JOIN outcome_subtypes subtypes ON outcomes.subtype_id = subtypes.id
    LEFT JOIN animals ON animals.id = outcomes.animal_id
    LEFT JOIN animal_species species ON animals.specie_id = species.id
    LEFT JOIN animal_breeds breeds ON animals.breed_id = breeds.id
    LEFT JOIN animal_colors main_colors ON animals.main_color_id = main_colors.id

