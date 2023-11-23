import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow

#Load the attrition .feather file dataset
attrition_pop = pd.read_feather('/Users/mac/Downloads/attrition.feather')
print(attrition_pop.head())
print(attrition_pop.columns)

#Create a simple random sample and set seed
attrition_samp = attrition_pop.sample(n=70, random_state=18900217)
print(attrition_samp)

#Create a systemic sample
sample_size = 70
pop_size = len(attrition_pop)
interval = pop_size//sample_size

attrition_sys_samp =  attrition_pop.iloc[::interval]
print(attrition_sys_samp)

#Plot a systematic sample to see if it is Ok
attrition_pop_id = attrition_pop.reset_index()

#attrition_pop_id.plot(x='index', y='YearsAtCompany', kind='scatter')
#plt.title('YearsAtCompany Vs Index')
#plt.show()

attrition_shuffled = attrition_pop.sample(frac=1)

attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()
#attrition_shuffled.plot(x='index', y='YearsAtCompany', kind='scatter')
#plt.title('YearsAtCompany Vs Index for Randomised systematic sample')
#plt.show()

#Proportional Stratified Sampling
#Proportion of employees by Education Level
education_count_pop = attrition_pop['Education'].value_counts(normalize=True)
print(education_count_pop)

attrition_strat = attrition_pop.groupby('Education').sample(frac=0.4, random_state=2022)

education_count_strat  = attrition_strat['Education'].value_counts(normalize=True)
print(education_count_strat)

#Equal sample of 30
attrition_eq = attrition_pop.groupby('Education').sample(n=30, random_state=2022)
education_count_eq = attrition_eq['Education'].value_counts(normalize=True)
print(education_count_eq)

#Weighted Samples
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0,41,1))
plt.title('Years At Company distribution on general population')
plt.show()

attrition_weight = attrition_pop.sample(n=300, weights='YearsAtCompany')

attrition_weight['YearsAtCompany'].hist(bins=np.arange(0,41,1))
plt.title('Years At Company distribution on wieghted sample')
plt.show()
