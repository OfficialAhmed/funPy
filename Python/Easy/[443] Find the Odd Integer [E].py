"""
####  Find the Odd Integer  ####

Create a function that takes a list and finds the integer which appears an odd number of times.


[Examples]

___
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
_____



[Notes]

There will always only be one integer that appears an odd number of times.


[arrays] [bit_operations] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
Find the Number Occurring Odd Number of Times
https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant …
_________
_________
if/else in Python's list comprehension?
https://stackoverflow.com/questions/4260280/if-else-in-pythons-list-comprehension
How can I do the following in Python? row = [unicode(x.strip()) for x in row if x is not None else ''] Essentially: replace all the Nones with empty strings, and then …
_________
_________
How can I count the occurrences of a list item?
https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
Discussions on how to count occurrences in a list without using count() method.
_________
_________
Set vs List
https://stackoverflow.com/questions/2831212/python-sets-vs-lists
Sets are significantly faster when it comes to determining if an object is present in the set
_________

"""


# Your code should go here:

# Requirements:
# - Takes a list.
# - Has only integers in the list.

def findOdd(lst1):
    if isinstance(lst1, list):

        # Check if all the elements in the lst1: list == type(int):
        try:
            for integers in lst1:
                assert isinstance(integers, int)
        except AssertionError:
            return "List input with only integer elements are allowed."

        # To count unique elements.
        uniqueElements = set(lst1)
        countDictionary = {}
        intCount = 0

        # Will also have to work with hashing.
        # Let's try two for loops instead of two while loops.
        for uniq in uniqueElements:
            for ele in lst1:
                if uniq == ele:
                    intCount += 1
            countDictionary[uniq] = intCount
            intCount = 0

        # I have a count dictionary now.
        print(countDictionary)

        # I have to now somehow value return it.
        for key, output in countDictionary.items():
            if output % 2 != 0:
                print(f"key: {key}")
                return f"value - output: {output}"

        return countDictionary


print(findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))  # ➞ -1

print(findOdd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))  # ➞ 5

print(findOdd([10]))  # ➞ 10
