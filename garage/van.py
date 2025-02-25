from vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, id: int, make: str, model: str, milage: int, year: int, 
                 mot: bool, side_door: bool):
        super().__init__(id, make, model, milage, year, mot)
        self._side_door = side_door

    @property
    def side_door(self):
        return self._side_door

    def service(self, full_service: bool):
        if full_service is True:
            return f"Performing a full service on the {self._description()}.\nIt needs a lot of work."
        else: 
            return f"Performing a quick service on the {self._description()}.\nIt doesn't need much doing to it."  

    def wash(self):
        output = ""

        output += f"Giving the {self.year} {self.make} {self.model} van a wash.\nBest clear out the stuff in the back while we're at it.\n"
        
        if self.side_door is True:
            output += f"We can use the side door to get the stuff out of the back of the {self._description()}."

        return output
