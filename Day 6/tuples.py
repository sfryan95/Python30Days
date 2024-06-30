# Day 6: 30 Days of python programming

tpl = ()

brothers = ('Cyrus', 'Trent', 'Ryan', 'Justin')

sisters = ('Erin', 'Mac', 'Phoebe')

siblings = brothers + sisters
print(siblings)

print(len(siblings))

print(siblings)
family_members = siblings + ('Lynn', 'Chief')
print(family_members )

*sibs, mother, father = family_members
print(sibs)
print(mother)
print(father)

fruits = ('apple', 'orange')
vegs = ('brussels', 'carrots')
animal_prods = ('steak', 'pork')

food_stuff_tp = fruits + vegs + animal_prods
print(food_stuff_tp)
food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)
middle_indx = len(food_stuff_lst) // 2
print(food_stuff_lst[middle_indx - 1: middle_indx + 1])
print(food_stuff_lst[0:3])
print(food_stuff_lst[-3:])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
