#LISTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#append - to add something
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

#copy
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)
# Output: [1, 2, 3, 4, 5]

#count
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print(count)
# Output: 4

#extend - connect some lists
fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)

#insert
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

#just modified
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25 # Modifying the second element
print(my_list)
# Output: [10, 25, 30, 40, 50]


#pop
my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop(2) # Removes and returns the element at index 2
print(removed_element)
# Output: 30
print(my_list)
# Output: [10, 20, 40, 50]

my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop() # Removes and returns the last element
print(removed_element)
# Output: 50
print(my_list)
# Output: [10, 20, 30, 40]


#remove
my_list = [10, 20, 30, 40, 50]
my_list.remove(30) # Removes the element 30
print(my_list)
# Output: [10, 20, 40, 50]

#reverse
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# Output: [5, 4, 3, 2, 1]



#slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])
# Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])
# Output: [1, 2, 3] (elements from the beginning up to index 2)
print(my_list[2:])
# Output: [3, 4, 5] (elements from index 2 to the end)
print(my_list[::2])
# Output: [1, 3, 5] (every second element)


#sort
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)
# Output: [1, 2, 5, 8, 9]

my_list = [5, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)
# Output: [9, 8, 5, 2, 1]



#index
fruits = ("apple", "banana", "orange","apple")
print(fruits.index("apple")) #Returns the index value at which apple is present.
#Output: 0





#DICTIONARY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#image we have dictionary person:

#modify values
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"  # Update the existing value for the same key

#del - delete
del person["Country"]

#update in dict
person.update({"Profession": "Doctor"})

#clear
grades.clear()

#check for
if "name" in person:
    print("Name exists in the dictionary.")

#got all keys from dict to list
person_keys = list(person.keys())

#extract all values from dict to list
person_values = list(person.values())

#all values frm dict to list
info = list(person.items())

#SETS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#discard in sets
fruits.discard("apple")

#subset
is_subset = fruits.issubset(colors)

#issuperset
is_superset = colors.issuperset(fruits)


#set operators
combined = fruits.union(colors)
common = fruits.intersection(colors)
unique_to_fruits = fruits.difference(colors)
sym_diff = fruits.symmetric_difference(colors)
