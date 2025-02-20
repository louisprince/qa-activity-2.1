from vehicle import Vehicle
from exceptions import VehicleNotFoundException

class Garage:
    def __init__(self):
        self.__vehicles: list[Vehicle] = []

    @property
    def vehicles(self):
        return self.__vehicles
    
    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)

    def get_vehicle(self, id: int):
        for vehicle in self.__vehicles:
            if vehicle.id == id:
                return vehicle
        raise VehicleNotFoundException
