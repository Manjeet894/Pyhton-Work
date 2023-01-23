# --------List in Python-----------

# String, int and boolean data types:

myList =["apple","mango","orange"]
myIntList =[1,2,3,4,5]
myBoolList = [True,False,True]

print("\n -----Lists and access whole list-----")

print(myList)   #show the whole list
print(myIntList)   #show the whole list
print(myBoolList)   #show the whole list

#print(type(myList))


# Access list items
print("\n --accessing list item with index--")
print(myList[1])

# Change or update list items

print("\n Update list Items ")

friends = ["serry","joban","vinayak","atul","dheeraj"]

print(" Friends List Before Updation", friends)

friends[3] ="Priyanshu"

print(" Friends List After Updation",friends)


# Add or insert into List items 
print("\n Add or insert into list item ")
print("\n",friends)
friends.append("Akash")
print("After item insert using append function ",friends) #insert at end of the list 

friends.insert(1,"Gourav")
print("\nInsert specified index ",friends) #insert at specified index

# Remove or delete from the list 
print("\n Remove & deletion from list")
print(friends)
friends.remove("Akash")
print(friends)

"""
Some Remove or delete function

.pop() remove a sepecified index item / without indexing it removes the last item from the list 
 del listName[] remove a sepecified index item / delete the whole list
.clear() delete all items in a list & list still remain  

"""

