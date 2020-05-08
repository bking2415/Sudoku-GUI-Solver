import random

# print(random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=9))
# print(random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=9))


# cube = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=9)
#
# # print(cube)
#
#
# # function to get unique values
# def unique(list):
#     # initialize a null list
#     unique_list = []
#     values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     # traverse for all elements
#     for x in list:
#         if x == 0:
#             unique_list.append(x)
#         # check if exists in unique_list or not
#         else:
#             if x not in unique_list:
#                 unique_list.append(x)
#                 values.remove(x)
#                 # print(values)
#             else:
#                 # Choose a random value that has not been used already
#                 rand = random.sample(values, k=1)
#                 # print(rand[0])
#                 values.remove(rand[0])
#                 unique_list.append(rand[0])
#                 # print(values)
#     # Print list
#     # for x in unique_list:
#     #     print(x)
#     return unique_list
#
# table = unique(cube)
# print(unique(cube))
#
# rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
base = 3
side = base * base


# pattern for a baseline valid solution
def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return random.sample(s, len(s))


def createBoard():
    rBase = range(base)

    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board


# print(createBoard())

# def createBoard():
#     board = []
#
#     for i in range(9):
#         cube = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=9)
#         board.append(unique(cube))
#
#     return board

# print(createBoard())
