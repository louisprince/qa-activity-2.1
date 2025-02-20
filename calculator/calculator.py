#!/bin/python3

class Calculator:
    def add(self, first: float, second: float) -> float:
        return first + second
    
    def subtract(self, first: float, second: float) -> float:
        return first - second
    
    def multiply(self, first: float, second: float) -> float:
        return first * second
    
    def divide(self, first: float, second: float) -> float:
        if first == 0 or second == 0:
            return 0
        else:
            return first / second
