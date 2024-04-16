import pytest

from src import pypotage


class TestChef(pypotage.Chef):
    def prepare(self, ingredient):
        ingredient.formula._id = "test"
        ingredient.formula._type = str
        return ingredient

    def cook(self, line):
        line.formula._type = str
        return line


@pytest.fixture(autouse=True)
def reset():
    pypotage.pot.ingredients.clear()


def test_preparechefline_works():
    @pypotage.prepare
    def bean_1():
        return 1

    assert pypotage.cook(int).take_out() == 1

    pypotage.pot.chefs.append(TestChef())

    @pypotage.prepare
    def bean_2():
        return 1

    assert pypotage.cook(int, "test").take_out() == 1
