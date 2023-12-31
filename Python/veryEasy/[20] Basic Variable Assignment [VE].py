"""
####  Basic Variable Assignment  ####

A student learning Python was trying to make a function.
His code should concatenate a passed string name with string "Hello" and store it in a variable called result.
He needs your help to fix this code.


[Examples]

___
name_string("Mubashir") ➞ "MubashirHello"

name_string("Matt") ➞ "MattHello"

name_string("python") ➞ "pythonHello"
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[bugs] [functional_programming] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Concatenation
https://www.w3schools.com/python/python_strings_concatenate.asp
To concatenate, or combine, two strings you can use the + operator.
_________
_________
Variables and Assignment
https://www.pluralsight.com/guides/python-basics-variables-assignment
Variables hold values. In Python, variables do not require forward declaration - all you need to do is provide a variable name and assign it some value.
_________
_________
String Methods
https://www.w3schools.com/python/python_strings_methods.asp
Python has a set of built-in methods that you can use on strings.
_________
_________
Python Assignment Operators (=)
https://www.tutorialspoint.com/python/assignment_operators_example.htm
Assigns values from right side operands to left side operand.
_________
_________
Variable Assignment
https://youtu.be/BBJa32lCaaY
You will learn how to deal with variable assignments here!
_________

"""


# Your code should go here:

def name_string(name):
    return name + "Hello"


print(name_string("Mubashir"))  # ➞ "MubashirHello"

print(name_string("Matt"))  # ➞ "MattHello"

print(name_string("python"))  # ➞ "pythonHello"

# complete.
