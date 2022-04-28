import pytest
from dao import OutcomesDAO
from config import DB_PATH

@pytest.fixture()
def outcomes_db():
    return OutcomesDAO(DB_PATH)
