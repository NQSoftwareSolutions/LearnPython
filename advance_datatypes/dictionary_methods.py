# Todo Dictionary methods

cars = {"c1": {"n": "Honda", "y": 2020}, "c2": {"n": "civic", "y": 2022}}
languages = {"j": "Java", "py": "Python", "js": "Javascript", "r": "Ruby", "p": "PHP", "c#": "C Sharp", "kt": "Kotlin"}

# Todo Get keys of dictionary
print("Keys %s" % cars.keys())
print("Keys %s" % languages.keys())

# Todo Get values of dictionary
print("values %s" % cars.values())
print("values %s" % languages.values())

# Todo Get items of dictionary
print("Items %s" % cars.items())
print("items %s" % languages.items())

# Todo Copy a dictionary
cars_copy = cars.copy()
print("Copying, original %s, \n copied %s" % (cars, cars_copy))

# Todo Clear dictionary
print("Now car copy dictionary is '%s'" % cars_copy.clear())

# Todo delete any items from dictionary
popped = cars.pop('c1')
print("Deleting %s from dictionary \n & now cars dictionary is %s" % (popped, cars))



