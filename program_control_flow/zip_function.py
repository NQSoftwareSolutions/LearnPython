# Todo Iterating multiple lists- Using the zip function
"""
    Python zip Function
The zip() function combines the contents of two or more iterables.
zip() returns a zip object.
This is an iterator of tuples where all the values you have passed
as arguments are stored as pairs. Python's zip() function
takes an iterable—such as a list, tuple, set,
or dictionary—as an argument.
"""

l1 = ["java", "python", "javascript", "Ruby", "PHP", "C Sharp", "Kotlin"]
l2 = [1, 2, 3, 4]

# Todo Iterate over multiple lists by one for loop  by zip
"""
    This loop will take shorter list & run up to last item of shorter list
    b/c this will run until loop finding pairs of values for both iterators
    we can iterate any number of list by just adding list in zip function & provide 
    iterators for that list
"""
for a, b in zip(l1, l2):
    print("list 1 item %s" % a)
    print("list 2 item %s" % b)


