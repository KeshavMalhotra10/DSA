# lists
"""
General purpose
Most widely used data strucutre
Grow and shrink size as needed
Sequence type
Sortable
"""

# creating a new list
x = list()

y = ["a", 25, "dog", 8.43, True]

tuple1 = (10, 20)

z = list(tuple1)

# list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i > 4]
print(b)

# extend
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)
print(x)

x = [5, 3, 8, 6]
x.pop()  # pops of the 6
print(x)
print(x.pop())
