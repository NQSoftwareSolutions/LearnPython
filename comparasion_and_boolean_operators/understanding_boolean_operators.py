# Todo Understanding with boolean operators
"""
    The logical operators and, or and not are also referred to as boolean operators.
    While and as well as or operator needs two operands,
    which may evaluate to true or false, not operator needs
    one operand evaluating to true or false.

    AND will return true if both inputs are ture else false
    OR will return true if any of one input is true else false
    NOT will return inverse (If true then false & if false then true)
"""
a = 10
b = 20

print("Boolean Operator AND on (== & !=) return %s" % str(a == b and a != b))
print("Boolean Operator AND on (< & !=) return %s" % str(a < b and a != b))
print("Boolean Operator OR on (== & !=) return %s" % str(a == b or a != b))
print("Boolean Operator OR on (< & !=) return %s" % str(a < b or a != b))
print("Boolean Operator NOT on (== & !=) return %s" % str(not a != b))
print("Boolean Operator NOT on (< & !=) return %s" % str(not a == b))

print("&"*100)
print("Order of precedence")
print("&"*100)
# Todo Boolean operators order of precedence
"""
    1. not
    2. and 
    3. or
    
    we can customize the order of precedence by putting bracket
"""
boolean1 = False or not False and False
print("Results %s" % str(boolean1))
boolean1 = True or not False and False
print("Results %s" % str(boolean1))
boolean1 = (True or not False) and False
print("Results %s" % str(boolean1))
boolean1 = (False or not False) and False
print("Results %s" % str(boolean1))