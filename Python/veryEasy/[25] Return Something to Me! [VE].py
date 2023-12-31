"""
####  Return Something to Me!  ####

Write a function that returns the string "something" joined with a space " " and the given argument a.


[Examples]

___
give_me_something("is better than nothing") ➞ "something is better than nothing"

give_me_something("Bob Jane") ➞ "something Bob Jane"

give_me_something("something") ➞ "something something"
_____



[Notes]

Assume an input is given.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python String Append
https://www.javacodegeeks.com/2019/04/python-string-append-example.html
This is an article about appending of string in python. In Python, string is an immutable object. You can use ‘+’ operator to append two strings to create a new string. …
_________
_________
How to Use Python Lambda Functions
https://realpython.com/python-lambda/
Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions.
_________
_________
format() Function
https://www.educba.com/python-format-function/
Python has acquired a wide and peak level in the market like no language has done ever before, especially in the domain of Artificial Intelligence and Data Science. Kno …
_________

"""


# Your code should go here:

def give_me_somethng(input1):
    return "something {0}".format(input1)


print(give_me_somethng("is better than nothing"))  # ➞ "something is better than nothing"

print(give_me_somethng("Bob Jane"))  # ➞ "something Bob Jane"

print(give_me_somethng("something"))  # ➞ "something something"

# complete.
