from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
import pytest
import data


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, data.sause_name, data.sause_price],
                                 [INGREDIENT_TYPE_FILLING, data.filling_name, data.filling_price]
                             ]
                             )
    def test_success_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, data.sause_name, data.sause_price],
                                 [INGREDIENT_TYPE_FILLING, data.filling_name, data.filling_price]
                             ]
                             )
    def test_success_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, data.sause_name, data.sause_price],
                                 [INGREDIENT_TYPE_FILLING, data.filling_name, data.filling_price]
                             ]
                             )
    def test_success_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

