import pytest
from app import app

class TestAPI():

    @pytest.mark.parametrize(
        "id", ['1', '1000', '10000']
    )
    def test_json(self, id):
        response = app.test_client().get(f'/{id}')
        data = response.json
        return_type = type(data)
        assert isinstance(data, dict), f'Ошибка в возвращаемом типе: ' \
                                                   f'должен быть dict, ' \
                                                   f'возвращается {return_type}'