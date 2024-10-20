Correction made: Added the internal documentation for the project to the top of the source code.
#-------------------------------------------
# Program Name: Module 2 Critical Thinking
# Author: Brian Holden
# Date: 25 June, 2024
#-------------------------------------------
# Pseudocode: The user is asked to input a vehicle brand, model, year, starting odometer, ending, 
# odometer, and miles per gallon of the vehicle. Once the user inputs this information, the 
# program then processes what was entered and prints out, in order, what the user inputs using a 
# dictionary function.
#-------------------------------------------
# Program Brand Input: Ford
# Program Model Input: Mustang
# Program Year Input: 2024
# Program Starting Odometer Input: 4
# Program Ending Odometer Input: 216
# Program Miles Per Gallon Input: 24
# Program Output: 2024 Ford Mustang, 4 Starting miles, 216 Ending miles, 24 Miles per gallon
#-------------------------------------------
brand = input("Enter the brand of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")
starting_odometer = input("Enter the starting odometer reading: ")
ending_odometer = input("Enter the ending odometer reading: ")
miles_per_gallon = input("Enter the estimated miles per gallon consumed by the vehicle: ")

vehicle_information = {
    "brand": brand,
    "model": model,
    "year": year,
    "starting_odometer": starting_odometer,
    "ending_odometer": ending_odometer,
    "miles_per_gallon": miles_per_gallon
}
print(vehicle_information["year"],vehicle_information["brand"],vehicle_information["model"])
print(vehicle_information["starting_odometer"], "Starting miles")
print(vehicle_information["ending_odometer"], "Ending miles")
print(vehicle_information["miles_per_gallon"], "Miles per gallon")
