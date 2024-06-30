# Day 8: 30 Days of python programming

dog = {}
dog['name'] = 'spot'
dog['color'] = 'white'
dog['breed'] = 'lab'
dog['legs'] = 4
dog['age'] = 7

student = {
  'first_name': 'Sean',
  'last_name': 'Ryan',
  'gender': 'male', 
  'age': 29,
  'is_married': False, 
  'skills': ['JavaScript', 'Python'], 
  'country': 'USA', 
  'city': 'Napa'
}

print(len(student))
print(student['skills'], type(student['skills']))
student['skills'].append('React')
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())
del student['city']
print(student)
del dog

