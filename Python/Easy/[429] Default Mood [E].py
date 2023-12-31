"""
####  Default Mood  ####

Create a function that takes in a current mood and
return a sentence in the following format: "Today, I am feeling {mood}".
However, if no argument is passed, return "Today, I am feeling neutral".


[Examples]

___
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"
_____



[Notes]

Check the Resources tab for some helpful information.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Adding Default Function Parameters
https://www.programiz.com/python-programming/function-argument
In Python, you can define a function that takes variable number of arguments.
You will learn to define such functions using default, keyword and arbitrary arguments in …
_________
_________
Python String Formatting Best Practices
https://realpython.com/python-string-formatting/
Remember the Zen of Python and how there should be “one obvious way to do something in Python”?
You might scratch your head when you find out that there are four major …
_________
_________
Using Python Optional Arguments When Defining Functions
https://realpython.com/python-optional-arguments/
Learn about Python optional arguments and how to define functions with default values.
You'll also learn how to create functions that accept any number of arguments usi …
_________

"""


# Your code should go here:


def moodToday(moodInput="neutral") -> str:
    return "Today, I am feeling {0}.".format(moodInput)


print(moodToday("happy"))  # ➞ "Today, I am feeling happy"

print(moodToday("sad"))  # ➞ "Today, I am feeling sad"

print(moodToday())  # ➞ "Today, I am feeling neutral"


def moodToday1(moodInput="neutral") -> str:
    return f"Today, I am feeling {moodInput}."  # Learn this type of formatting and solve this error.


print(moodToday1("happy"))  # ➞ "Today, I am feeling happy"

print(moodToday1("sad"))  # ➞ "Today, I am feeling sad"

print(moodToday1())  # ➞ "Today, I am feeling neutral"

# inc.
# Also learn typing module a little to have a typing module for all the type you know.
# Use chatgpt if needed in the process.
