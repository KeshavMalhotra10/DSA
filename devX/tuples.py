# tuples
"""
immutable
useful for fixed data
faster than lists
sequence type
"""


# constructors

x = ()
x = (1, 2, 3)
x = 1, 2, 3  # python still knows this is a tuple
x = (2,)  # single value tuple, make sure you have comma

print(x, type(x))

# tuples are immutable, but member objects can be mutable
y = ([1, 2], 3)
del y[0][1]
print(y)

y += (4,)  # concatenation works for tuple
print(y)
