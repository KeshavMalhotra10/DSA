# dictionary stores key value pairs

fruit = {"apple": 5, "bananas": 4.50, "carrot": 2.75}  # map fruit to price

print(fruit["apple"])

# hashmaps perform operations in constant time o(1)
# hashmaps don't store duplicates. Every key is unique
# hashmaps are unordered, keys are not stored in any order


# hashshets:
"""
only store keys
instead of storing fruit and price
hashset will only store fruits
useful for checking if fruit is in stock
"""

# When to use hashmaps or sets
"""
Hashmap
-------
dictionaries
counting frequencies
storing key-value pairs
quick lookups

Hashsets
--------
store unique elements
marking elements as used or visited
check duplicates

"""
# in a problem pay attention to keywords:
"""
keywords
--------
frequency
unique
map
dictionary
fast lookup
"""

# 2 sum - unsorted
# 1.if needed in map then return pair
# 2 populate hash map with each number and corresponding index
# 3. check 1 to 2

# solution
# --------
"""
def pair_sum_unsorted_two_pass(nums, target):
    hash_map = {}  # store num and indice
    for i, num in enumerate(nums):
        needed = target - num
        if needed in hash_map:
            return [hash_map[needed], i]
        hash_map[num] = i
"""

# Verify Sudoku Board
"""
Given a partially completed 9x9 Sudoku board, determine if the current state of the board
adheres to the rules of the game:
• Each row and column must contain unique numbers between 1 and 9, or be empty
(represented as 0).
• Each of the nine 3x3 subgrids that compose the grid must contain unique numbers
between 1 and 9, or be empty.
Note: You are asked to determine whether the current state of the board is valid given
these rules, not whether the board is solvable.


"""

# solution
# --------
# 1. check whether row is unique
# 2. check whether column is unique
# 3. view the sudoku board as a 3x3 column such that rows and columns are 0,1,2
# 4. if ever the board becomes non-unique, return False


def verify_board(board):
    # create has shets for each row, column, and subgrid to keep track
    # of numbers previously seen on any given row, column, or subgrid
    row_sets = [
        set() for _ in range(9)
    ]  # note I use _ instead of a character, we do this to say arbritary variable not used further
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            # check if num has been seen in current row, column, or subgrid
            if num in row_sets[r]:
                return False
            if num in column_sets[c]:
                return False
            if (
                num in subgrid_sets[r // 3][c // 3]
            ):  # we do //3 because we made a 9x9 into a 3x3
                return False

            # if we passed above checks, mark value as seen and add it to
            # corresponding hashsets
            row_sets[r].add(num)
            column_sets(c).add(num)
            subgrid_sets[r // 3][c // 3].add(num)
        return True
