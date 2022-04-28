import pytest

class TestOutcomesDAO:
    pass

class TestGetOutcomesById(TestOutcomesDAO):

    @pytest.mark.parametrize(
        "id, correct_return_type",
        [('1', dict), ('20', dict)]
    )
    def test_search(self, outcomes_db, id, correct_return_type):
        query_result = outcomes_db.get_outcome_by_id(id)
        return_type = type(query_result)
        assert return_type == correct_return_type, f'Ошибка в возвращаемом типе: ' \
                                                   f'должен быть {correct_return_type}, ' \
                                                   f'возвращается {return_type}'

    @pytest.mark.parametrize(
        "id", ['text', '$%', '1.1', '210,1', '-1']
    )
    def test_type_error(self, outcomes_db, id):
        with pytest.raises(TypeError):
            outcomes_db.get_outcome_by_id(id)


    @pytest.mark.parametrize(
        "id", ['50000', '30000']
    )
    def test_value_error(self, outcomes_db, id):
        with pytest.raises(ValueError):
            outcomes_db.get_outcome_by_id(id)
