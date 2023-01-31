""""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}







car.pop("model")
print("\n using pop method",car)

print(car.get('model'))

# Python3 code to demonstrate working of 
# Mapping key values to Dictionary
# Using dictionary comprehension
  
# initializing list
test_list = [{'name' : 'Manjeet', 'age' : 23}, 
             {'name' : 'Akshat',  'age' : 22},
             {'name' : 'Nikhil', 'age' : 21}]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Mapping key values to Dictionary
# Using dictionary comprehension
res = {sub['name'] : sub['age'] for sub in test_list}
  
# printing result 
print("The flattened dictionary is : " + str(dict(res))) 



def test(d):
  return max(d, key = d.get), min(d, key = d.get)

students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print("\nFinds the key of the maximum and minimum value of the said dictionary:")
print(test(students))



person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# key_name = input("\n Enter the Country Name : ")
# Get the list of keys and check if 'country' key is present
key_name = 'country'
if key_name in person.keys:
    print("country name is", person[key_name])
else:
    print("Key not found")
# Output country name is USA