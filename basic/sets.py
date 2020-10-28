# Python Sets

# set
set1 = {"Spiderman", "Ironman", "Thor"}
print(set1)                 # set(['Spiderman', 'Ironman', 'Thor'])

# access items
for x in set1:
    print(x)

print("Ironman" in set1)    # true

# add items
# use the add() method
set1.add("Hulk")
print(set1)                 # set(['Spiderman', 'Ironman', 'Hulk', 'Thor'])

# add multiples items
set1.update(["Wolverine", "Capitan America"])
print(set1)                 # set(['Spiderman', 'Hulk', 'Thor', 'Wolverine', 'Capitan America', 'Ironman'])

# get the length of a set
print(len(set1))            # 6

# remove item
set1.remove("Hulk")
print(set1)                 # set(['Spiderman', 'Thor', 'Wolverine', 'Capitan America', 'Ironman'])

# remove the last item
# use the pop() method
superheroe = set1.pop()
print(superheroe)           # Spiderman
print(set1)                 # set(['Thor', 'Wolverine', 'Capitan America', 'Ironman'])

# clear
set1.clear()
print(set1)                 # set([])

# del set1
# print(set1)               # NameError: name 'set1' is not defined

# join two sets
set2 = {"a", "b", "c"}
set3 = {1, 3, 5}

set4 = set2.union(set3)
print(set4)                 # set(['a', 1, 'c', 'b', 5, 3])

