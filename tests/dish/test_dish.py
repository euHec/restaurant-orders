import pytest
from src.models.ingredient import Ingredient, Restriction
from src.models.dish import Dish


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("Bife Acebolado", "24.99")

    with pytest.raises(ValueError):
        Dish("Bife Acebolado", -24.99)

    dish = Dish("Omelete", 24.99)
    dish1 = Dish("moqueca de camarão", 120.00)

    assert dish.name == "Omelete"
    assert dish.price == 24.99
    assert dish.recipe == {}

    ovo = Ingredient("ovo")

    dish.add_ingredient_dependency(ovo, 2)

    assert len(dish.recipe) == 1
    assert ovo in dish.recipe
    assert dish.recipe[ovo] == 2

    assert dish == dish
    assert dish != dish1

    assert hash(dish) == hash(dish)
    assert hash(dish) != hash(dish1)

    assert repr(dish) == "Dish('Omelete', R$24.99)"

    restrictions = dish.get_restrictions()

    assert Restriction.ANIMAL_DERIVED in restrictions

    ingredients = dish.get_ingredients()

    assert ovo in ingredients
