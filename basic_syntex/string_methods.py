# Todo Strong methods
"""
    There are some built in methods for manipulating strings
    Method will just provide result after manipulation will not change original string
    We can not change or assign value to any index of string
"""

s = "Abdul Qayoom Jat"

# Todo Accessing characters in string
first = s[0]
"""
    Index always starts from zero
"""
print("Character : " + first)

# Todo len(string)
"""
    len will help to identify length of string
"""
print("Get Length : " + str(len(s)))
# Todo upper(string)
"""
    upper will convert string to upper case
"""
print("To Upper case : " + s.upper())
# Todo lower(string)
"""
    lower will convert string to lower case
"""
print("To Lower case : " + s.lower())
# Todo str(any non string)
"""
    str converts any of non string value to string
"""
print("Non String to String : " + str(len(s)))

# Todo Replace (old pattern, new pattern, no of instances))
"""
    Replace methods will replace pattern available in string value by new specified pattern
"""
pattern = "1abc2abc3abc4acb"
print("Pattern " + pattern + " Replace by " + pattern.replace("abc", "xyz"))
print("Pattern " + pattern + " Replace by " + pattern.replace("abc", "xyz", 2))

# Todo Sub-String method
sub = s[6:12]
"""
    This will start from index 6 & end at index 11
    b/c starting index is inclusive
    & ending index is exclusive
"""
print("Sub String : " + sub)
steps = s[6:12:2]
"""
    Third argument is steps to take for next character
    Default step is 1 & not skipping any thing
"""
print("Step sub string : " + steps)

# Todo Slicing more to string
print("Slicing (Full) : " + s[:])
print("Slicing (1 to full) : " + s[1:])
print("Slicing (0 to 9) : " + s[:10])
print("Slicing (Every second char) : " + s[::2])
print("Slicing (Every third char) : " + s[::3])
print("Slicing (get 7th char) : " + s[6])
# Todo Reverse string
print("Reverse String : " + s[::-1])
# Todo String work as circle
print("String Circle Behave (last) : " + s[-1])
print("String Circle Behave (2nd last) : " + s[-2])
print("String Circle Behave (0 to 2nd last) : " + s[:-1])

# Todo split (string)
"""
    Python String split()
        The split() method splits a string into a list. 
        A string is separated based on a separator character. ... 
        separator is the character the split() function will use to separate out 
        the characters in the string. 
        By default, any white space character will be used as a separator (space, newline).
    spilt method will split string from space " " & create list for those words
    split used to convert a strong into list
"""
print("Split : " + str(s.split()))




