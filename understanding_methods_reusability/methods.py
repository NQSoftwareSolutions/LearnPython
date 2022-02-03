# Todo Understanding methods
"""
    Defining Functions in Python
In computer programming, a function is a named section of a code that
performs a specific task. This typically involves taking some input,
 manipulating the input and returning an output.

 Group of statements for one task in one logical unit.
 method of doing anything / task
"""


# Todo Define method with out params
def sum_num():
    print("Sum is %s" % str(3 + 4))
    print("*" * 100)


# Todo call method
sum_num()

# Todo Define method with params
"""
    Method need same number of augments which it is expecting
"""


def sum_num(num1, num2):
    print("Sum is %s" % str(num1 + num2))
    print("*" * 100)


# Todo call parametrized method
sum_num(5, 6)
sum_num(100, 6)
sum_num(5, 23672)


# Todo Method which return a value
def sum_num_ret(num1, num2):
    """
    This method will some two numbers
    :param num1: any number
    :param num2: any number
    :return: sum of two numbers
    """
    s = num2 + num1
    return s


# Todo Use return value of method
return_value = sum_num_ret(34, 34)
print("Returned value %s" % return_value)


# Todo create Method with documentation
def sum_num_doc(num1, num2):
    """
    This method will just some two numbers
    :param num1: any number
    :param num2: any number
    :return: nothing
    """
    print("Sum is %s" % str(num1 + num2))
    print("*" * 100)


print("*" * 100)


# Todo Check list for availability of any thing in method
def is_programming_language(language):
    languages = ["java", "python", "javascript", "ruby", "php", "c sharp", "kotlin"]
    if language in languages:
        print("%s is programming language" % language)
    else:
        print("%s is not programming language" % language)


is_programming_language("python")
is_programming_language("Python")

# Todo Working with positional / Optional Parameters
"""
    A positional argument means its position matters in a function call. 
    A keyword argument is a function argument with a name label. 
    Passing arguments as keyword arguments means order does not matter.
    
    We can provide optional parameter to our methods, 
    so those arguments will be optional 
     We are providing argument value with name so position does not matter
     & we can also provide less number of params then expected by method.
     if method expects 3 arguments & we provide 2 
     & method has optional params then method will get default value for 
     third param.
     
     if we does not provide any value to optional parameterized method then it will get
     default value for that param but 
     it we provide value for optional param then it will have high preference.
     
     one method can have optional as well as non option params
     we can change the place of non optional or non positional param
"""


def optional_arg_method(num=2, num2=2):
    """
    This method will sum two numbers
    :param num: optional & any number
    :param num2: optional & any number
    :return: sum of numbers
    """
    return num + num2


print("*" * 100)
print("Optional param Method with out params %s" % str(optional_arg_method()))
print("Optional param Method with params %s" % str(optional_arg_method(2, 5)))
# Todo Call methods with specifying parameter names & value
print("Optional param Method with params %s" % str(optional_arg_method(num2=5, num=6)))
print("Optional param Method with params %s" % str(optional_arg_method(num=5, num2=6)))

print("*" * 100)


# Todo create a method with optional & non optional params
def optional_arg_method(num0, num=2, num2=2):
    """
    This method will sum two numbers
    :param num0: not optional & any number
    :param num: optional & any number
    :param num2: optional & any number
    :return: sum of numbers
    """
    return num0 + num + num2


print("Positional & No-positional method : %s " % str(optional_arg_method(5, 5, 6)))
print("*" * 100)

# Todo understanding scope of variable
"""
    The scope of a variable refers to the context in which that variable
     is visible/accessible to the Python interpreter.
     
     Local scope variables can only be accessed within its block. 
     
     In Python, a variable declared outside of the function or in 
     global scope is known as a global variable. 
     This means that a global variable can be accessed inside 
     or outside of the function.
"""
print("*" * 100)
# Todo define local variable
"""
    This will be visible in method
"""


def test_var(a):
    a += 10
    print("Local Variable %s" % a)
    a += 10
    print("Local Variable %s" % a)


# Todo define global variable
"""
    this will be visible in file
"""
a = 1

test_var(a)
print("Global Variable (is not changed) %s" % a)

print("*" * 100)
# Todo Create a method which used value of global variable
a = 20


def test_g_var():
    global a
    # Todo global
    """
    Todo Global
        Global keyword is a keyword that allows a user to modify a 
        variable outside of the current scope. 
        It is used to create global variables from a non-global scope 
        i.e inside a function.
    
        this will find global variable a 
        & use its value
        It we call this method 
        then this will affect the value of global variable
    """
    print("Variable inside %s" % a)
    a = 10
    print("Variable inside %s" % a)


test_g_var()
print("Global Variable (is changed) %s" % a)

