# Todo For loop
"""
    A for loop in Python is a control flow statement that is used
    to repeatedly execute a group of statements as long as the condition
    is satisfied.
    Such a type of statement is also known as an iterative statement.
    Therefore, a for loop is an iterative statement.
"""

s = "Abdul Qayoom Jat"

# Todo Access individual character of string
print("*" * 100)
for n in s:
    print("String Character is %s" % n)

# Todo Access every character of string & change specified one
print("*" * 100)
for n in s:
    if n == "o":
        print("String Character is O")
    else:
        print("String Character is %s" % n)

# Todo access list & print separate items
print("*" * 100)
languages = ["java", "python", "javascript", "Ruby", "PHP", "C Sharp", "Kotlin"]
for lang in languages:
    print(lang, end=" ")
print("*" * 100)

# Todo access list of number & do operation on it
print("*" * 100)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in nums:
    if n % 2 == 0:
        print("Even %s" % n)
    else:
        print("Odd %s" % n)
print("*" * 100)

# Todo access dictionary of number & get keys
"""
    By default for loop provide keys by accessing dictionary
"""
print("*" * 100)
d_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
for k in d_num:
    print("Key is %s " % k)
print("*" * 100)

# Todo access dictionary of number & get value
"""
    By default for loop provide keys by accessing dictionary
"""
print("*" * 100)
d_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
for k in d_num:
    print("value is %s & key is %s" % (d_num[k], k))
print("*" * 100)

# Todo Access key & items of dictionary by for loop
print("*" * 100)
d_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
for k, v in d_num.items():
    print("value is %s & key is %s" % (v, k))
print("*" * 100)
