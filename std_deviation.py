#!/bin/python3.8
import math
import csv
import statistics

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]
formattedData = []
for i in data:
    formattedData.append(int(i))
print(formattedData)

deviatedData = statistics.stdev(formattedData)
print(deviatedData)
