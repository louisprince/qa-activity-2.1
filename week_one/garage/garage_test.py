import unittest
from garage import Garage
from car import Car
from van import Van

class TestGarage(unittest.TestCase):
    # Before All - Runs once before all cases
    @classmethod
    def setUpClass(cls):
        print("set up calculator")
        cls.shared_resource = "Calculator is ready to go!"

    # Before Each Test - Runs for each testcase
    def setUp(self) -> None:
        self.garage = Garage()
        self.garage.add_vehicle(Car(123, "Ford", "Escort", 75495, 1991, False, False, False))
        self.garage.add_vehicle(Car(456, "Tesla", "Model S", 35982, 2023, True, True, True))
        self.garage.add_vehicle(Van(789, "Merdedes", "Sprinter", 362895, 2021, True, True))

    def test_init(self):
        self.assertTrue(isinstance(self.garage, Garage), True)
    
    def test_wash_all(self):
        expected_output = """Giving the 1991 Ford Escort car a wash.
Hoovering the crumbs around the drivers seat.
Giving the 2023 Tesla Model S car a wash.
Hoovering the crumbs around the drivers seat.
Giving the 2021 Merdedes Sprinter van a wash.
Best clear out the stuff in the back while we're at it.
We can use the side door to get the stuff out of the back of the 2021 Merdedes Sprinter.
"""
        self.assertEquals(self.garage.wash_all(), expected_output)

    # After Each Test - Runs for each testcase
    def tearDown(self) -> None:
        print("Tearing down after a test case...")
        self.my_calculator = None

    # After All - Runs at the end (once)
    @classmethod
    def tearDownClass(cls):
        print("cleaning up calculator")
        cls.shared_resource = None