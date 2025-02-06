from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_success_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_success_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_success_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        expected_result = len(burger.ingredients)-1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == expected_result

    def test_success_move_ingredient(self):
        burger = Burger()
        mock_first_ingredient = Mock()
        burger.add_ingredient(mock_first_ingredient)
        mock_second_ingredient = Mock()
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_second_ingredient
        assert burger.ingredients[1] == mock_first_ingredient

    def test_success_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        bun_price = mock_bun.get_price.return_value = 500
        mock_ingredient = Mock()
        ingredient_price = mock_ingredient.get_price.return_value = 250
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = bun_price * 2 + ingredient_price
        assert burger.get_price() == price

    def test_success_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 500
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Соус Spicy-X'
        mock_ingredient.get_type.return_value = 'sauce'
        mock_ingredient.get_price.return_value = 250
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= sauce Соус Spicy-X =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '\nPrice: 1250')
        assert burger.get_receipt() == expected_result

