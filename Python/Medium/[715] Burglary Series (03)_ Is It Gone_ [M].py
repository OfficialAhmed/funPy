"""
####  Burglary Series (03): Is It Gone?  ####

Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!
Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:
___
*) "Rambo is gone..." if the name is on the list.
*) "Rambo is here!" if the name is not on the list.
___

Note that the first letter of the name in the return statement is capitalized.


[Examples]

___
 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.


 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.


items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary.
_____



[Notes]

N/A


[data_structures] [strings] 



-------------------------------------------------------------------
[Resources]
_________
capitalize() Method
https://www.programiz.com/python-programming/methods/string/capitalize
Converts first character of a string to uppercase letter and lowercases all other characters, if any.
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
title() Method
https://www.programiz.com/python-programming/methods/string/title
Returns a string with first letter of each word capitalized; a title cased string.
_________
_________
Check if Dictionary Is Empty
https://www.geeksforgeeks.org/python-check-if-dictionary-is-empty/
Sometimes, we need to check if a particular dictionary is empty or not. This particular task has its application in web development domain in which we sometimes need to …
_________
_________
Iterate dictionary (key and value) with for loop in Python | note.nkmk.me
https://note.nkmk.me/en/python-dict-keys-values-items/
In Python, to iterate the dictionary (dict) with a for loop, use keys(), values(), items() methods. You can also get a list of all keys and values in the dictionary wit …
_________

"""


# Your code should go here:


# Will see the right way of doing this.

def pets1(items):
    if dict1["timmy"] != True:
        return "Timmy is gone..."

    elif dict1["timmy"] == True:  # First how to avoid keyerror? # I will do try and
        # except but before that try and error is to be done.
        return "Timmy is here!"


def pets(dict1):
    if dict1["timmy"] != True:
        return "Timmy is here!"
    try:
        if dict1["timmy"] == True:
            return "Timmy is gone..."
    except KeyError:


items1 = {
    "tv": 30,
    "timmy": 20,
    "stereo": 50,
}  # ➞ "Timmy is gone..."
# Timmy is in the dictionary.

# print(pets(items1))

items = {
    "tv": 30,
    "stereo": 50,
}  # ➞ "Timmy is here!"
# Timmy is not in the  dictionary.

print(pets(items))

items = {}  # ➞ "Timmy is here!"
# Timmy is not in the dictionary.


# inc.
