import random

initialIndex = random.sample(range(0, 9), 9)

stateSpace = []  # Calculation of possibilities

actions = []  # up,down, left, right

initGoalState = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]     # Divides an array in equal chunks

initialState = lol(initialIndex, 3)

print(initialIndex)
print(initialState)
