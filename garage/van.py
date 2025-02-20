from vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, make: str, model: str, milage: int, year: int, 
                 mot: bool, side_door: bool):
        super().__init__(make, model, milage, year, mot)
        self._side_door = side_door

    @property
    def side_door(self):
        return self._side_door

    def service(self, full_service: bool):
        if full_service is True:
            print(f"Performing a full service on the {self._description()}. "
                  "It needs a lot of work.")
        else: 
            print(f"Performing a quick service on the {self._description()}. "
                  "It doesn't need much doing to it.")    

    def wash(self):
        print(f"Giving the {self.year} {self.make} {self.model} van a wash. "
               "Best clear out the stuff in the back while we're at it.")
        
        if self.side_door is True:
            print("We can use the side door to get the stuff out of the back "
                 f"of the {self._description()}.")
