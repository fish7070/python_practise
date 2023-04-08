# Understanding Polymorphism using class methods


class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The dog ({}) is {} now!".format(self.name, "moving"))

    def run(self):
        print("The dog ({}) is {} now!".format(self.name, "running"))

    def swim(self):
        print("The dog ({}) is {} now!".format(self.name, "swimming"))

    def jump(self):
        print("The dog ({}) is {} now!".format(self.name, "jumping"))

    def make_sound(self):
        print("The dog ({}) is {} now!".format(self.name, "barking"))


class Cat:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The cat ({}) is {} now!".format(self.name, "moving"))

    def run(self):
        print("The cat ({}) is {} now!".format(self.name, "running"))

    def swim(self):
        print("The cat ({}) is {} now!".format(self.name, "swimming"))

    def jump(self):
        print("The cat ({}) is {} now!".format(self.name, "jumping"))

    def make_sound(self):
        print("The cat ({}) is {} now!".format(self.name, "meowing"))


class Snake:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The snake ({}) is {} now!".format(self.name, "moving"))

    def run(self):
        print("Snakes can not {}!".format(self.name, "run"))

    def swim(self):
        print("The snake ({}) is {} now!".format(self.name, "swimming"))

    def jump(self):
        print("Some snakes jump. But, I ({}) can not {}".format(self.name, "jump"))

    def make_sound(self):
        print("The snake ({}) is {} now!".format(self.name, "hissing"))


def main():
    dog1 = Dog("Jimmy")
    cat1 = Cat("Kitty")
    snake1 = Snake("Scotch")

    animals_list = [dog1, cat1, snake1]
    
    for animal in animals_list:
        print(type(animal))
        animal.make_sound()


if __name__ == "__main__":
    main()
