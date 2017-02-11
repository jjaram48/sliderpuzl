import random
from random import randint

w, h = 3, 3;  # Defines width and height of the initialState Array

initialState = [[0 for x in range(w)] for y in range(h)]

stateSpace = []  # Calculation of possibilities

actions = []  # up,down, left, right

# initGoalState = [[1, 2, 3][4, 5, 6][7, 8, 0]]

# goalState = tuple(initGoalState)

for i in initialState:
    # randint(0, 9)
    random.sample(range(0, 9), 3)
    # for j in initialState:

# print(randint(0,9))

print(initialState)
