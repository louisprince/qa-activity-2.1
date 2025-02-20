from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make: str, model: str, milage: int, year: int, 
                 mot: bool, apple: bool, android: bool):
        super().__init__(make, model, milage, year, mot)
        self._apple = apple
        self._android = android

    @property
    def apple(self):
        return self._apple

    @property
    def android(self):
        return self._android
    
    def service(self, full_service: bool):
        if full_service is True:
            print(f"Performing a full service on the {self._description()}. "
                  "It needs a lot of work.")
        else: 
            print(f"Performing a quick service on the {self._description()}. "
                  "It doesn't need much doing to it.")
            
        if self.android is True:
            print("While we're at it lets give the Android Auto system in the "
                 f"{self._description()} a tune up.")

        if self.apple is True:
             print("While we're at it lets give the Apple Car Play system in "
                 f"the {self._description()} a tune up.")
            
    def wash(self):
        print(f"Giving the {self.year} {self.make} {self.model} car a wash. "
               "Hoovering the crumbs around the drivers seat.")
    
    