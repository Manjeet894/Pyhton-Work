
#Tuple's


mytuple = (4109, "Manjeet","BCA",True)

print("\n Data type in tuples",mytuple)

"""
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
index[0]
for one item you must enter the comma after the item i.e. ("Hello",)

"""

# Access the tuples...

print("\n Access the tuple's with indexing",mytuple[1])

"""
------- At Glance -------
Negative Indexing
Range of indexes and Negative indexes
Check item using if condition..

"""

#update Tuples

"""
First convert into list and update it and again convert into tuples..

"""

tuple1 = list(mytuple)
tuple1[1] = "Manjeet Saini"
mytuple = tuple(tuple1)

print("\n Update tuples",mytuple)

"""
remove() to remove items from tuples
can't remove items in a tuples,
To remove item in a tuple you need to follow the same proccess in update  
"""

tuple2 = list(mytuple)
tuple2.remove(True)
mytuple = tuple(tuple2)

print("\n Remove item from tuple ",mytuple)

# del() keyword use to delete the complete tuple

mytuple2 = ("Hello Manjeet", 4109)
print("New tuple", mytuple2)

del mytuple2
# print("After deleting",mytuple2) & show error because tuple not exits
