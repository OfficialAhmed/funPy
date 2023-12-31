"""
####  Convert Hours into Seconds  ####

Write a function that converts hours into seconds.


[Examples]

___
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
_____



[Notes]

___
*) 60 seconds in a minute, 60 minutes in an hour
*) Don't forget to return your answer.
___



[language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Math in Python
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Being able to effectively perform mathematical operations in programming is an important skill to develop because of how frequently you’ll be working with numbers. Thou …
_________
_________
Conversion of Hours into Seconds
https://www.math-only-math.com/conversion-of-hours-into-seconds.html
We know 1 hour is equal to 3600 seconds, which is required to convert the measuring time from hours to seconds.
_________
_________
How many seconds are in an hour?
https://www.rapidtables.com/calc/time/seconds-in-hour.html
One hour has 60 minutes and one minute has 60 seconds.
_________
_________
How to Do Math
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Video Tutorial for Challenge
https://youtube.com/watch?v=Lz0GzT_A0CY
Video tutorial of this challenge.
_________

"""


# Your code should go here:

def howManySeconds(n):
    return n * pow(60, 2)


print(howManySeconds(2))  # ➞ 7200

print(howManySeconds(10))  # ➞ 36000

print(howManySeconds(24))  # ➞ 86400
