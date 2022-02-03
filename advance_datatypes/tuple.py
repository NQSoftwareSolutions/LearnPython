# Todo Tuple
"""
    Tuples are same as list but tuple are not mutable
    A Tuple is a collection of Python objects separated by commas.
    In someways a tuple is similar to a list in terms of indexing,
    nested objects and repetition but a tuple is immutable unlike lists which are mutable.

    why tuple?
        B/c It Is immutable
"""

my_tuple = ("1", "2", 3, 4, 4, 5, 6, 4, 8, 9, 0)
print("Tuple %s" % str(my_tuple))

# Todo slicing tuple
print("Slicing, (Show full) is %s" % str(my_tuple))
print("Slicing, (3 to last) is %s" % str(my_tuple[3:]))
print("Slicing, (Show at 5) is %s" % str(my_tuple[5]))
print("Slicing, (Show last) is %s" % str(my_tuple[-1]))
print("Slicing, (Show first) is %s" % str(my_tuple[0]))

# Todo get tuple index of item
print("Get Index of, ('2') is %s" % str(my_tuple.index('2')))

# Todo check counts of any item in tuple
print("Check Counts: of (4) are %s" % str(my_tuple.count(4)))
