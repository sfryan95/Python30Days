# Day 7: 30 Days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['X', 'Meta'])
print(it_companies)
it_companies.remove('X')
print(it_companies)

# the difference between .remove() and .discard() is that if any item is not found using remove it will cause an error, while no error will be thrown with discard

a_and_b = A.union(B)
print(a_and_b)
print(A.intersection(B))
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

age_set = set(age)
print(len(age_set), len(age))

# Explain the difference between the following data types: string, list, tuple and set
# A string is a collection of characters enclosed by quotes.
# A list is an ordered, mutable, and indexed collection of any data types.
# A tuple is an ordered, immutable, and indexed collection of any data types.
# A set is a collection of unordered and unindexed distinct elements.

sentence = 'I am a teacher and I love to inspire and teach people.'
lst = sentence.split()
set = set(lst)

print(f'There are {len(set)} unique words in the provided setence!')