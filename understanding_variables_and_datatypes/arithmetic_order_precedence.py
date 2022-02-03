# Todo Arithmetic order of precedence
"""
    / & * have same ordered of precedence
    - & + have same ordered of precedence
    () = parentheses is used to set own order of precedence

    operators with same precedence will be solved from left to right

"""
# Todo with out bracket
# Todo just sum
p = 5 + 5 + 5 + 10 + 10 + 10
print("Just sum : " + str(p))

# Todo just subtraction
p = 5 - 5 - 5 - 10 - 10 - 10
print("Just subtraction : " + str(p))

# Todo just subtraction & summation
p = 5 - 5 - 5 + 10 + 10 + 10
print("Just sum & sub : " + str(p))

# Todo just multiplication, subtraction & summation
p = 5 - 5 - 5 * 10 + 10 + 10
print("Just mul, sum & sub : " + str(p))

# Todo just division, multiplication, subtraction & summation
p = 5 - 5 - 5 * 10 / 10 + 10
print("Just div, mul, sum & sub : " + str(p))

# Todo effect of parentheses
p = (5 - 5 - 5) * 10 / 10 + 10
print("Effect of parentheses : " + str(p))
