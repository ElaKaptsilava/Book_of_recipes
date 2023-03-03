class Manager:
    def show(self):
        menu = Menu()
        menu.show_menu()

class Menu(Manager):
    def show_menu(self):
        manager_menu = '''1. Add a new recipe
        2. Show all recipes
        3. Would you like to return to the choice?
        '''
        self.show_choice()

    def show_choice(self):
        user_choice = str(input())
        self.make_choice(choice=user_choice)

    def make_choice(self, choice):
        pass

class Recipes:
    pass

class Ingredients(Recipes):
    pass

class Instrukcja(Recipes):
    pass