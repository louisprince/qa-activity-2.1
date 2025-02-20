from car import Car
from van import Van

#  create three derived classes (Car, Motorbike, etc.). Each derived class should have its own attributes in addition to the normal Vehicle attributes.

# Using a List<> implementation, store all your Vehicles in a Garage class.

# Create a method in Garage that iterates through each Vehicle, calculating a bill for each type of Vehicle in a different way, depending on the type of Vehicle it is (this does not need to be complex).

# Garage should have methods that add a Vehicle, remove a Vehicle by its ID or its type, fix a Vehicle (which calculates the bill), and to empty the Garage.

# Garage should have a method to remove multiple Vehicles by their type.

def main():
    car1 = Car("Ford", "Escort", 75495, 1991, False, False, False )
    car1.service(False)
    car1.wash()

    car2 = Car("Tesla", "Model S", 35982, 2023, True, True, True)
    car2.service(True)
    car2.wash()

    van1 = Van("Merdedes", "Sprinter", 362895, 2021, True, True)
    van1.service(False)
    van1.wash()

main()

