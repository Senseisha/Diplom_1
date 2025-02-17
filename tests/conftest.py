import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    return bun


@pytest.fixture
def mock_first_ingredient():
    first_ingredient = Mock()
    return first_ingredient


@pytest.fixture
def mock_second_ingredient():
    second_ingredient = Mock()
    return second_ingredient


@pytest.fixture
def mock_sause():
    sause = Mock()
    sause.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sause.get_name.return_value = 'Соус традиционный галактический'
    sause.get_price.return_value = 15
    return sause


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = 'Биокотлета из марсианской Магнолии'
    filling.get_price.return_value = 424
    return filling

