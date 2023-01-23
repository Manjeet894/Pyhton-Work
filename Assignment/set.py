"""
 ---------Sets----------

items are unchangeable, but you can remove and add new items
Duplicates Not allowed
Can't access item using index or key


"""

mySet = {"Manjeet",4109,"BCA",True}
print("Access sets",mySet)

# Get the length of sets using len() function..

print("\n Getting Length of sets",len(mySet))

print("\n Check or access items present in set", mySet)
print("Manjeet" in mySet) # returns value in boolen true/false...


# adding or update items into sets using add() method
# Adding

print(mySet)

mySet.add("Haryana")
print("\n Adding item in sets",mySet)

# Updating

print("\n",mySet)
mySet2 = {"Pggc - 11 "}

mySet.update(mySet2)

print("\n After Updating",mySet)

# Removing items using remove() method item, clear() method empties the set
# del() keyword delete the set completely



print("\n Before Removing",mySet)

mySet.remove("BCA")
print("\n After removing ",mySet)

"""
---Some Methods
.remove()
.discard()
.pop()
.clear()
.del()

"""












