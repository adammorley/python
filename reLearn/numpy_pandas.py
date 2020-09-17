#!/usr/bin/python3

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(type(np_height))

bmi = np_weight / np_height ** 2
print(bmi)
print(bmi[bmi>25])

data = {
        "country":['brazil', 'russia', 'india', 'china', 'South Africa'],
        "capital":['brasilia', 'moscow', 'new dehli', 'beijing', 'pretoria'],
        'population':[200, 143, 1252, 1357, 53],
}

import pandas as pd
brics = pd.DataFrame(data)
print(brics)

brics.index=['BR', 'RU', 'IN', 'CN', 'SA']

print(brics)

cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
print(cars[0:2])
