# Todo Break continue while / else
"""
    ? Break:
        In Python, the break statement provides you with the opportunity
        to exit out of a loop when an external condition is triggered.
        You'll put the break statement within the block of code under your
        loop statement, usually after a conditional if statement.
    ? Continue:
        Continue statement is a loop control statement that forces to execute
        the next iteration of the loop while skipping the rest of the code
        inside the loop for the current iteration only
        i.e. when the continue statement is executed in the loop,
        the code inside the loop following the continue statement will
        be skipped for the current iteration and the next iteration of
        the loop will begin.
"""

# Todo add in list by loop & use break
num = 0
my_list = []
while num < 10:
    my_list.append(num)
    print("'Break' List is %s" % my_list)
    num += 1
    if num == 8:
        break

# Todo add in list by loop & use continue
num = 0
my_list = []
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    my_list.append(num)
    print("'Continue' List is %s" % my_list)
