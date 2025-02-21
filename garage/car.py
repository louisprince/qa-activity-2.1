from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, id: int, make: str, model: str, milage: int, year: int, 
                 mot: bool, apple: bool, android: bool):
        super().__init__(id, make, model, milage, year, mot)
        self._apple = apple
        self._android = android

    @property
    def apple(self):
        return self._apple

    @property
    def android(self):
        return self._android
    
    def service(self, full_service: bool):
        output = ""

        if full_service is True:
            output += f"Performing a full service on the {self._description()}.\nIt needs a lot of work."
        else: 
            output += f"Performing a quick service on the {self._description()}.\nIt doesn't need much doing to it."
            
        if self.android is True and full_service is True:
            output += f"While we're at it lets give the Android Auto system in the {self._description()} a tune up."

        if self.apple is True and full_service is True:
             output += f"While we're at it lets give the Apple Car Play system in the {self._description()} a tune up."

        return output
            
    def wash(self):
        return f"Giving the {self.year} {self.make} {self.model} car a wash.\nHoovering the crumbs around the drivers seat."
           
    