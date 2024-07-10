# Day 20: 30 Days of python programming
from collections import Counter
import requests # importing the request module
import re
import statistics

# url = 'http://www.gutenberg.org/files/1112/1112.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page


def find_most_common_words(url, num_words):
  response = requests.get(url)
  text = response.text
  words = re.findall(r'\b\w+\b', text.lower())
  word_counter = Counter(words)
  return word_counter.most_common(num_words)

# print(find_most_common_words('http://www.gutenberg.org/files/1112/1112.txt', 10))

def get_cats_weight_stats(cats_api):
    response = requests.get(cats_api)
    breeds = response.json()
    
    weights = []
    
    for breed in breeds:
        weight_metric = breed['weight']['metric']
        weight_range = weight_metric.split(' - ')
        min_weight = float(weight_range[0])
        max_weight = float(weight_range[1])
        weights.append((min_weight + max_weight) / 2)
    
    min_weight = min(weights)
    max_weight = max(weights)
    mean_weight = statistics.mean(weights)
    median_weight = statistics.median(weights)
    std_dev_weight = statistics.stdev(weights)
    
    return {
        'min': min_weight,
        'max': max_weight,
        'mean': mean_weight,
        'median': median_weight,
        'std_dev': std_dev_weight
    }

cats_api = 'https://api.thecatapi.com/v1/breeds'
weight_stats = get_cats_weight_stats(cats_api)
print(weight_stats)


def get_cats_lifespan_stats(cats_api):
    response = requests.get(cats_api)
    breeds = response.json()
    
    lifespans = []
    
    for breed in breeds:
        weight_metric = breed['life_span']
        weight_range = weight_metric.split(' - ')
        min_len = float(weight_range[0])
        max_len = float(weight_range[1])
        lifespans.append((min_len + max_len) / 2)
    
    min_len = min(lifespans)
    max_len = max(lifespans)
    mean_len = statistics.mean(lifespans)
    median_len = statistics.median(lifespans)
    std_dev_len = statistics.stdev(lifespans)
    
    return {
        'min': min_len,
        'max': max_len,
        'mean': mean_len,
        'median': median_len,
        'std_dev': std_dev_len
    }

cats_api = 'https://api.thecatapi.com/v1/breeds'
lifespan_stats = get_cats_lifespan_stats(cats_api)
print(lifespan_stats)



import requests
import pandas as pd
from collections import defaultdict

def get_country_breed_frequency_table(cats_api):
    response = requests.get(cats_api)
    breeds = response.json()
    
    country_breed_count = defaultdict(int)
    
    for breed in breeds:
        country_code = breed.get('country_code', 'Unknown')
        breed_name = breed['name']
        country_breed_count[(country_code, breed_name)] += 1
    
    # Convert to DataFrame for better visualization
    frequency_table = pd.DataFrame(
        country_breed_count.items(), 
        columns=['Country_Breed', 'Frequency']
    )
    frequency_table[['Country', 'Breed']] = pd.DataFrame(frequency_table['Country_Breed'].tolist(), index=frequency_table.index)
    frequency_table = frequency_table.drop(columns=['Country_Breed'])
    
    return frequency_table

cats_api = 'https://api.thecatapi.com/v1/breeds'
frequency_table = get_country_breed_frequency_table(cats_api)

print(frequency_table)

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content of the UCI Machine Learning Repository page
url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find all tables and identify the target table by inspecting its contents
tables = soup.find_all('table', {'cellpadding': '3'})

# Step 4: Ensure we have found the correct table
if not tables:
    print("No tables found")
else:
    table = tables[0]  # Assuming the first table is the correct one

    # Extract the headers
    headers = [header.text.strip() for header in table.find_all('th')]

    # Extract the rows
    rows = table.find_all('tr')[1:]  # Skip the header row

    # Extract the dataset information
    datasets = []
    for row in rows:
        columns = row.find_all('td')
        dataset_info = [column.text.strip() for column in columns]
        datasets.append(dataset_info)

    # Print the headers and the first few datasets as a sample
    print(headers)
    for dataset in datasets[:5]:
        print(dataset)