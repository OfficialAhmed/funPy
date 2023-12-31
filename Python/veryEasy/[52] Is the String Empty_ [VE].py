"""
####  Is the String Empty?  ####

Create a function that returns True if a string is empty and False otherwise.


[Examples]

___
is_empty("") ➞ True

is_empty(" ") ➞ False

is_empty("a") ➞ False
_____



[Notes]

___
*) A string containing only whitespaces " " does not count as empty.
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to check if a string is empty or not?
https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/
Python strings are immutable and hence have more complex handling when talking about its operations. Note that a string with spaces is actually an empty string but has …
_________
_________
Truth Value Testing
https://docs.python.org/3/library/stdtypes.html#truth-value-testing
Official documentation of how "truthiness" works in Python 3.
_________
_________
Python's Built-in Types
https://docs.python.org/2/library/stdtypes.html
The principal built-in types are numerics, sequences, mappings, files, classes, instances and exceptions. Some operations are supported by several object types; in part …
_________
_________
Truth Value Testing
https://codesteps.com/2018/11/06/python-truth-value-testing/
What really the Truth Value is? True is the Truth value. But non boolean values doesn’t have true or false values. For example, numbers do not have true or false value. …
_________
_________
Truth Value Testing
https://docs.python.org/2.4/lib/truth.html
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. The following values are considered false: …
_________
_________
Check String Empty or Not
https://www.netjstech.com/2019/07/check-string-empty-or-not-python.html
Check if a String is empty or not in Python using len() function, not keyword and using isspace() method.
_________
_________
len() Function
https://realpython.com/len-python-function/
Learn how and when to use the len() Python function. You'll also learn how to customize your class definitions so that objects of a user-defined class can be used as ar …
_________

"""


# Your code should go here:


def isEmpty(string1):
    if isinstance(string1, str):

        count = 0
        try:
            while True:
                string1[
                    count]  # It doesn't go ahead, if error encountered then jump back to the previous results. I like it.
                count += 1
        except IndexError:
            pass

        if count == 0:
            return True
        elif count > 0:
            return False
    else:
        return "Only string inputs allowed."


print(isEmpty(""))  # ➞ True

print(isEmpty(" "))  # ➞ False

print(isEmpty("a"))  # ➞ False

# I want this program to be used in pythontutor, analysed in pythonTutor. It will be good.

# inc.
# only for testing on pythontutor.com

# complete.
