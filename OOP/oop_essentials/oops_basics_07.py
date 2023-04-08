# Creating Objects


class Car:
    no_of_tires = 4

    def __init__(self, make, model, year, color, moon_roof=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False

    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False


def main():
    print("Hello from the main() method!")
    car1 = Car("Ford", "Mustang", 2010, "Blue")
    car2 = Car("Tesla", "Model 3", 2020, "Red", True)


if __name__ == '__main__':
    main()