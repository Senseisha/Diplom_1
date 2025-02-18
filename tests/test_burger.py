import data


class TestBurger:
    def test_success_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_success_add_ingredient(self, burger, mock_sause, mock_filling):
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2

    def test_success_remove_ingredient(self, burger, mock_sause, mock_filling):
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_filling)
        expected_result = len(burger.ingredients)-1
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == expected_result

    def test_success_move_ingredient(self, burger, mock_sause, mock_filling):
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == mock_filling.get_name()
        assert burger.ingredients[1].get_name() == mock_sause.get_name()

    def test_success_get_price(self, burger, mock_bun, mock_first_ingredient, mock_second_ingredient):
        bun_price = mock_bun.get_price.return_value = 988
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        first_ingredient_price = mock_first_ingredient.get_price.return_value = 88
        second_ingredient_price = mock_second_ingredient.get_price.return_value = 3000

        burger.set_buns(mock_bun)
        price = bun_price * 2 + first_ingredient_price + second_ingredient_price
        assert burger.get_price() == price

    def test_success_get_receipt(self, burger, mock_bun, mock_sause):

        mock_bun.get_name.return_value = data.first_bun_name
        mock_bun.get_price.return_value = data.first_bun_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sause)
        expected_result = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= sauce Соус традиционный галактический =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '\nPrice: 1991')
        assert burger.get_receipt() == expected_result

