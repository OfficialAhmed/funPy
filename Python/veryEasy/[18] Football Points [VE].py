"""
####  Football Points  ####

Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
___
*) wins get 3 points
*) draws get 1 point
*) losses get 0 points
___



[Examples]

___
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0
_____



[Notes]

Inputs will be numbers greater than or equal to 0.


[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.programiz.com/python-programming/operators
Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
_________
_________
Three Points for a Win
https://www.rookieroad.com/soccer/rules-and-regulations/scoring-rules/
Is a standard used in many sports leagues and group tournaments, especially in association football, in which three (rather than two) points are awarded to the team win …
_________
_________
Soccer Scoring Rules
https://www.rookieroad.com/soccer/rules-and-regulations/scoring-rules/
In the sport of soccer, teams work together to to score goals, because goals win the game. A goal is when the ball fully crosses the goal line between the goalposts and …
_________

"""


# Your code should go here:

def football_points(wins, draws, losses):
    if wins and draws and losses < 0:
        return "Inputs should be zero or greater."
    else:
        formula = wins * 3 + draws
        return formula


print(football_points(3, 4, 2))  # ➞ 13

print(football_points(5, 0, 2))  # ➞ 15

print(football_points(0, 0, 1))  # ➞ 0

print(football_points(113, 13, -1))

# complete.
