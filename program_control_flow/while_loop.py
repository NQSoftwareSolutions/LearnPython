# Todo While loop
"""
    Python While Loop is used to execute a block of statements repeatedly
    until a given condition is satisfied.
    And when the condition becomes false, the line immediately after
    the loop in the program is executed.
"""

a = 5
b = 10

while a < b:
    print("A is %s" % str(a))
    a += 1

# Todo add in list by loop
num = 0
my_list = []
while num < 10:
    my_list.append(num)
    print("List is %s" % my_list)
    num += 1

