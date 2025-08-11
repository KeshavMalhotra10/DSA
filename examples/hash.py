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


def pair_sum_unsorted_two_pass(nums, target):
    hash_map = {}  # store num and indice
    for i, num in enumerate(nums):
        needed = target - num
        if needed in hash_map:
            return [hash_map[needed], i]
        hash_map[num] = i
