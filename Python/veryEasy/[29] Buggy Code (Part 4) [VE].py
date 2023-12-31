"""
####  Buggy Code (Part 4)  ####

Emmy has written a function that returns a greeting to users.
However, she's in love with Nitkarsh, and would like to greet him slightly differently.
She added a special case in her function, but she made a mistake.
Can you help her?


[Examples]

___
greeting("Matt") ➞ "Hello, Matt!"

greeting("Helen") ➞ "Hello, Helen!"

greeting("Nitkarsh") ➞ "Hello, my Love!"
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[bugs] [conditions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
Sequence in Python
https://blog.withcode.uk/2018/09/08-sequence-in-python/
There are three main building blocks that all computer programs consist of: sequence, selection and iteration. This activity is designed to help you design and code you …
_________
_________
If Statement
https://pythonexamples.org/python-if-example/
Is a conditional statement wherein a set of statements execute based on the result of a condition. In this Python example, we will learn about Python If statement synt …
_________

"""


# Your code should go here:


def greeting(name):
    if name.lower() == "nitkarsh":
        return "Hello, my Love!"
    else:
        return "Hello, {0}!".format(name)


print(greeting("Matt"))  # ➞ "Hello, Matt!"

print(greeting("Helen"))  # ➞ "Hello, Helen!"

print(greeting("Nitkarsh"))  # ➞ "Hello, my Love!"

# complete.
