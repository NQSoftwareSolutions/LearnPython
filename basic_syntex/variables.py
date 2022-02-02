import keyword as kw;

# Todo Variable rules for naming variables
"""
    Variable can not be any reserved word or key word
"""
# Todo get list of keywords or reserved words
print(kw.kwlist)
"""
    This is a method in keyword module for getting list of keywords or reserved words.
"""
"""
    start variable name with letter of underscore
    Do not start name with a number
    Variable name can contain letters, number & underscore (name_123)
    Do not use special characters in variable name
"""
# Todo assign values to variables in one line (not recommended)
a = b = c = d = "Qayoom"
print(a)
print(b)
print(c)
print(d)
"""
    All reference names a,b,c, d have same value Qayoom
    a,b,c,d are String object reference name
    Reference counter of Qayoom object is 4
"""
# Todo other of assigning different values to multiple variables in one
#  line (not recommended)
a, b, c, d = 10, 20, 30, 40
print(a)
print(b)
print(c)
print(d)
"""
    Now all variables have different values
    a = 10
    b = 20
    c = 30
    d = 40
"""

# Todo understanding Reference count, references & variables
a = "Qayoom"
b = "Qayoom"

"""
A table 
object reference count 
object Qayoom has two references a & b
Qayoom is data or value of string objects named a & b
Referencing count of string object Qayoom is 2
"""

a = 234
"""
now a new integer object 123 is create & reference name is a
data at reference a is 234
& in table reference a will be referencing to object 234 not Qayoom
& reference object of qayoom is now decreased to 1 b/c now reference a is 
pointing to 234 integer object.
If reference count becomes zero for any object then python will send
object to garbage collector & free up space.
"""

# Todo using of equality operator
a = 786
b = a

print(a == b)
print(b is a)
print(a is b)

"""
use of "is" & "=="
"is" is same as equality operator
Now above 3 print statement will print trues b/c all statement are same.
"""

print(a)
print(b)

# Todo assigning value of one variable to get other type of object
e = a == b
print(e)
e = a is b
print(e)
"""
Now e is boolean object reference after getting 
"""
