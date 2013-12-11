# CS61A - Lecture 3

# Multiple Environments
#  
# Life Cycle of user defined functions:
# -- Def Statement:
#     Has Name, Formal Parameter, Body
# -- What Happens?
#     A new function is created
#     Name bound to that function in the current frame
# 
# -- Call Expression:
#     Operator and Operands evaluated
#     Function (value of operator) is called on arguments (values of operands)
# 
# -- Calling / Applying
#     A new frame is created
#     Parameters are bound to arguements
#     Body is executed in new environment

from operator import mul
def square(x):
    return mul(x, x)
print(square(square(3)))

# An environment is a sequence of frames
# So Far:
#     - The global frame alone
#     - A local frame, then the global frame
#     - All environments end in the global frame
#     
# 
# Every expression is evaluated in the context of an environment
# 
# A NAME evaluates to the value bound to that name in the earliest
# frame of the current environment in which that name is found.
