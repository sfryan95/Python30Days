# Day 19: 30 Days of python programming
import json
from collections import Counter

def count_lines_and_words (file):
  with open(file, 'r') as f:
    content = f.read()
  num_lines = len(content.splitlines())
  num_words = len(content.split())
  return (num_lines, num_words)

print(count_lines_and_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/donald_speech.txt'))
print(count_lines_and_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/melina_trump_speech.txt'))
print(count_lines_and_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/michelle_obama_speech.txt'))
print(count_lines_and_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/obama_speech.txt'))

def top_ten_langagues(file, num_langauges):
  with open(file, 'r') as json_file:
    country_data = json.load(json_file)
  language_counter = Counter()
  for country in country_data:
    language_counter.update(country['languages'])
  return language_counter.most_common(num_langauges)

print(top_ten_langagues('/Users/seanryan/Desktop/30DaysOfPython/Day 19/countries_data.json', 3))


def most_populated_counteries(file, num_counteries):
  with open(file, 'r') as json_file:
    country_data = json.load(json_file)
  most_populated = sorted(country_data, key=lambda x: x['population'], reverse=True)
  most_populated_names = []
  for country in most_populated[:num_counteries]:
      most_populated_names.append({'country': country['name'], 'population': country['population']}) 
  return most_populated_names
  
print(most_populated_counteries('/Users/seanryan/Desktop/30DaysOfPython/Day 19/countries_data.json', 3))

def find_most_common_words(file, num_words):
  with open(file, 'r') as f:
    content = f.read()
  words = content.split()
  word_counter = Counter(words)
  return word_counter.most_common(num_words)

print(find_most_common_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/donald_speech.txt', 3))
print(find_most_common_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/melina_trump_speech.txt', 3))
print(find_most_common_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/michelle_obama_speech.txt', 3))
print(find_most_common_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/obama_speech.txt', 3))
print(find_most_common_words('/Users/seanryan/Desktop/30DaysOfPython/Day 19/romeo_and_juliet.txt', 10))

import csv

def csv_reader(file):
    with open(file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        python_count = 0
        js_count = 0
        java_count = 0
        for row in csv_reader:
            for cell in row:
                cell_lower = cell.lower()
                if 'python' in cell_lower:
                    python_count += 1
                if 'javascript' in cell_lower:
                    js_count += 1
                if 'java' in cell_lower and 'javascript' not in cell_lower:
                    java_count += 1
    return f'python_count: {python_count}, js_count: {js_count}, java_count: {java_count}'

print(csv_reader('/Users/seanryan/Desktop/30DaysOfPython/Day 19/hacker_news.csv'))