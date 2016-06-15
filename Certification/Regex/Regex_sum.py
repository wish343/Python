__author__ = 'wIsh'

import re

file1 = open('regex_sum_1.txt')
sum1 = sum([int(x) for x in re.findall('[0-9]+', file1.read())])

file2 = open('regex_sum_2.txt')
sum2 = sum([int(x) for x in re.findall('[0-9]+', file2.read())])


print(sum1)
print(sum2)