# Todo some short cuts for doing operations in python

# Todo Addition
a = b = 10

a = a + 10
b += 10
"""
    both operations will return same result
"""
print("Sum A = " + str(a) + " & B = " + str(b))

# Todo Subtraction
a = b = 10

a = a - 10
b -= 10
"""
    both operations will return same result
"""
print("Subtraction A = " + str(a) + " & B = " + str(b))

# Todo Multiplication
a = b = 10

a = a * 10
b *= 10
"""
    both operations will return same result
"""
print("Multiplication A = " + str(a) + " & B = " + str(b))

# Todo Division
a = b = 10

a = a / 10
b /= 10
"""
    both operations will return same result
"""
print("Division A = " + str(a) + " & B = " + str(b))

# Todo create a list of numbers
print("Range Numbers: " + str(range(10, 100)))
"""
    Above method is generating numbers 
    but not showing so we need to type cast it in list
    & ending number is exclusive
"""
print("Range Numbers: " + str(list(range(10, 100))))

# Todo print method short cut
"""
    we can multiply any string available in print function
"""
star = "*"
print(star * 100)  # this will print 100 stars

# Todo print results of multiple print statement on one line
a = 0
while a < 10:
    print(a, end=", ")
    a += 1
    """
        end is a positional variable
    """
