#!/usr/bin/env python3

"""
Examples for conditions (if, else...)

https://docs.python.org/3/tutorial/controlflow.html#if-statements

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

# Define some variables
variableA = 1
variableB = "Text"
myAccommodation = "Tent"

# If..else
print("Simple if..else")
if variableA == 1:
    print("Variable is equal to 1")
else:
    print("Variable is unequal to 1")


# If..elif..else. Python does not support switch..case
print("If..elif..else")

if variableA < 0:
    print("variableA < 0")
elif variableA >0:
    print("variableA > 0")
else:
    print("variableA == 0")

# We can also use and, or etc.
print("Compare with \"and\"")
if variableA == 1 and variableB == "Text":
    print("This is true")
else:
    print("This is not true")

# What to try out
#################
# - Try out different conditions with and and or
