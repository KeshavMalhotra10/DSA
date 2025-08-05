# string
x = "frog"
print(x[3])

# list
x = ["pig", "cow", "horse"]
print(x[1])

# tuple
x = ("kevin", "niklas", "jenny", "craig")
print(x[0])


# slicing - [start: end+1 : step]

x = "computer"

print(x[1:4])
print(x[1:6:2])
print(x[3:])

# concatenating

# string
x = "horse" + "shoe"
print(x)

# list
y = ["pig", "cow"] + ["horse", "goat"]
print(y)

# tuple
z = ("kevin", "niklas") + ("jenny", "craig")
print(z)

# multiplying

# string
x = "horse" * 3
print(x)

# list
y = [8, 5] * 3
print(y)

# tuple
z = (2, 4) * 3
print(z)


# checking membership

x = "bug"
print("u" in x)

# list
y = ["pig", "cow", "horse"]
print("cow" not in y)

# tuple
z = ("kevin", "niklas", "jenny")
print("Niklas" in z)  # case sensitive


# iterating through items in a sequence

x = [7, 8, 3]
for item in x:
    print(item)

# index & item
y = [7, 8, 3]
for index, item in enumerate(y):
    print(index, item)

# find the minimum
# string
x = "bug"
print(min(x))

# list
y = ["pig", "cow", "horse"]
print(min(y))

# tuple
z = ("kevin", "niklas", "jenny")
print(min(z))

# numrical
a = [3, 5, 1, 8, 2]
print(min(a))

# same for maxiumum, max()

print(max(a))


# sum
# list
z = [50, 4, 7, 19]
print(sum(z))

# tuple
y = (50, 4, 7, 19)
print(sum(y[-2:]))  # sums last two elements

# sorting - returns a new list of items in sorted order, no change to og list

# string
x = "bug"
print(sorted(x))

# list
y = ["pig", "cow", "horse"]
print(sorted(y))

# tuple

z = ("kevin", "niklas", "jenny")
print(sorted(z))

# sort by second letter using lambda function

z = ("kevin", "niklas", "jenny")
print(sorted(z, key=lambda k: k[1]))
