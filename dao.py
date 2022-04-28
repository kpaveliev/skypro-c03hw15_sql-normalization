import sqlite3

class OutcomesDAO:

    def __init__(self, path: str) -> None:
        """Path to the database needs to be submitted when creating dao object"""
        self.path = path


    def query_database(self, sql_query: str, *args) -> list:
        """Create connection and pass query

        :param sql_query: SQL query which needs to be made
        :param *args: Arguments to be added to the query
        :return: List with the query results
        """
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(sql_query, args)
            query_result = cursor.fetchall()
        return query_result

    def count_records(self) -> int:
        """Get total number of rows in the database"""
        # Query the database
        sql_query = """
                SELECT COUNT()
                FROM outcomes
        """
        query_result = self.query_database(sql_query)
        records_number = query_result[0][0]
        return records_number

    def get_outcome_by_id(self, id: str) -> dict:
        """Get outcome details by id

        :param id: Outcome id to look for
        :return: Dictionary with the selected fields for the outcome found
        :raise TypeError: If value passed is not number
        :raise ValueError: If value passed is outside range of possible numbers
        """
        # Get total number of records in the database and check if id meet conditions
        records_number = self.count_records()

        if not id.isdigit():
            raise TypeError(f'ID passed ({id}) is not positive integer, '
                            f'only positive integers in range 0-{records_number} accepted')
        elif not 0 <= int(id) <= records_number:
            raise ValueError(f'ID passed ({id}) is not found in the database, '
                             f'value should be in range 0-{records_number}')

        # Query the database if value is okay
        else:
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
            query_result = self.query_database(sql_query, id)

            # Make a dictionary with the query results
            outcome_found = {
                'id': query_result[0][0],
                'year': query_result[0][1],
                'type': query_result[0][2],
                'subtype': query_result[0][3],
                'animal_name': query_result[0][4],
                'animal_specie': query_result[0][5],
                'animal_breed': query_result[0][6],
                'animal_main_color': query_result[0][7]
            }

        return outcome_found
