class Manager:
    def show(self):
        menu = Menu()
        menu.show_menu()


class Menu(Manager):
    def show_menu(self):
        manager_menu = '1. Add a new recipe\n2. Show all recipes\n3. Would you like to return to the choice?'
        print(manager_menu)
        self.make_choice()

    def make_choice(self):
        while True:
            user_choice = input()
            self.conditions_choice(choice=user_choice)

    def conditions_choice(self, choice):
        recipes = Recipe()
        if choice == '1':
            recipes.show_menu()
        elif choice == '2':
            pass


class Recipe:
    recipes = {}
    def __init__(self):
        self.name = []
        self.recipe_ingridients = []
        self.recipe_instruction = []

    def show_menu(self):
        print('Enter recipe name: ')
        enter_name_recipe = input()
        self.recipe_name(recipe_name=enter_name_recipe)

    def recipe_name(self, recipe_name):
        self.name.append(recipe_name)
        print(f'Enter the ingredients needed for cooking "{recipe_name}":')
        enter_ingridients = input()
        self.add_recipe_ingridients(ingridients=enter_ingridients)

    def add_recipe_ingridients(self, ingridients):
        self.recipe_ingridients.append(ingridients)
        print(f'Enter the instructions:')
        enter_instruction = input()
        self.add_recipe_instruction(instructions=enter_instruction)

    def add_recipe_instruction(self, instructions):
        pass

    def show_recipes(self):
        pass


def main():
    manager = Manager()
    manager.show()


if __name__ == '__main__':
    main()
