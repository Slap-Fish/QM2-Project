# Putting Ana's data into a format that's easier for ME to use

# Import relevant library
import pandas as pd

# Get the data
dataf = pd.read_csv('data/Normalised_CENTRALITY_Similarity.csv')

# Reduce down to just the data we're interested in
dataf = dataf[['Year', 'Party', 'Normalized_Similarity']]

# Create two new dataframes of just one party each
labour = dataf[dataf['Party'] == 'Labour']
tory = dataf[dataf['Party'] == 'Conservative']

# Get summary stats
labour['mean'] = labour.groupby(['Year'])['Normalized_Similarity'].transform('mean')
labour['std'] = labour.groupby(['Year'])['Normalized_Similarity'].transform('std')
tory['mean'] = tory.groupby(['Year'])['Normalized_Similarity'].transform('mean')
tory['std'] = tory.groupby(['Year'])['Normalized_Similarity'].transform('std')

# Undo the mess created in the index due to splitting up the 'dataf' dataframe
labour.reset_index(drop=True, inplace=True)
tory.reset_index(drop=True, inplace=True)

# Create new dataframes with one row for each of the allotted years
df1, df2 = pd.DataFrame(), pd.DataFrame()
df1['Year'], df2['Year'] = [2005 + i for i in range(15)], [2005 + i for i in range(15)]

# Store summary stats as columns in one dataframe per party
for i in range(15):
    # Isolate one year of data at a time from tory dataframe
    dfi = tory.loc[tory['Year'] == 2005  + i]
    # Ensure index starts from zero
    dfi.reset_index(inplace=True)
    # Get mean, stdev and n
    mean_value = dfi.loc[0, 'mean']
    std_value = dfi.loc[0, 'std']
    n_value = dfi.shape[0]
    # Store in dataframe df1
    df1.at[i, 'Mean_Centrality'] = mean_value
    df1.at[i, 'STD_Centrality'] = std_value
    df1.at[i, 'N_Centrality'] = n_value
    
    # Repeat for labour party
    dfi = labour.loc[labour['Year'] == 2005  + i]
    dfi.reset_index(inplace=True)
    mean_value = dfi.loc[0, 'mean']
    std_value = dfi.loc[0, 'std']
    n_value = dfi.shape[0]
    # Store in dataframe df2
    df2.at[i, 'Mean_Centrality'] = mean_value
    df2.at[i, 'STD_Centrality'] = std_value
    df2.at[i, 'N_Centrality'] = n_value

# Create a column indicating party
df1['Party'], df2['Party'] = 'Tory', 'Labour'

# Join dataframes together
df = pd.concat([df1,df2])

# Reset the index
df.reset_index(drop=True, inplace=True)

# Save new dataframe as csv file
df.to_csv("data/SingleColumn_CentralityData.csv")