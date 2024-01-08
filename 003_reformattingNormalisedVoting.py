# Here I try to format my data in a way which is easier to compare with Ana's

# Import relevant library
import pandas as pd
import os

# Get data
datafile = pd.read_csv('data/Normalised_VOTING_Similarity.csv')

# Create columns for the relevant summary statistics
# These will be used to plot our data points and create error bars
datafile['LabMean'] = datafile.groupby(['Year'])['Normalised_LabLD'].transform('mean')
datafile['LabSTD'] = datafile.groupby(['Year'])['Normalised_LabLD'].transform('std')
datafile['ConMean'] = datafile.groupby(['Year'])['Normalised_ConLD'].transform('mean')
datafile['ConSTD'] = datafile.groupby(['Year'])['Normalised_ConLD'].transform('std')

# Create two new dataframes, blank save for the year column
df3, df4 = pd.DataFrame(), pd.DataFrame()
df3['Year'], df4['Year'] = [2005 + i for i in range(15)], [2005 + i for i in range(15)]

# Here I store the summary statistics of both parties as individual columns in separately in the two new dataframes
for i in range(15):
    # Isolate one year of data at a time
    dfi = datafile.loc[datafile['Year'] == 2005  + i]
    # Ensure index of isolated dfi starts from zero
    dfi.reset_index(inplace=True)
    # Get mean, stdev and n for tory party
    mean_value = dfi.loc[0, 'ConMean']
    std_value = dfi.loc[0, 'ConSTD']
    n_value = dfi.shape[0]
    # Store in dataframe df3
    df3.at[i, 'Mean_Vote'] = mean_value
    df3.at[i, 'STD_Vote'] = std_value
    df3.at[i, 'N_Vote'] = n_value
    # Repeat for labour party and store in df4
    mean_value = dfi.loc[0, 'LabMean']
    std_value = dfi.loc[0, 'LabSTD']
    df4.at[i, 'Mean_Vote'] = mean_value
    df4.at[i, 'STD_Vote'] = std_value
    df4.at[i, 'N_Vote'] = n_value

# Add a column indicating the party
df3['Party'], df4['Party'] = 'Tory', 'Labour'

# Join the dataframes together to get one with summary statistics and party
df = pd.concat([df3,df4])

# Reset index
df.reset_index(drop=True, inplace=True)

# Save as new csv file
df.to_csv("data/SingleColumn_VotingData.csv")