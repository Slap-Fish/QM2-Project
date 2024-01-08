# Here I put the reformatted voting and speeches data into one dataset I can later manipulate

# Import relevant library
import pandas as pd

# Get data
dataf = pd.read_csv('data/SingleColumn_CentralityData.csv')
datafile = pd.read_csv('data/SingleColumn_VotingData.csv')

# Merge polling data and centrality data by index columns
df_joined = datafile.merge(dataf, left_index=True, right_index=True)

# Remove superfluous and repeated columns
df_joined.drop(['Unnamed: 0_x', 'Party_x', 'Unnamed: 0_y', 'Year_y'], axis=1, inplace=True)

# Simplify some column names
df_joined.rename(columns={'Year_x': 'Year', 'Party_y': 'Party'}, inplace=True)

# Save as csv file
df_joined.to_csv("data/combined_data_ii.csv")