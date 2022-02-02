# Todo Numbers - Exponentiation & Modulo

# Todo Exponentiation (Power)
"""
    Exponentiation is a mathematical operation, written as bⁿ, involving two numbers,
     the base b and the exponent or power n, and pronounced as "b raised to the power
      of n".
      In python eg:
            a = 5
            b = 2
            expo = a ** b

            will return expo = 25
"""
a = 5
b = 2
expo = a ** b
print("Exponentiation : " + str(expo))

# Todo Modulo operations
"""
    In computing, the modulo operation returns the remainder or signed remainder 
    of a division, after one number is divided by another.
    Given two positive numbers a and n, a modulo n is the remainder of 
    the Euclidean division of a by n, where a is the dividend and n is the divisor.
    eg:
        remainder = 10 % 4
        
        this will return 2 b/c 10 is not fully division able with 4
        & 8 is completely division able with 4
        & if we do 10 - 8 it will return 2 
"""
remainder = 10 % 4
print("Remainder : " + str(remainder))
