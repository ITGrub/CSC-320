#-------------------------------------------
# Program Name: New/Used Car Dealership Inventory
# Author: Brian Holden
# Date: 3 August, 2024
#-------------------------------------------
# Pseudocode: The program begins by setting up an Automobile focused Class and
# begins initiating the defined components that will be used within the code.
# Next I defined how the components will accept input from the coder via the
# self input functions along with defining how the set components will be sorted 
# for printing to the text file at the end. Next I defined adding, removing, and
# updating vehicles. Lastly I gave the script an execution to output the Inventory
# to a text file for ease of reading, saving, and printing for later use.
#-------------------------------------------
# Program Input: List of Vehicles and Information about them.
# Program Output: List of Vehicles with Information.
#-------------------------------------------
class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    # Information Getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    # Information Setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_color(self, color):
        self.__color = color

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def __str__(self):
        return f"{self.__year} {self.__make} {self.__model}, Color: {self.__color}, Mileage: {self.__mileage}"

class DealershipInventory:
    def __init__(self):
        self.inventory = []

    def add_vehicle(self, automobile):
        self.inventory.append(automobile)

    def remove_vehicle(self, index):
        if 0 <= index < len(self.inventory):
            self.inventory.pop(index)
        else:
            print("Invalid index. Vehicle not found.")

    def update_vehicle(self, index, make=None, model=None, color=None, year=None, mileage=None):
        if 0 <= index < len(self.inventory):
            if make:
                self.inventory[index].set_make(make)
            if model:
                self.inventory[index].set_model(model)
            if color:
                self.inventory[index].set_color(color)
            if year:
                self.inventory[index].set_year(year)
            if mileage:
                self.inventory[index].set_mileage(mileage)
        else:
            print("Invalid index. Vehicle not found.")

    def output_inventory(self, filename):
        with open(filename, 'w') as file:
            for vehicle in self.inventory:
                file.write(str(vehicle) + '\n')

def main():
    dealership = DealershipInventory()

    # Adding some vehicles
    dealership.add_vehicle(Automobile("Toyota", "Camry", "White", 2020, 15940))
    dealership.add_vehicle(Automobile("Honda", "Civic", "Blue", 2019, 29000))
    dealership.add_vehicle(Automobile("Ford", "Mustang", "Black", 2018, 30250))
    dealership.add_vehicle(Automobile("Volkswagen", "Jetta", "Black", 2020, 26252))
    dealership.add_vehicle(Automobile("Toyota", "Supra", "Purple", 2024, 569))
    dealership.add_vehicle(Automobile("Toyota", "GT86", "Black", 2020, 19000))
    dealership.add_vehicle(Automobile("Toyota", "Camry", "White", 1999, 180000))
    dealership.add_vehicle(Automobile("Chevorlet", "Silverado", "Green", 2022, 45000))
    dealership.add_vehicle(Automobile("Toyota", "Tundra", "Orange", 2024, 1000))
    dealership.add_vehicle(Automobile("Ford", "F150 Raptor Custom", "OD Green", 2024, 250))

    # Updating vehicles
    dealership.update_vehicle(1, color="Green", mileage=22000)
    dealership.update_vehicle(5, color="Burgandy", mileage=19500)

    # Removing a vehicle
    dealership.remove_vehicle(2)

    # Outputting inventory to a text file
    dealership.output_inventory("Vechicle Inventory.txt")

if __name__ == "__main__":
    main()
