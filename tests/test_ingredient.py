from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
import pytest


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15],
                                 [INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424]
                             ]
                             )
    def test_success_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15],
                                 [INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424]
                             ]
                             )
    def test_success_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15],
                                 [INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424]
                             ]
                             )
    def test_success_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

