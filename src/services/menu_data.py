import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.source(source_path)

    def source(self, source_path):
        with open(source_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader, None)

            for row in csv_reader:
                row_name, row_price, row_ingredient, row_quantity = row
                price = float(row_price)
                quantity = int(row_quantity)

                new_dish = next(
                    (d for d in self.dishes if d.name == row_name), None
                )
                if new_dish is None:
                    new_dish = Dish(row_name, price)
                    self.dishes.add(new_dish)

                new_ingredient = Ingredient(row_ingredient)
                new_dish.add_ingredient_dependency(new_ingredient, quantity)
