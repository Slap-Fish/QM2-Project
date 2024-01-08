# This code compares the voteshare of the major two parties with the voteshare of the Lib Dems

# Import relevant library
import pandas as pd

# Get voting intentions data
datafile = pd.read_csv('data/VotingIntentionsSansMonth.csv')

# There's a random unnamed column the same as the index column that keeps on popping up unnecessarily
# I'll have to keep removing it like this every time it reappears
datafile.drop(['Unnamed: 0'], axis=1, inplace=True)

# Find the difference in voteshare between the main two parties and Lib Dems
datafile['Con_wrt_LD'] = abs(datafile['Con']-datafile['LD'])
datafile['Lab_wrt_LD'] = abs(datafile['Lab']-datafile['LD'])

# Store data in new dataframe
datafile2 = datafile[['Year', 'Con_wrt_LD', 'Lab_wrt_LD']]

# Normalise the differences on a scale of 0-1
# 1 represents absolute similarity (same voteshare as Lib Dems)
# 0 represents absolute difference (100% voteshare against 0% voteshare)
datafile['Normalised_ConLD'] = (100-datafile['Con_wrt_LD'])/100
datafile['Normalised_LabLD'] = (100-datafile['Lab_wrt_LD'])/100

# Store data in new dataframe
datafile3 = datafile[['Year', 'Normalised_ConLD', 'Normalised_LabLD']]

# Save dataframes to csv files
#datafile2.to_csv("data/VotingSimilarityData.csv")
datafile3.to_csv("data/Normalised_VOTING_Similarity.csv")