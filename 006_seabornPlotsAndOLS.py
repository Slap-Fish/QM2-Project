# In this code I plot various joinplots
# I also do some Ordinary Least Squares regression

# Import relevant libraries
import seaborn as sns
import pandas as pd
import matplotlib as plt
import os
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col
from statsmodels.formula.api import ols
#from statsmodels.iolib.summary2 import summary_col

# Get data
datafile = pd.read_csv('data/combined_data_ii.csv')

# Create two secondary dataframes by isolating the party
df_tory = datafile[datafile['Party'] == 'Tory']
df_labour = datafile[datafile['Party'] == 'Labour']

# First plot regression line for all data points, ignoring party
plot0 = sns.jointplot(data=datafile, # plot a scatterplot with a regression line and two histograms
                x='Mean_Vote',
                y='Mean_Centrality',
                kind="reg",  # set the kind of plot to be a regression plot
                scatter_kws=dict(alpha=1, color='black'), # set the transparency of the points to be 1
                line_kws=dict(color='gold'), # set the color of the regression line to gold
                height=8) # set the height of the plot to be 8 inches
plot0.fig.suptitle("Relationship Between Mean Vote and Mean Centrality", y=1.02)

# Ensure that the parties are represented by their proper colour
custom_palette = {'Tory': 'blue', 'Labour': 'red'}

# Create a scatterplot of all data points, representing different parties with different colours
plot1 = sns.jointplot(data=datafile, # plot a scatterplot with a regression line and two histograms
                x='Mean_Vote',
                y='Mean_Centrality',
                hue='Party',
                palette=custom_palette, # predefined colours
                height=8) # set the height of the plot to be 8 inches
plot1.fig.suptitle("Scatter Plot of Mean Vote and Mean Centrality by Party", y=1.02)

# Plot regression line for Conservative data points
plot2 = sns.jointplot(data=df_tory, # plot a scatterplot with a regression line and two histograms
                x='Mean_Vote',
                y='Mean_Centrality',
                kind="reg",  # set the kind of plot to be a regression plot
                scatter_kws=dict(alpha=1, color='black'), # set the transparency of the points to be 1
                line_kws=dict(color='blue'), # set the color of the regression line to blue
                height=8) # set the height of the plot to be 8 inches
plot2.fig.suptitle("Relationship Between Mean Vote and Mean Centrality (Conservatives)", y=1.02)

# Plot regression line for Labour data points
plot3 = sns.jointplot(data=df_labour, # plot a scatterplot with a regression line and two histograms
                x='Mean_Vote',
                y='Mean_Centrality',
                kind="reg",  # set the kind of plot to be a regression plot
                scatter_kws=dict(alpha=1, color='black'), # set the transparency of the points to be 1
                line_kws=dict(color='red'), # set the color of the regression line to red
                height=8) # set the height of the plot to be 8 inches
plot3.fig.suptitle("Relationship Between Mean Vote and Mean Centrality (Labour)", y=1.02)

# Do an ols model for:
# Just Conservative data points
model1= ols('Mean_Centrality ~  Mean_Vote', data=df_tory).fit() # fit the model
print(model1.summary()) # print the summary
# Just Labour data points
model2= ols('Mean_Centrality ~  Mean_Vote', data=df_labour).fit() # fit the model
print(model2.summary()) # print the summary
# All data points
model= ols('Mean_Centrality ~  Mean_Vote', data=datafile).fit() # fit the model
print(model.summary()) # print the summary