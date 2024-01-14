import unittest
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501

ANIMAL_DERIVED = "ANIMAL_DERIVED"
ANIMAL_MEAT = "ANIMAL_MEAT"
SEAFOOD = "SEAFOOD"
LACTOSE = "LACTOSE"
GLUTEN = "GLUTEN"


# Req 1
def test_ingredient():
    pass


def test_same_ingredient_has_same_hash():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert hash(ingredient1) == hash(ingredient2)


def test_different_ingredient_has_different_hash():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)


def test_equal_ingredients_are_equal():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2


def test_different_ingredients_are_not_equal():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 != ingredient2


def test_repr_returns_correct_value():
    ingredient = Ingredient("queijo mussarela")
    assert repr(ingredient) == "Ingredient('queijo mussarela')"


def test_name_attribute_correct():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"


def test_restrictions_attribute_correct():
    ingredient = Ingredient("queijo mussarela")
    expected_restrictions = {LACTOSE, ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions


def test_incorrect_name_attribute_fails():
    ingredient = Ingredient("queijo mussarela")
    expected_name = "queijo cheddar"
    assert (
        ingredient.name == expected_name
    ), f"Expected: {expected_name}, Actual: {ingredient.name}"


def test_incorrect_restrictions_attribute_fails():
    ingredient = Ingredient("queijo mussarela")
    expected_restrictions = {LACTOSE, GLUTEN}
    assert (
        ingredient.restrictions == expected_restrictions
    ), f"Expected: {expected_restrictions}, Actual: {ingredient.restrictions}"


if __name__ == "__main__":
    unittest.main()
