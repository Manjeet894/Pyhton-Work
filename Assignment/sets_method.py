

"""
--- Sets Method's ---

add() -> Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""



fruitsSet = {"orange","apple","mango"}
fruitsSets= {"pomegarante","kiwi","pinaple"}

print("\n Access Sets ",fruitsSet)

fruitsSet.update(fruitsSets)
print("\n Updated Set",fruitsSet)

fruitsSet.remove("kiwi")
print("\n Updated Set after remove",fruitsSet)


fruitsSet.discard("mango")
print("\n Updated Set after discard",fruitsSet)

x = fruitsSets.pop()

print("\n removing using pop : ",x)
print("\n uodated after pop mehtod",fruitsSets)

fruitsSets.clear()
print("\n updated after clear method",fruitsSets)

"""
del fruitsSets
print("\n sets deleted using del method",fruitsSets)

"""

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("\n union of two sets : ",set3)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print("\n Check the elements and give common element",x)