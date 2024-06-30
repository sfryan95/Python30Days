# Day 4: 30 Days of python programming

# print('Thirty ' + 'days ' + 'of ' + 'python')

# print('Coding ' + 'for ' + 'all')

company = 'Coding For All'

# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())
# print(company[6:])
# print(company.index('Coding'))
# print(company.replace('Coding', 'Python'))
# print(company.split())
# print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))
# print(company[0])
# print(company[-1])
# print(company[10])

def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

# print(create_acronym(company))
# print(create_acronym('Python For Everyone'))

# print(company.index('C'))
# print(company.index('F'))
# print('Coding For All People'.rfind('l'))
# print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
# print('You cannot end a sentence with because because because is a conjunction'[31:55])

# print(company.startswith('Coding'))
# print(company.endswith('coding'))
# print('   Coding For All      '.strip())
# print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
# print('I am enjoying this challenge. \nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2

print('The area of a circle with radius {} is {} meters square.'.format(radius, area))
print(f'The area of a circle with radius {radius} is {area} meters square.')

a = 8
b = 6

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')

