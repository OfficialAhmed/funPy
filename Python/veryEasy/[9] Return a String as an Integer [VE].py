"""
####  Return a String as an Integer  ####

Create a function that takes a string and returns it as an integer.


[Examples]

___
string_int("6") ➞ 6

string_int("1000") ➞ 1000

string_int("12") ➞ 12
_____



[Notes]

___
*) All numbers will be whole.
*) All numbers will be positive.
___



[language_fundamentals] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
int() Method
https://www.programiz.com/python-programming/methods/built-in/int
Returns an integer object from any number or string.
_________
_________
String to Int() and Int to String
https://careerkarma.com/blog/python-string-to-int/#:~:text=To%20convert%20a%20string%20to,as%20an%20int%20%2C%20or%20integer.
The Python int method is used to convert a string to an integer. Learn how to use the int and str method.
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=SKR-8fowFiE
In this video, you will learn how to solve these problems: 0:22 Return a String as an Integer, 1:31 Add, Subtract, Multiply or Divide?, 4:35 To the Power of ___...
_________
_________
int() Function
https://www.w3schools.com/python/ref_func_int.asp
Converts the specified value into an integer number.
_________

"""


# Your code should go here:


def stringInt(n: str) -> int:
    try:
        newN = int(n)
        assert newN > 0
        return newN
    except AssertionError:
        return "Positive integers only."
    except ValueError:
        return "Input positive integers as number only."


print(stringInt("6"))  # ➞ 6

print(stringInt("1000"))  # ➞ 1000

print(stringInt("12"))  # ➞ 12

print(stringInt("0"))
print(stringInt("Hello"))

# complete.
