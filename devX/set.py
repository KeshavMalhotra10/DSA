# sets
"""
store non-duplicate items
very fast access vs lists
math set ops (union, intersection)
sets are unordered
"""

# constructors

x = {3, 5, 3, 5}  # duplicates are removed
print(x)

y = set()
print(y)

list1 = [2, 3, 4]

z = set(list1)
print(z)

# set operations

x = {3, 8, 5}
x.add(7)
print(x)

x.remove(3)
print(x)

# pop random item from set x

print(x.pop(), x)

# delete all items from set x
x.clear()
print(x)


s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)  # intersection(occurs in both)
print(s1 | s2)  # union(all items from both, non duplicates)
print(s1 ^ s2)  # symmetric difference (items in either but not both)
print(s1 - s2)  # difference (items in s1 but not in s2)
print(s1 <= s2)  # subset (s1 is a subset of s2)
print(s1 >= s2)  # superset (s1 is a superset of s2)
