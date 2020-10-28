# Python Collections (Arrays)

# List
# Create a List
list1 = ["apple","banana","strawberry","watermelon","pineapple", "orange"]
print(list1)

# Access items list
print(list1[0])
print(list1[2])

# negative indexing
print(list1[-1])    # pineapple

# range of indexes
print(list1[2:5])   # ['strawberry', 'watermelon', 'pineapple']
print(list1[:3])    # ['apple', 'banana', 'strawberry']
print(list1[4:])    # ['pineapple', 'orange']

# range of negative indexes
print(list1[-4:-2]) # ['strawberry', 'watermelon']

# change item value
list1[1] = "mango"
print(list1)        # ['apple', 'mango'...]

# loop through a list
for x in list1:
    print(x)

# check if item exists
if "mango" in list1:
    print("Yes, 'apple' is in the fruit list")

# list length
print(len(list1))   # 6

# add items
# using the append() method to append an item
list1.append("banana")  
print(list1)        # ['apple', 'mango', 'strawberry', 'watermelon', 'pineapple', 'orange', 'banana']

# to add item at the specific index, use the insert() method
list1.insert(3, "cherry")
print(list1)        # ['apple', 'mango', 'strawberry', 'cherry', ...]

# remove item
list1.remove("pineapple")
print(list1)        # ['apple', 'mango', 'strawberry', 'cherry', 'watermelon', 'orange', 'banana']

list1.pop()
print(list1)        # ['apple', 'mango', 'strawberry', 'cherry', 'watermelon', 'orange']
list1.pop()
print(list1)        # ['apple', 'mango', 'strawberry', 'cherry', 'watermelon']

del list1[0]
print(list1)        # ['mango', 'strawberry', 'cherry', 'watermelon']

# The list() constructor
mylist = list(("apple", "banana", "cherry"))
print(mylist)






