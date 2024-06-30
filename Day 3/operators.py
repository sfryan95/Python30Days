# Day 3: 30 Days of python programming

import math

age = 29
height = 6.2
formula = 1 + 1j

# base = int(input('Please enter a base length: '))
# height2 = int(input('Please enter a height length: '))
# print('The area of the triangle is ' + str(base*height2))

# a = int(input('Please enter the first triangle side length: '))
# b = int(input('Please enter the second triangle side length: '))
# c = int(input('Please enter the third triangle side length: '))
# print('The perimeter of the triangle is ' + str(a+b+c))

# length = int(input('Please enter rectangle length: '))
# width = int(input('Please enter rectangle width: '))
# print('The area of the rectangle is ' + str(length*width))
# print('The perimeter of the rectangle is ' + str(2 * (length+width)))

# radius = int(input('Please enter a circle radius: '))
# print('The area of the circle is ' + str(math.pi * (radius**2)))
# print('The circumference of the circle is ' + str(2 * math.pi * radius))

slope1 = 2
x_inter = 1
y_inter = 2

x1, x2 = 2, 6
y1, y2 = 2, 10
slope2 = (y2 - y1) / (x2 - x1);

# print(slope1 == slope2)

# x = int(input('Please enter an x value: '))
# y = (x**2) + (6*x) + 9
# print(y)

# print(len('python') != len('dragon'))

# print('on' in 'python' and 'on' in 'dragon')

# sentence = 'I hope this course is not full of jargon'

# print('jargon' in sentence)

# print('on' not in 'python' and 'on' not in 'dragon')

# print(type(float(len('python'))), type(str(len('python'))))

# print((2 % 2) == 0)

# print((7//3) == int(2.7))

# print(type('10') == type(10))

# print(int(9.8) == 10)

# hours = int(input('Please enter hours worked: '))
# rate = int(input('Please enter hourly rate: '))
# print('Your weekly earning is $' + str(hours * rate))

# seconds_in_year = 31536000
# years = int(input('How old are you? '))
# print('You have lived for ' + str(seconds_in_year * years) + ' seconds')

# Function to generate the table
def generate_table():
    for i in range(1, 6):
        print(f"{i} 1 {i} {i**2} {i**3}")

# Call the function to display the table
generate_table()