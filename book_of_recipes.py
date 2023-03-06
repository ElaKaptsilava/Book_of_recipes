class Manager:
    def show(self):
        menu = Menu()
        menu.make_choice()


class Menu(Manager):
    def __init__(self):
        self.recipes = Recipe()

    def make_choice(self):
        manager_menu = '1. Add a new recipe\n2. Show all recipes\n3. Would you like to return to the choice?'

        while True:
            print(manager_menu)
            user_choice = input()
            if not user_choice:
                break
            self.conditions_choice(choice=user_choice)

    def conditions_choice(self, choice):
        if choice == '1':
            self.recipes.recipe_name()
        elif choice == '2':
            self.recipes.show_recipes()


class Recipe(Manager):
    recipes = []

    def __init__(self):
        self.name = []
        self.ingridients = []
        self.instruction = []

    def __repr__(self):
        return f'{self.name}:\n {self.ingridients}\n\n{self.instruction}'

    def __str__(self):
        return f'{self.name}:\n {self.ingridients}\n\n{self.instruction}'

    def recipe_name(self):
        print('Enter recipe name: ')
        recipe_name = input()
        self.name = recipe_name
        print(f'Enter the ingredients needed for cooking "{recipe_name}":')
        self.recipe_ingridients()

    def recipe_ingridients(self):
        while True:
            enter_ingridients = input()
            if not enter_ingridients:
                break
            self.ingridients = enter_ingridients.split()
        print(f'Enter the instructions:')
        self.recipe_instruction()

    def recipe_instruction(self):
        while True:
            enter_instruction = input()
            if not enter_instruction:
                break
            self.instruction = enter_instruction

    def make_recipe_book(self):
        #self.recipes[self.name] = {'Ingridients': self.ingridients, 'Instructions': self.instruction}
        pass

    def show_recipes(self):
        for name in self.name:
            print(name)
        for ingridients in self.ingridients:
            print(ingridients)
        for number, instruction in enumerate(self.instruction, 1):
            print(instruction)


def main():
    manager = Manager()
    manager.show()


if __name__ == '__main__':
    main()
