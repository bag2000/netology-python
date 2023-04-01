from pprint import pprint

class CookBook:
    def __init__(self, recipe_file: str):
        self.recipe_file = recipe_file
    
    def read_book(self):

        with open(self.recipe_file, 'rt') as file:

            cook_book = {}

            for line in file:
                recipe_name = line.strip()
                ingredient_count = int(file.readline().strip())
                recipe = []
                for _ in range(ingredient_count):
                    ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                    recipe.append({
                        'ingredient_name': ingredient_name,
                        'quantity': quantity,
                        'measure': measure
                    })
                file.readline()
                cook_book[recipe_name] = recipe

        return cook_book

    def get_shop_list_by_dishes(self, dishes: list, person_count: int):

        ingredients_to_buy = {}

        for recipe in dishes:
            ingredients = self.read_book().get(recipe)
            for ingridient in ingredients:
                ingredient_name = ingridient.get('ingredient_name')
                measure = ingridient.get('measure')
                quantity = int(ingridient.get('quantity'))
                if ingredient_name not in ingredients_to_buy:
                    ingredients_to_buy[ingredient_name]={
                        'measure': measure,
                        'quantity': quantity * person_count
                    }
                else:
                    ingridient = ingredients_to_buy.get(ingredient_name)
                    quantity = ingridient['quantity'] + quantity * person_count
                    ingredients_to_buy[ingredient_name]={
                        'measure': measure,
                        'quantity': quantity * person_count
                    }
        return ingredients_to_buy

cook_book = CookBook('recipes.txt')
pprint(cook_book.read_book(), width=100, indent=2, sort_dicts=False)
pprint(cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), width=100, indent=2, sort_dicts=False)