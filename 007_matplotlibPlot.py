# Here I create a simple scatter plot with error bars to see if data looks reasonable

# Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# Get data
datafile = pd.read_csv('data/combined_data_ii.csv')

# Ensure columns are such that we can maths them
datafile['STD_Vote'] = datafile['STD_Vote'].astype(float)
datafile['N_Vote'] = datafile['N_Vote'].astype(float)
datafile['STD_Centrality'] = datafile['STD_Centrality'].astype(float)
datafile['N_Centrality'] = datafile['N_Centrality'].astype(float)

# Calculate the error in both axes for each data point and store in new columns
for i in range(30):
    datafile.loc[i, 'Error_Vote'] = (2*datafile.loc[i, 'STD_Vote']/sqrt(datafile.loc[i, 'N_Vote']))
    datafile.loc[i, 'Error_Centrality'] = (2*datafile.loc[i, 'STD_Centrality']/sqrt(datafile.loc[i, 'N_Centrality']))

# Assign variables to the axes and error bars
x = datafile['Mean_Vote']
y = datafile['Mean_Centrality']
x_err = datafile['Error_Vote']
y_err = datafile['Error_Centrality']

# Plot a scatter plot with error bars
plt.scatter(x, y)
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='none', color='gray', capsize=5)

# Label and display
plt.xlabel('Voteshare')
plt.ylabel('Centrality')
plt.title('Scatter Plot of Political Centrality of Labour and Tories 2005-2019')
plt.show()
