# Methods


class Car:
    
    no_of_tires = 4

    
    def __init__(self):
        
        self.make = "Ford"
        self.model = "Mustang"
        self.year = 2010
        self.color = "Blue"
        self.moon_roof = True
        self.engine_running = False

    
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False
