# Todo Conditional logic if & else
"""
    Decision-making in a programming language is automated
    using conditional statements, in which Python evaluates the code to see
    if it meets the specified conditions. The conditions are evaluated
    and processed as true or false.
    If this is found to be true, the program is run as needed.
    Indentations are important & python prefer indentation multiple of four
"""
a = 10
b = 20

# Todo check a condition by if
if a > b:
    print("%s is greater then %s" % (a, b))

if a < b:
    print("%s is less then %s" % (a, b))
elif a == b:
    print("%s is equal to %s" % (a, b))
else:
    print("%s is greater then %s" % (a, b))