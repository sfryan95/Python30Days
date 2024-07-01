# Day 12: 30 Days of python programming

from random import randint
import random
import string

def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
  
# def random_user_id(num):
#   user_id = ''
#   random_letter = string.ascii_letters
#   random_num = string.digits
#   for i in range(num):
#     if randint(0, 100) % 2 == 0:
#       user_id += random_num[randint(0, 9)]
#     else:
#       user_id += random_letter[randint(0, 25)]
#   return user_id

# print(random_user_id())

# def user_id_gen_by_user():
#   num_chars = int(input('Please enter id length: '))
#   num_ids = int(input('Please enter number of ids to generate: '))
  
#   for i in range(num_ids):
#     print(random_user_id(num_chars))

# user_id_gen_by_user()

def rgb_color_gen():
  return f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'

# print(rgb_color_gen())

def list_of_hexa_colors(num):
  colors = []
  letters = 'abcde'
  color = '#'
  for i in range(num):
    for i in range(6):
      if randint(0,1) % 2 == 0:
        color += random.choice(letters)
      else:
        color += str(randint(0,9))
    colors.append(color)
    color = '#'
  print(colors)

# print(list_of_hexa_colors(2))

def list_of_rgb_colors(num):
  colors = []
  for i in range(num):
    colors.append(rgb_color_gen())
  print(colors)

# print(list_of_rgb_colors(2))

def generate_colors(color_type, num):
  if color_type == 'hexa':
    list_of_hexa_colors(num)
  elif color_type == 'rgb':
    list_of_rgb_colors(num)

generate_colors('hexa', 4)
generate_colors('rgb', 4)

def suffle_list(lst):
  lst1 = []
  lst2 = []
  new_lst = lst.copy()
  i = 0
  while len(new_lst) > 0:
    if len(new_lst) % 2 == 0:
      lst1.append(new_lst[i])
    else:
      lst2.append(new_lst[i])
    del new_lst[i]
  return lst1 + lst2

print(suffle_list([1,2,3,4,5,6,7]))

def random_nums():
  nums = set()
  while len(nums) < 7:
    nums.add(randint(0, 9))
    
  return list(nums)

print(random_nums())
