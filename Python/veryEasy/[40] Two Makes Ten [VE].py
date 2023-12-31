"""
####  Two Makes Ten  ####

Create a function that takes two arguments. Both arguments are integers, a and b.
Return True if one of them is 10 or if their sum is 10.


[Examples]

___
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True
_____



[Notes]

Don't forget to return the result.


[algorithms] [conditions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Membership Operators Example
https://www.tutorialspoint.com/python/membership_operators_example.htm
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below ...
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
How to Use the Python or Operator
https://realpython.com/python-or-operator/
There are three Boolean operators in Python: and, or, and not. With them, you can test conditions and decide which execution path your programs will take. In this tutor …
_________
_________
Video Tutorial for the Challenge
https://youtube.com/watch?v=Lz0GzT_A0CY
Video tutorial of this challenge.
_________

"""


# Your code should go here:

def makes10(a, b):
    if a or b == 10 or a + b == 10:  # Iska logical error kya hai? Go through that method way of tracingValues (a == 10 or b == 10 or a + b == 10) woh kyu right aata hai?
        return True  # logical error traceRouting se pata lagao please.
    else:
        return False


print(makes10(9, 10))  # ➞ True

print(makes10(9, 9))  # ➞ False

print(makes10(1, 9))  # ➞ True

print(makes10(10, 10))

print(makes10(3, 3))
