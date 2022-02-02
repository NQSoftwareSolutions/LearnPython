# Todo Boolean data types
"""
    In computer science, the Boolean data type is a data type that has one of two possible
    values which is intended to represent the two truth values of logic and Boolean algebra.
    It is named after George Boole, who first defined an algebraic system of logic
    in the mid 19th century.

    Boolean is just like a switch just two operation (on or off) (0 or 1) (true or false)
    Boolean data type have only two possibilities

    Anything (Object or value) which is 0 then it false
    Anything (Object or value) which is non-zero then it is true
"""

a = True
b = False

print(a)
print(b)

# Todo bool function
"""
    Python bool() function is used to return or convert a value to a Boolean value 
    i.e., True or False, using the standard truth testing procedure.
"""
print("Bool of 0 : " + str(bool(0)))
# anything other than 0 will be true
print("Bool of 1 : " + str(bool(1)))
print("Bool of 2 : " + str(bool(2)))

c = ""  # empty string
print("Empty string : " + str(bool(c)))
c = "Abdul"  # not empty string
print("Not Empty string : " + str(bool(c)))
c = " "  # space string
print("space string : " + str(bool(c)))
c = None  # none or null
print("none value : " + str(bool(c)))

