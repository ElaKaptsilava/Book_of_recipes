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
            pass
        elif choice == 2:
            recipes.show_recipes()


class Recipes:
    def add_ingridients(self):
        pass

    def add_Instruction(self):
        pass

    def show_recipes(self):
        pass


class Ingredients(Recipes):
    pass


class Instruction(Recipes):
    pass


def main():
    manager = Manager()
    manager.show()


if __name__ == '__main__':
    main()
