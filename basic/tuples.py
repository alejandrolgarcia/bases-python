# Python Tuple

# create a tuple
tuple1 = ("Batman", "Superman", "WonderWoman", "Flash", "Aquaman", "Cybord", "Green Lantern")
print(tuple1)

# access tuple items
print(tuple1[1])    # Superman

# negative indexing
print(tuple1[-1])   # Green Lantern

# range of indexes
print(tuple1[2:5])  # ('WonderWoman', 'Flash', 'Aquaman')

# change tuple values
tuple2 = list(tuple1)
tuple2[1] = "General Zod"
tuple1 = tuple(tuple2)

print(tuple1)       # ('Batman', 'General Zod', 'WonderWoman', 'Flash', 'Aquaman', 'Cybord', 'Green Lantern')

# loop through a tuple
for x in tuple1:
    print(x)

# check if item exists
if "Flash" in tuple1:
    print("Yes, 'Flash' is in the superheroes tuple")

# tuple length
print(len(tuple1))  # 7

# add items
# tuple1[1] = "Superman"
# print(tuple1)     This will raise an error. Tuples are unchangeable

# remove items
# Note: You cannot remove items in a tuple

# join two tuples
tuple3 = ("a", "b", "c", "d")
tuple4 = (1, 2, 3)
tuple5 = tuple3 + tuple4
print(tuple5)       # ('a', 'b', 'c', 'd', 1, 2, 3)




