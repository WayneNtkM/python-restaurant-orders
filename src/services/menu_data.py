import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.reader = self.__read_file_sorted(source_path)
        self.dishes = self.__menu_data_builder()

    def __read_file_sorted(self, source_path: str):
        with open(source_path, 'r') as file:
            reader = list(csv.DictReader(file))
            return reader

    def __menu_data_builder(self):
        dishes = set()
        for d in self.reader:
            dish = Dish(d["dish"], float(d["price"]))
            amount = int(d["recipe_amount"])
            ingredient = (Ingredient(d["ingredient"]))

            dishes.add(dish)

            my_tuple = tuple(dishes)

            my_tuple[0].add_ingredient_dependency(ingredient, amount)

        return dishes
