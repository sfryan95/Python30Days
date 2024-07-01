# Day 9: 30 Days of python programming

# age = int(input('Enter your age: '))

# if age >= 18:
#   print('You are old enough to drive!')
# else:
#   print(f'You must wait {18-age} years to drive.')

# my_age = 29
# your_age = int(input('Enter your age: '))

# if your_age > my_age and your_age - my_age > 1:
#   print(f'You are {your_age - my_age} years older than me!')
# elif your_age > my_age:
#      print(f'You are {your_age - my_age} year older than me!')
# elif your_age == my_age:
#   print('OMG we are the same age')

# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter another number: '))

# if num1 > num2:
#    print(f'{num1} is greater than {num2}')
# elif num2 > num1:
#    print(f'{num2} is greater than {num1}')
# else:
#    print('Woah the numbers are equal!')

# grade = int(input('Please enter student grade: '))

# if grade >= 90:
#    print('A')
# elif grade < 90 and grade >= 80:
#    print('B')
# elif grade < 80 and grade >= 70:
#    print('C')
# elif grade < 70 and grade >= 60:
#    print('D')
# else:
#   print('F')

# curr_month = input('Please enter the current month: ')

# Autumn = ['September', 'October', 'November']
# Winter = ['December', 'January', 'February']
# Spring = ['March', 'April', 'May']
# Summer = ['June', 'July', 'August']

# if curr_month in Autumn:
#     print('Autumn')
# elif curr_month in Winter:
#     print('Winter')
# elif curr_month in Spring:
#     print('Spring')
# else:
#     print('Summer')

# fruit = input('Please enter a fruit: ')

# fruits = ['banana', 'orange', 'mango', 'lemon']

# if fruit not in fruits:
#     fruits.append(fruit)
# else:
#     print('That fruit already exist in the list')

# print(fruits)

person = {
  'first_name': 'Asabeneh',
  'last_name': 'Yetayeh',
  'age': 250,
  'country': 'Finland',
  'is_marred': True,
  'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address': {
      'street': 'Space street',
      'zipcode': '02210'
  }
}

if person['skills']:
    print(person['skills'][len(person['skills'])// 2])

if person['skills']:
    print('Python' in person['skills'])


if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('Full-Stack Developer')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('Front-end Developer')
elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
    print('Front-end Developer')
else: 
    print('unknown title')

# Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred'] == True:
    married = 'is married.'
else:
    married = 'is not married.'

print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He {married}')