from vehicle import Vehicle
from car import Car
from van import Van
from garage import Garage
from exceptions import VehicleNotFoundException

def main():
    garage = Garage()

    garage.add_vehicle(Car(123, "Ford", "Escort", 75495, 1991, False, False, False))
    garage.add_vehicle(Car(456, "Tesla", "Model S", 35982, 2023, True, True, True))
    garage.add_vehicle(Van(789, "Merdedes", "Sprinter", 362895, 2021, True, True))

    vehicle = choose_vehicle(garage)
    choose_action(vehicle)

def choose_vehicle(garage: Garage):
    vehicle_id = None
    vehicle = None

    while vehicle == None:
        try:
            vehicle_id = int(input("Enter the vehicle ID: "))
        except ValueError:
            print("Vehicle ID must be a number!")
            continue
        try:
            vehicle = garage.get_vehicle(vehicle_id)
        except VehicleNotFoundException:
            print(f"Could not find vehicle: {vehicle_id}")
            continue

    return vehicle

def choose_action(vehicle: Vehicle):    
    while True:
        action = input("Choose an action:\n"
                "Wash (w)\n"
                "Quick Service (q)\n"
                "Full Service (f)\n")

        try:
            match action.lower():
                case "w": return vehicle.wash()
                case "q": return vehicle.service(False)
                case "f": return vehicle.service(True)
                case _: raise ValueError
        except ValueError:
            print("Invalid option. Try again.")

main()

