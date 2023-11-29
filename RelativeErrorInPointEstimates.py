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