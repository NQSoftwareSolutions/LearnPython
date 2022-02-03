# Todo Nested Dictionary
"""
    In Python, a nested dictionary is a dictionary inside a dictionary.
    It's a collection of dictionaries into one single dictionary.
    Here, the nested_dict is a nested dictionary with the dictionary dictA and dictB .
    They are two dictionary each having own key and value.

    Dictionary support nested dictionary so we can add dictionary in a key
    like eg :   cars = {"c1": {"n": "Honda", "y": 2020}, "c2": {"n": "civic", "y": 2022}}
"""
cars = {"c1": {"n": "Honda", "y": 2020}, "c2": {"n": "civic", "y": 2022}}
car_have = {'c1': [1, 2, 4, 5], 'c2': [3, 5, 6]}

# Todo access data from nested dictionary
print("Access value (car1 name) %s" % cars['c1']['n'])
print("Access value (car2 model) %s" % cars['c2']['y'])
print("Access value (car1) %s" % cars['c1'])
# print("Access value (cars have at 2 index) %s" % cars['c1'][2])
"""
    we can access the value of key by primary & secondary key
"""
