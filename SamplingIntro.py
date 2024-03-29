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

#Using Histagram to find out generalization
spotify_population['acousticness'].hist(bins=np.arange(0,1.01,0.01))
plt.title('Data distribution for acousticness rating')
plt.show()

#Can we generalize findings
spotify_population['duration_minutes'].hist(bins=np.arange(0,15.5,0.5))
plt.title('Data distribution for song duration in minutes')
plt.show()

#Generating Randon Numbers using Uniform and Normal distribution
uniforms = np.random.uniform(low=-3, high=3, size=5000)
print(uniforms)

normals = np.random.normal(loc=5, scale=2, size=5000)
print(normals)

#Plot a Histogram for Uniform and Normal Distribution values
plt.hist(uniforms,bins=np.arange(-3,3.5, 0.5))
plt.title('Histogram showing distribution of Uniform Values')
plt.show()

plt.hist(normals,bins=np.arange(-2,13.5, 0.5))
plt.title('Histogram showing distribution of Normal Values')
plt.show()