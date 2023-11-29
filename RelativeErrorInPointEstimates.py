import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow
import random

#Load the attrition .feather file dataset
attrition_pop = pd.read_feather('/Users/mac/Downloads/attrition.feather')
print(attrition_pop.head())
print(attrition_pop.columns)

#Calculation relative error
mean_attrition_pop = attrition_pop['Attrition'].mean()

attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()
rel_error_pct50 = 100 * abs(mean_attrition_pop - mean_attrition_srs50)/mean_attrition_pop
print(rel_error_pct50)

attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()
rel_error_pct100 = 100 * abs(mean_attrition_pop - mean_attrition_srs100)/mean_attrition_pop
print(rel_error_pct100)

#Replicating Samples
mean_attritions = []

for i in range(500):
    mean_attritions.append(attrition_pop.sample(n=60)['Attrition'].mean())

# plt.hist(mean_attritions, bins=16)
# plt.title('Sample Distribution for Attrition')
# plt.show()

# Exact sampling distribution
#Define the expand grid function.
# Expand a grid representing 5 8-sided dice
dice = expand_grid({
    'die1':[1,2,3,4,5,6,7,8],
    'die2':[1,2,3,4,5,6,7,8],
    'die3':[1,2,3,4,5,6,7,8],
    'die4':[1,2,3,4,5,6,7,8],
    'die5':[1,2,3,4,5,6,7,8]
    })
dice['mean_roll'] = (dice['die1'] + dice['die2'] + dice['die3'] +
                     dice['die4'] + dice['die5'])/5
dice['mean_roll'] = dice['mean_roll'].astype('category')
dice['mean_roll'].value_counts(sort=False).plot(kind='bar')
plt.show()