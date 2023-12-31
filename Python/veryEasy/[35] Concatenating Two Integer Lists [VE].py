"""
####  Concatenating Two Integer Lists  ####

Create a function to concatenate two integer lists.


[Examples]

___
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
_____



[Notes]

___
*) Don't forget to return the result.
*) See Resources tab for more info.
___



[arrays] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How do I concatenate two lists in Python?
https://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
In Python, the only way I can find to concatenate two lists is list.extend, which modifies the first list. Is there any concatenation function that returns its result w …
_________
_________
Ways to Concatenate Two Lists
https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/
Let’s see how to concatenate two lists using different methods in Python. This operation is useful when we have numbers of lists of elements which needs to be processed …
_________
_________
Python Lists
https://www.w3schools.com/python/python_lists.asp
Use argument in to search the list for an element. e.g if "apple" in lst: print("apple is in list")
_________
_________
Splitting, Concatenating, and Joining Strings
https://realpython.com/python-string-split-concatenate-join/
In this beginner-friendly article, you’ll learn some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to us …
_________
_________
Progamiz – extend() Function
https://www.programiz.com/python-programming/methods/list/extend
A guide from the website 'Programiz' on the 'extend()' function which enables a user to add the items of an Array to the end of another Array
_________

"""


# Your code should go here:

def concat(list1, list2):
    list4 = list1 + list2
    print(list1)
    return list4


# explore extend, addition, append and why they are not working here?
# what is actually going on in memory?


print(concat([1, 3, 5], [2, 6, 8]))  # ➞ [1, 3, 5, 2, 6, 8]

print(concat([7, 8], [10, 9, 1, 1, 2]))  # ➞ [7, 8, 10, 9, 1, 1, 2]

print(concat([4, 5, 1], [3, 3, 3, 3, 3]))  # ➞ [4, 5, 1, 3, 3, 3, 3, 3]
