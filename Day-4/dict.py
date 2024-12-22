my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name']) 

my_dict['age'] = 26  # Modifying
my_dict['occupation'] = 'Engineer'  # Adding
print(my_dict)

if 'age' in my_dict:
    print('Age is present in the dictionary')

for key, value in my_dict.items():
    print(key, value)    