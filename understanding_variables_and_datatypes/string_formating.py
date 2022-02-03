# Todo String formatting

# Todo add in blanks of string sentence
language = "Python"
tool = "Selenium"
print("Original: Wellcome to  automation by ")
"""
    now we have to add words on
    after to & after by
"""
print("Formatted : Wellcome to " + language + " automation by " + tool)

# Todo Recommended way
"""
    by creating place holder for incoming values by %
    Number of % & number of variable should match
"""
print("Formatted : Wellcome to %s automation by %s" % (language, tool))
print("Formatted : Wellcome to %s" % language)
"""
    If their is only one place holder then we don't need to add parenthesis
"""
