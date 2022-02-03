# Todo List Methods

languages = ["java", "python", "javascript", "Ruby", "PHP", "C Sharp", "Kotlin"]
# Todo Get length of the list
print("Length of list is %s" % str(len(languages)))
"""
    This will provide length of the list
"""

# Todo Append list after initialization
languages.append("HTML")
print("New Item is appended & now list is %s" % languages)
"""
    Append used to add items in list
    This will add a new item at the end of the list
    The append() method in python adds a single item to the existing list.
     It doesn't return a new list of items but will modify the original list by 
     adding the item to the end of the list.
"""

# Todo insert item of specified index
languages.insert(5, "CSS")
print("New item is inserted & now list is %s" % languages)
"""
    The Python List insert() method is an inbuilt function in Python that inserts a given 
    element at a given index in a list.
    Syntax: list_name.insert(index, element)
    Parameters:
    Returns: This method does not return any value but it inserts the given 
    element at the given index.
"""

# Todo Get index of specified item
index = languages.index("CSS")
print("Index is %s" % str(index))

# Todo Remove last item from a list
popped = languages.pop()
print("%s is popped & new list is %s" % (popped, languages))

# Todo Remove specified item from list
removed = "CSS"
languages.remove(removed)
"""
    Remove does not return any thing
"""
print("%s is removed & now new list is %s" % (removed, languages))

# Todo Slicing list
"""
    In slicing 
    first index is inclusive & last index is exclusive
"""
print("Slicing (0 to 4) %s" % languages[0:4])
print("Slicing (2 to last) %s" % languages[2:])
print("Slicing (first) %s" % languages[0])
print("Slicing (last) %s" % languages[-1])

# Todo Sort list alphabetically
print("Original list is %s \n& Sorted list is (alphabetically) %s" % (languages, sorted(languages)))

