from abc import ABC, abstractmethod
from typing import final

class Vehicle(ABC):
    def __init__(self, id: int, make: str, model: str, milage: int, year: int, mot: bool):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._milage = milage
        self._mot = mot

    @property
    def id(self):
        return self._id

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    @property
    def milage(self):
        return self._milage

    @milage.setter
    def milage(self, value: int):
        self._milage = value

    @property
    def mot(self):
        return self._mot

    @mot.setter
    def mot(self, value: bool):
        self._mot = value

    @final
    def _description(self):
        return f"{self.year} {self.make} {self.model}"

    @abstractmethod
    def service(self, full_service: bool) -> str:
        pass

    @abstractmethod
    def wash(self) -> str:
        pass