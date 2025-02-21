class MathsOperations:
    def divide(self, a, b):
        if a != 0 and b != 0:
            return a / b
        else:
            return 0
    
    def multiply(self, a, b):
        return a * b
    
class StringOperations:
    def upper(self, s):
        return (f"Uppercase string: {s.upper()}")
    
    def lower(self, s):
        return (f"Lowercase string: {s.lower()}")

# MathsOperations injector
def maths_ops(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs, maths_ops=MathsOperations())

    return wrapper

# StringOperations injector
def string_ops(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs, string_ops=StringOperations())

    return wrapper

###############################################################################
########## Functions to test out the dependency injection #####################
###############################################################################

@maths_ops
def do_some_maths(x, y, maths_ops=None):
    result = x - y
    print(f"The result of the subtraction is: {result}")

    if maths_ops:
        print(f"{result} divided by 3 is: {maths_ops.divide(result, 3)}")
        print(f"{result} multiplied by 5 is: {maths_ops.multiply(result, 5)}")


@string_ops
def do_some_string_stuff(s, string_ops=None):
    print(f"The input string is: {s}")

    if string_ops:
        print(string_ops.upper(s))
        print(string_ops.lower(s))


@string_ops
@maths_ops
def do_a_bit_of_both(s, x, string_ops=None, maths_ops=None):
    print(f"The input string is: {s}")
    print(f"The input number is: {x}")

    if string_ops:
        print(string_ops.upper(s))
        print(string_ops.lower(s))

    if maths_ops:
        print(f"65473 divided by {x} is: {maths_ops.divide(65473, x)}")
        print(f"{x} multiplied by 10 is: {maths_ops.multiply(x, 10)}")


do_some_maths(8,2)
do_some_string_stuff("Hello world!")
do_a_bit_of_both("Lolzords", 27)