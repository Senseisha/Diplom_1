from praktikum.bun import Bun
import pytest
import data


class TestBun:
    @pytest.mark.parametrize('name, price',
                         [
                             [data.first_bun_name, data.first_bun_price],
                             [data.second_bun_name, data.second_bun_price]
                         ]
    )
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price',
                             [
                                 [data.first_bun_name, data.first_bun_price],
                                 [data.second_bun_name, data.second_bun_price]
                             ]
    )
    def test_bun_name_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
