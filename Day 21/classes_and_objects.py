# Day 6: 30 Days of python programming
from collections import Counter
import math
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
  def __init__(self, data):
    self.data = sorted(data)
  def count(self):
    return len(self.data)
  def sum(self):
    return sum(self.data)
  def min(self):
    return min(self.data)
  def max(self):
    return max(self.data)
  def range(self):
    return self.max() - self.min()
  def mean(self):
    return self.sum() / len(self.data)
  def median(self):
    mid = len(self.data) // 2
    if len(self.data) % 2 == 0:
      return (self.data[mid - 1], self.data[mid + 1])
    else:
      return self.data[mid]
  def mode(self):
    count = Counter(self.data)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]
    return {'mode': modes, 'count': max_count}
  def var(self):
    sum_sqr_diff = 0
    mean = self.mean()
    for num in self.data:
        sum_sqr_diff += (num - mean) **2
    return sum_sqr_diff / len(self.data)
  def std(self):
    return math.sqrt(self.var())
  def freq_dist(self):
    return Counter(self.data)

data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
