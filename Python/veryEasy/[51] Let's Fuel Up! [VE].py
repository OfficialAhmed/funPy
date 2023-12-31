"""
####  Let's Fuel Up!  ####

A vehicle needs 10 times the amount of fuel than the distance it travels.
However, it must always carry a minimum of 100 fuel before setting off.
Create a function which calculates the amount of fuel it needs, given the distance.


[Examples]

___
calculate_fuel(15) ➞ 150

calculate_fuel(23.5) ➞ 235

calculate_fuel(3) ➞ 100
_____



[Notes]

___
*) Distance will be a number greater than zero.
*) Return 100 if the calculated fuel turns out to be less than 100.
___



[control_flow] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
max() Method
https://forum.freecodecamp.org/t/the-python-max-function-explained-with-examples/19205
Returns the largest item in an iterable or the largest of two or more arguments.
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=fo7hXynbkxI
In this video, you will learn how to solve these: 0:20 Are the Numbers Equal?, 2:08 Let's Fuel Up!, 4:31 Luke, I Am Your ...
_________

"""


# Your code should go here:

def calculateFuel(distance):
    if distance >= 0:
        formula = distance * 10

        if formula < 100:
            return 100
        elif formula >= 100:
            return formula

    elif distance < 0:
        return "Distance cannot be negative."


print(calculateFuel(15))  # ➞ 150

print(calculateFuel(23.5))  # ➞ 235

print(calculateFuel(3))  # ➞ 100

print(calculateFuel(0))

print(calculateFuel(10))

print(calculateFuel(10.1))

print(calculateFuel(-0.1))

# complete.
