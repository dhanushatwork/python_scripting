#Reverse a linked list.

# what is list
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


my_list = ["love", "laughter", "war"]
print(my_list)
#len of list
print(len(my_list))
#List items can be of any data type:
list1 = [1,2,3,4,5]
list2 = ["money", "rich", "tax"]
list3 = [True, False]
print(list1)
print(list2)
print(list3)

#change item in list
list2[2] = "high"
print(list2)

#insert
list2.insert(3, "power")
print(list2)

#append - adds item to end of the list
list2.append("guns")
print(list2)

#add any iteratable
new_tuple = ("durgs","cars")
list2.extend(new_tuple)
print(list2)

#loop directly in list
for x in list2:
    print(x)
#looping thru index
for i in range(len(list2)):
    print(list2[i])
#looping thru while
y = 0
while y < len(list2):
    print(list2[y])
    y = y + 1

#list() constructor
#The list() constructor in Python is used to create a new list object. It can take an iterable as an argument 
# and convert it into a list. If no argument is provided, it creates an empty list.

string = "welcome to the world of vanmam"
# string = (1,2,3)
# string = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
list_data = list(string)
print(list_data[:-2])
if "x" in string:
    print("This list has letter 'A' in it")
else:
    print("Invalid condition")


#List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
emp_sal = [100000, 85000, 45000, 70000, 25000, 90000, 30000]
high_sal_list = []
for a in emp_sal:
    if a > 40000:
        high_sal_list.append(a)

high_sal_list.sort()
print(high_sal_list)       


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
def cusfun(n):
    return abs(n - 50)

num_list = [100, 75, 15, 85, 69, 77]
num_list.sort(key=cusfun)
print(num_list)