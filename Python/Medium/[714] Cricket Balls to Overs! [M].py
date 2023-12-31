"""
####  Cricket Balls to Overs!  ####

In cricket, an over consists of six deliveries a bowler bowls from one end.
Create a function that takes the number of balls bowled by a bowler and
calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.


[Examples]

___
total_overs(2400) ➞ 400

total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

total_overs(945) ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

total_overs(5) ➞ 0.5
_____



[Notes]

The number following the decimal point represents the balls remaining after the last over. Therefore, it will only ever have a value of 1-5.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
divmod() Method
https://www.programiz.com/python-programming/methods/built-in/divmod
Takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
_________
_________
Over
https://en.wikipedia.org/wiki/Over_(cricket)
Consists of six consecutive legal deliveries bowled from one end of a cricket pitch to the player batting at the other end, almost always by a single bowler.
_________
_________
How to Use the % Operator
https://realpython.com/python-modulo-operator/
Look at the mathematical concepts behind the modulo operation and how the modulo operator is used with Python's numeric types. You'll also see ways to use the modulo op …
_________
_________
Floor Division
https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
Also referred to as integer division. The resultant value is a whole integer, though the result’s type is not necessarily int.
_________

"""


# Your code should go here:

def totalOvers(ballsBowled):
    results = divmod(ballsBowled, 6)
    # return "Over: {0}, Balls: {1} left".format(results[0], results[1])
    return "{0}.{1}".format(results[0], results[1])


# print(totalOvers(2400))  # ➞ 400
#
# print(totalOvers(164))  # ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.
#
# print(totalOvers(945))  # ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.
#
# print(totalOvers(5))  # ➞ 0.5


def totalOversTotal(ballsBowled):
    overs = ballsBowled // 6
    balls = (int(((ballsBowled / 6) - overs) * 10))
    # balls = divmod(balls, 2)
    balls = int(balls) // 2
    # balls = float(balls) // 2
    # Formatting technique se ho sakta hai filhal ke liye toh. # But, I don't kn
    # now that technique so I will use formula method.

    return balls
    # print(balls)
    # return overs


print(totalOversTotal(2400))  # ➞ 400

print(totalOversTotal(164))  # ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

print(totalOversTotal(945))  # ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

print(totalOversTotal(5))  # ➞ 0.5

# inc.
