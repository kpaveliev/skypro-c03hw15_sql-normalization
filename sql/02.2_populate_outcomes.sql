-- populate types
INSERT INTO outcome_types (type)
SELECT DISTINCT animals_old.outcome_type
FROM animals_old;

-- populate subtypes
INSERT INTO outcome_subtypes (subtype)
SELECT DISTINCT animals_old.outcome_subtype
FROM animals_old;

-- populate main outcomes table
INSERT INTO outcomes (id, month, year, age_upon_outcome, animal_id, type_id, subtype_id)
SELECT DISTINCT animals_old."index", animals_old.outcome_month, animals_old.outcome_year,
                animals_old.age_upon_outcome, animals_old.animal_id, outcome_types.id, outcome_subtypes.id
FROM animals_old
LEFT JOIN outcome_types ON outcome_types.type = animals_old.outcome_type
LEFT JOIN outcome_subtypes ON outcome_subtypes.subtype = animals_old.outcome_subtype;