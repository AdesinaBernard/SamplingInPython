import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow

#Load the Spotify .feather file dataset
spotify_population = pd.read_feather('/Users/mac/Downloads/spotify_2000_2020.feather')
print(spotify_population.head())
print(spotify_population.columns)
#print(spotify_population.info())
#spotify_population['release_date'] = spotify_population[spotify_population['release_date'].astype(datetime)]

#Creating samples and using Numpy
#Create a panda Series for the loudness population
loudness_pop = spotify_population['loudness']

#Create a sample from loudness population
loudness_samp = loudness_pop.sample(n=100)

#Calculate mean of loudness population and loudness sample
mean_loudness_pop = loudness_pop.mean()
mean_loudness_samp = loudness_samp.mean()

print(mean_loudness_pop, mean_loudness_samp)
