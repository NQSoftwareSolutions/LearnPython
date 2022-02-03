# Todo while else
"""
    In this syntax, the condition is checked at the beginning of each iteration.
    The code block inside the while statement will execute as long
    as the condition is True . When the condition becomes False and
    the loop runs normally, the else clause will execute.

    else of while will run if our code does not inter in loop
    this else is part of the loop so if we break loop by break statement then
    this else also will be breaked
"""

# Todo add in list by while else
num = 0
my_list = []
while num < 10:
    my_list.append(num)
    print("List is %s" % my_list)
    num += 1
else:
    print("We are out of loop")

# Todo add in list by while else with break
num = 0
my_list = []
while num < 10:
    my_list.append(num)
    print("'Break' List is %s" % my_list)
    if num == 8:
        break
    num += 1
else:
    print("We are out of loop")
