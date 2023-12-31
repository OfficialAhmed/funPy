"""
####  String to Integer and Vice Versa  ####

Write two functions:



[Examples]

___
to_int("77") ➞ 77

to_int("532") ➞ 532

to_str(77) ➞ "77"

to_str(532) ➞ "532"
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
int() Class
https://docs.python.org/3/library/functions.html#int
Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines …
_________
_________
str() Class
https://docs.python.org/3/library/functions.html#func-str
Return a str version of object. See str() for details.
_________
_________
How to Convert an Integer to a String
https://pythonprinciples.com/blog/converting-integer-to-string-in-python/
To convert an integer to a string, use the str() built-in function. The function takes an integer (or other type) as its input and produces a string as its output. Here …
_________
_________
How to Convert an Integer to a String
https://www.geeksforgeeks.org/convert-integer-to-string-in-python/#:~:text=In%20Python%20an%20integer%20can%20be%20converted%20into,%E2%80%9C%25s%E2%80%9D%20keyword%2C%20the.format%20function%20or%20using%20f-string%20function.
How to convert an integer to a string.
_________
_________
Handling Exceptions
https://wiki.python.org/moin/HandlingExceptions
The simplest way to handle exceptions is with a "try-except" block.
_________

"""


# Your code should go here:


def to_int(str1):
    return int(str1)


def to_str(int1):
    return str(int1)


print(to_int("77"))  # ➞ 77
print(type(to_int("77")))  # ➞ 77

print(to_int("532"))  # ➞ 532
print(type(to_int("532")))  # ➞ 532

print(to_str(77))  # ➞ "77"
print(type(to_str(77)))  # ➞ "77"

print(to_str(532))  # ➞ "532"
print(type(to_str(532)))  # ➞ "532"

# complete.
