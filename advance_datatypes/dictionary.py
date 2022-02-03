# Todo Dictionary
"""
    A dictionary is an unordered and mutable Python container that stores mappings
    of unique keys to values. Dictionaries are written with curly brackets ({}),
    including key-value pairs separated by commas (,).

    Dictionary is a data type in python, which used to store multiple values in one variable.
    Dictionary stores value in key value pair separated by colon ":"
    Different pairs will be separated by comma (,)

    eg:     dictionary = {k1:v1, k2:v2 & so on}

    Dictionary is not sequenced & not work on indexing
    Dictionary work on mapping
    Dictionary can have value of multiple times
    We can find items in list by key
"""

languages = {"j": "Java", "py": "Python", "js": "Javascript", "r": "Ruby", "p": "PHP", "c#": "C Sharp", "kt": "Kotlin"}
print("Dictionary %s" % languages)

# Todo access list items
print("Dictionary item (Python) %s" % languages["py"])

# Todo add item with key to list after initialization
languages["h"] = "HTML"
print("Dictionary is %s" % languages)

# Todo Get value of dictionary item perform operation
python = languages["py"]
java = languages["j"]
add = java + python
print("I get %s & %s from dictionary & add them to get %s" % (python, java, add))
print(languages["h"]*5)

# Todo Change the value at any key
languages["one"] = 1
print("New Dictionary %s" % languages)
languages["one"] = 2
print("Modified Dictionary %s" % languages)
