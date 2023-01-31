"""
---- using method in list in python ----

append -> (used to add item into a string)
extend -> (used to merge the item of two list in one)
pop	-> (used to remove a item using index)
clear -> (used to clear the item from the list)
insert -> (used to insert a item in list on a specific index)
remove -> (used to remove to a item from list)
copy -> (used to copy list but don't modified data in it)
count -> (return the number of times the value in the list)
index -> (This method returns the index of the specified element in the list.)
reverse -> (Reverse the order of the list)
sort -> (sort the item list and use (reverse = True) for decending order)

"""

list = [4109,"Manjeet","BCA","Pggc-11"]
print("\n",list)

list.append("Haryana")
print("\n add using append method ",list)

list.insert(5,"2022-2023")
print("\n add using insert method at a specific index",list)

list2 = [4067,"Vinayak","BCA","Pggc-11"] # second list

list.extend(list2)
print("\n Empty list using clear method",list)

list2.pop(3)
print("\n remove item using pop method at a specific index",list)

list2.clear()
print("\n Empty the list using clear method",list2)

list.remove("2022-2023")
print("\n remove a item using remove method",list)

my_list = list.copy()
print("\n Using a copy method to Copied List : ",my_list)

intList = [1,2,2,3,4,2,5,6,7,2]
x = intList.count(2)
print("\n Item count from the list ",x)


index = list.index("Manjeet")
print("\n Access Index of list item",index)

list.reverse()
print("\n Reverse the item of list",list)

fruitList =["Mango","apple","Orange","Banana","cherry"]
fruitList.sort(key = str.lower)
print("\n Sorted list",fruitList)
fruitList.sort(reverse=True)
print("\n Sorted list in decending order",fruitList)
