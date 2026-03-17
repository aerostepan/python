#We can put this class in a different python file and the import it into our script
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color 
        self.for_sale = for_sale 
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def describe(self):
        print(f"Model of the car: {self.model}")
        print(f"Manufacturing year: {self.year}")
        print(f"Color of the car: {self.color}")
        if self.for_sale:
            print("This car is for sale")
        else:
            print("This car is not for sale")

car1 = Car("BMW", 2025, "red", True)
car2 = Car("MB", 2025, "blue", False)
car3 = Car("Charger", 2023, "black", True)

car1.drive()
car2.stop()
car3.describe()