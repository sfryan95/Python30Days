# Day 2: 30 Days of python programming

import math

first_name = 'Sean'
last_name = 'Ryan'
full_name = 'Sean Ryan'
country = 'USA'
city = 'Napa'
age = 29
year = 2024
is_married = False
is_true = True
is_light_on = False
fav_food, fav_color = 'pasta', 'blue'

print(type(first_name)) # string
print(type(last_name)) # string
print(type(full_name)) # string
print(type(country)) # string
print(type(city)) # string
print(type(age)) # int
print(type(year)) # int
print(type(is_married)) # Bool
print(type(is_true)); # Bool
print(type(is_light_on)) # Bool
print(type(is_light_on)) # Bool
print(type(fav_food), type(fav_color)) # str

print(len(first_name)) # 4

print('My first name is ' + str(len(first_name)) + ' letters long and my last name is ' + str(len(first_name)) + ' letters long!')

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

area_of_circle = math.pi * (30 ** 2)
circum_of_circle = 2 * math.pi * 30

print(area_of_circle)
print(circum_of_circle)

print(math.pi * (int(input('Please enter a radius: ')) ** 2))

first_name2 = input('Please enter your first name: ')
last_name2 = input('Please enter your last name: ')
country = input('Please enter the country you are from: ')
age = input('Please enter your age: ')