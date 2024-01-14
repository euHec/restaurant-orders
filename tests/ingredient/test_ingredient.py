import unittest
from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("bacon")

    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)
    assert hash(ingredient2) == hash(ingredient3)
    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient1
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"


if __name__ == "__main__":
    unittest.main()
