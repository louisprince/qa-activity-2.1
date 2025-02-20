from car import Car
from van import Van
from garage import Garage

# Create a method in Garage that iterates through each Vehicle, calculating a bill for each type of Vehicle in a different way, depending on the type of Vehicle it is (this does not need to be complex).

# Garage should have methods that add a Vehicle, remove a Vehicle by its ID or its type, fix a Vehicle (which calculates the bill), and to empty the Garage.

# Garage should have a method to remove multiple Vehicles by their type.

def main():
    garage = Garage()

    garage.add_vehicle(Car(123, "Ford", "Escort", 75495, 1991, False, False, False))
    garage.add_vehicle(Car(456, "Tesla", "Model S", 35982, 2023, True, True, True))
    garage.add_vehicle(Van(789, "Merdedes", "Sprinter", 362895, 2021, True, True))

    try:
        garage.get_vehicle(321).wash()
    except Exception:
        print("Vehicle not found!")

    try:
        garage.get_vehicle(123).wash()
    except Exception:
        print("Vehicle not found!")

main()

