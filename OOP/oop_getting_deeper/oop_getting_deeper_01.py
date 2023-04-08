# Destructor


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

    def __del__(self):
        print("{} {} : Destructor Invoked!".format(self.make, self.model))

def main():
    print("Hello from the main() method!")
    car1 = Car("Ford", "Mustang", 2010, "Blue")
    car2 = Car("Tesla", "Model 3", 2020, "Red", True)

    print("Printing car1 details:".center(50, "-"))
    print("Make : {}".format(car1.make))
    print("Model : {}".format(car1.model))
    print("Year : {}".format(car1.year))
    print("Color : {}".format(car1.color))
    print("Moon Roof : {}".format(car1.moon_roof))

    print("Printing car2 details:".center(50, "-"))
    print("Make : {}".format(car2.make))
    print("Model : {}".format(car2.model))
    print("Year : {}".format(car2.year))
    print("Color : {}".format(car2.color))
    print("Moon Roof : {}".format(car2.moon_roof))

    print("Class Attributes:".center(50, "-"))
    print("car1:", car1.no_of_tires)
    print("car2:", car2.no_of_tires)
    print("Car:", Car.no_of_tires)

    print("Deleting Objects".center(50, "-"))
    del car2
    del car1
    del car2

if __name__ == '__main__':
    main()
