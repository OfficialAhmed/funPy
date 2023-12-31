"""
####  Stuttering Function  ####

Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after each,
and then the word is pronounced with a question mark ?.


[Examples]

___
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
_____



[Notes]

Assume all input is in lower case and at least two characters long.


[algorithms] [formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to get the first 2 letters of a string in Python?
https://stackoverflow.com/questions/20988835/how-to-get-the-first-2-letters-of-a-string-in-python/20989153
How to get the first 2 letters of a string in Python? def first2(s): return s[:2]
_________
_________
Format Specification Mini-Language
https://docs.python.org/3.5/library/string.html#format-specification-mini-language
Are used within replacement fields contained within a format string to define
how individual values are presented (see Format String Syntax). They can also be passed di …
_________
_________
Lists
https://docs.python.org/3.3/tutorial/introduction.html#lists
Python knows a number of compound data types, used to group together other values.
The most versatile is the list, which can be written as a list of comma-separated val …
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
Are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello". You can display a string literal with the print() function.
_________
_________
String Formatting Best Practices
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses.
You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
String Format Cookbook
https://mkaz.blog/code/python-string-format-cookbook/
Python v2.7 introduced a new string formatting method, that is now the default in Python3.
I started this string formatting cookbook as a quick reference to help me form …
_________

"""


# Your code should go here:

# Restrictions:
# - Input lower case.
# - length >= 2.
# Only characters allowed.

# Requirements:
# - As Example.

def stutter(word: str):
    # Count.
    try:
        index = 0
        while True:
            word[index]
            index += 1
    except IndexError:
        word_length = index
    # At least.
    if word_length >= 2:

        # To check lowercase only.
        lowercase_characters = [chr(ele) for ele in range(97, 97 + 26)]

        for char in word:
            if char not in lowercase_characters:
                return "Only lowercase letters are allowed."

        return f"{word[:2]}... {word[:2]}... {word}?"

    elif word_length < 2:
        return "Input length should be at least 2 letters."


print(stutter("incredible"))  # ➞ "in... in... incredible?"

print(stutter("enthusiastic"))  # ➞ "en... en... enthusiastic?"

print(stutter("outstanding"))  # ➞ "ou... ou... outstanding?"

print(stutter("Nitkarsh"))

print(stutter("nitkarsh"))
print(stutter("hello."))  # The error it gives is wrong. For symbols.
# Just find out how to handle symbols through ascii characters?
# inc.
# Want to check the format type, like below...
# return format."{string1[:2]... {string1[:2]... {string1}?}"
