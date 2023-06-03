"""
##Probabilities (Part 1)

Given a list of numbers and a value n, write a function that returns the probability of choosing a
number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.


[Examples]

___
probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
_____



[Notes]

___
*) Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
*) The numbers in the list are uniformly distributed, and have an equal chance of being chosen.
___



[arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
round() Method
https://www.programiz.com/python-programming/methods/built-in/round
Returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is provided, it rounds off the number to the nearest in …
_________
_________
filter() Method
https://www.geeksforgeeks.org/filter-in-python/
Filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
_________
_________
len() Method
https://www.geeksforgeeks.org/python-string-length-len/
Returns the length of the string.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
""" 
# Your code should go here:

def probability(lst1, theNum):
    outputLst1 = []
    tPossibleOutcomes = lst1.len()
    sortLst1 = lst1.sort() # Step.
    lastEle = sortLst1[-1]
    range1 = range(0, lastEle+1) # Total elemental range.
    i = 0
    while(i < lastEle + 1):
        if range1[i] => theNum:
            outputLst1.append(range1[i])
            i = i + 1
    favourableOutcomes = outputLst1.len()
    return "{0}%".format(100 * (favourableOutcomes / tPossibleOutcomes))

print(probability([5, 1, 8, 9], 6)) # ➞ 50.0

print(probability([7, 4, 17, 14, 12, 3], 16)) # ➞ 16.7

print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6)) # ➞ 70.0


# testing.
# checkAgain.
# checkAgain. Check all the resources again.

