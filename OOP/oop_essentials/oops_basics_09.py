# Changing Class and Object Variables/Attributes


class Car:
    no_of_tires = 4

    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""
        self.moon_roof = ""
        self.engine_running = ""

    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False


def main():
    print("Hello from the main() method!")
    car1 = Car()
    car2 = Car()

    car1.make = "Tesla"
    car1.model = "Model 3"
    car1.color = "Red"
    car1.year = 2020
    car1.moon_roof = True

    print("Printing car1 details:".center(50, "-"))
    print("Make : {}".format(car1.make))
    print("Model : {}".format(car1.model))
    print("Year : {}".format(car1.year))
    print("Color : {}".format(car1.color))
    print("Moon Roof : {}".format(car1.moon_roof))

    print("Class Attributes:".center(50, "-"))
    print("car1:", car1.no_of_tires)
    Car.no_of_tires = 25
    print("car1:", car1.no_of_tires)
    print("car2:", car2.no_of_tires)



if __name__ == '__main__':
    main()
