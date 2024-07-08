# Day 18: 30 Days of python programming
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
def most_frequent_words(str):
  # regex_patern = r'[a-z]'
  # lowercase_str = str.lower().split(' ')
  cleaned_str  = re.sub(r'[^\w\s]', '', str)
  lowercase_list = cleaned_str.lower().split(' ')
  
  word_count = dict()
  
  for word in lowercase_list:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1

  return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

print(most_frequent_words(paragraph))

def is_valid_variable(str):
  regex_pattern = r'[A-Z0-9-]'
  if re.findall(regex_pattern, str):
    return False
  else:
    return True

# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

regex_patern = r'[#%@$&!;]'
cleaned_sentence = re.sub(regex_patern, '', sentence)

# print(cleaned_sentence)

# print(most_frequent_words(cleaned_sentence)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]