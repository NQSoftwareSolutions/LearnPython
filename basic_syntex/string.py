# Todo Working with Strings
"""
    String is a sequence (Array) of characters
    String can contain (A-Z, a-z 0-9 Special Characters)
    String data will be in double quotes "" or single quotes ''

    A string is a data type used in programming, such as an integer and floating point unit,
    but is used to represent text rather than numbers.
    It comprises a set of characters that can also contain spaces and numbers.
    For example, the word "hamburger" and the phrase "I ate 3 hamburgers" are both strings.
"""
first = "Abdul "
middle = 'Qayoom '
last = 'jat'
print(first + middle + last)

# Todo Adding external code to string or Escape sequences
# Todo add quotes
print("This is nice 'quote'")
print('This is also nice "quote"')
"""
    We have to use bias with outer quotation marks 
"""
# Todo Using escape sequence
"""
    back slash "\" is used to ignore the functionality
    
"""
# Todo double quotes inside double quotes using \
print("Using \"escape\" sequences")
# Todo single quotes inside single quotes using \
print('Using \'escape\' sequences')
# Todo large string
c = "This is very large string" \
    " & i am writing it down"
"""
    Upper value will be assumed as one line
"""
print(c)

d = "This is very large string\
    & i am writing it down"
"""
    Upper value will be assumed as one line
"""
print(d)


