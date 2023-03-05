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
            user_choice = str(input())
            self.conditions_choice(choice=user_choice)

    def conditions_choice(self, choice):
        recipes = Recipes()
        if choice == 1:
            recipes.show_menu()
        elif choice == 2:
            pass


class Recipes:
    recipes = {}

    def show_menu(self):
        print('Enter recipe name: ')
        enter_name_recipe = input()
        self.recipe_name(recipe_name=enter_name_recipe)

    def recipe_name(self, recipe_name):
        pass

    def recipe_ingridients(self):
        pass

    def recipe_instruction(self):
        pass

    def show_recipes(self):
        pass


def main():
    manager = Manager()
    manager.show()


if __name__ == '__main__':
    main()
