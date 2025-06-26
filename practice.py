#LISTS
lst = [0,1,2,3,40,1,32,3]
set = set(lst)
print(type(set))

print (type(lst))

lst.append("qwe")

print(lst)

lst.remove ('qwe')

print(lst)

list1 = [1,2,3,4,5]
print(list1)

list1[0] = 25

print(list1)

list1.remove(25)
print(list1)

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

my_list2 = [1, 2, 3, 4, 5]
my_list2.remove(3)
my_list2.append(6)
print(my_list2)
my_list2.insert(2,6)
print(my_list2)

qwerty = [1,2,3,0,9,8,7]
qwerty.reverse ()
print(qwerty)


qwerty.sort()
qwerty.reverse()
print(qwerty)

x1 = "ovo"
x = "ovefm"
def puck (x):
    if x == x[::-1]:
        print("poly")
    else:
        print("no poly")
puck(x)

def puck (x1):
    if x1 == x1[::-1]:
        print("poly")
    else:
        print("no poly")
puck(x1)

fruits = ("apple", "banana", "orange","apple")
print(type(fruits))

print(fruits.index("apple"))

#DICT
f = {
    "alice":5,
    "bob":3
}
print(type(f))

###SET
print(set)
set.discard(40)
print(set)

fruits = {"apple", "banana", "orange", "grape"}
colors = {"red", "green", "blue", "orange"}
m = fruits.issubset(colors)
print(m)

fruits1 = {"grape", "blue"}
colors1 = {"grape", "blue"}
q = fruits1.issubset(colors1)
print(q)

fruits1 = {"grape", "blue"}
colors1 = {"grape", "blue"}
qq = fruits1.issuperset(colors1)
print(qq)

