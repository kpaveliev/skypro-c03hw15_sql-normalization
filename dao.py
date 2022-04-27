import sqlite3

class OutcomesDAO:

    def __init__(self, path: str) -> None:
        """Path to the database needs to be submitted when creating dao object"""
        self.path = path

    def get_outcome_by_id(self, id: int) -> dict:
        """Get outcome details by id

        :param id: Outcome id
        # :return: Dictionary with title, country, release year, genre, description
        # :raise ValueError: If title not found
        """
        # Query results from the database
        with sqlite3.connect(self.path) as connection:

            cursor = connection.cursor()
            sql_query = """
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
                    WHERE outcomes.id = :id             
            """
            cursor.execute(sql_query, {'id': id})
            query_result = cursor.fetchone()
        # Make a dictionary with the query results
        if query_result is not None:
            outcome_found = {
                'id': query_result[0],
                'year': query_result[1],
                'type': query_result[2],
                'subtype': query_result[3],
                'animal_name': query_result[4],
                'animal_specie': query_result[5],
                'animal_breed': query_result[6],
                'animal_main_color': query_result[7]
            }
        else:
            raise ValueError(f'{id} not found in the database')
        return outcome_found

if __name__ == "__main__":
    from config import DB_PATH
    db = OutcomesDAO(DB_PATH)
    result = db.get_outcome_by_id(1)
    print(result)
