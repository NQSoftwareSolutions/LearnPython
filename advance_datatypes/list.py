# Todo List & Accessing the elements
"""
    List is data type, which we used to store multiple value with one variable or reference name
    list used to store different collection of information in one variable
    list can have  multiple data type values
    List is collection of different values
    like languages = ["java", "python", "javascript", 786, "PHP", "C Sharp", "Kotlin"]
    We can place list in %s placeholder
    List also support index & list indexes also starts with 0

    The list is one of the most widely used data types in Python.
    A Python List can be easily identified by square brackets [ ].
    Lists are used to store the data items where each data item is separated by a comma (,).
    A Python List can have data items of any data type, be it an integer type or a boolean type.

    eg: languages = ["java", "python", "javascript", "Ruby", "PHP", "C Sharp", "Kotlin"]
"""
# Todo single data type list
languages = ["java", "python", "javascript", "Ruby", "PHP", "C Sharp", "Kotlin"]
print("Languages list %s" % str(languages))

# Todo multiple data type list
languages = ["java", "python", "javascript", 786, "PHP", 756, "Kotlin"]
print("Languages list %s" % str(languages))

# Todo Print empty list
empty_list = []
print("Empty list %s" % str(empty_list))

# Todo access items of list
print("Access Items: Second item is %s" % languages[1])
print("Access Items: sixth item is %s" % languages[5])
"""
    List also behave as circle as string
"""
print("Access Items: last item is %s" % languages[-1])

# Todo access list items & do arithmatic operations
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_num = numbers[4] + numbers[8]
print("Sum is %s" % str(sum_num))
