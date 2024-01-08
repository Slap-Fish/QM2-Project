# The function of this code is to put all of the pages of voting intention data into one dataframe
# I also clean it somewhat, in praparation for later manipulation

# Import relevant library
import pandas as pd
import os

# Make a directory called 'data' to store everything in, if there isn't one already
directory = 'data'
os.makedirs(directory, exist_ok=True)

# These are the various pages of data I'm conflating
df1 = pd.read_csv('data/main-party-pollbase-2001-2005.csv')
df2 = pd.read_csv('data/main-party-pollbase-2005-2010.csv')
df3 = pd.read_csv('data/main-party-pollbase-2010-2015.csv')
df4 = pd.read_csv('data/main-party-pollbase-2015-2017.csv')
df5 = pd.read_csv('data/main-party-pollbase-2017-2019.csv')
df6 = pd.read_csv('data/main-party-pollbase-2019-2023.csv')
datafile = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True, axis=0)

# Get rid of entries I don't care about
datafile = datafile.dropna()
datafile = datafile[(datafile['Year'] > 2004) & (datafile['Year'] < 2020)]

# The 'Conservative' column was being a bit funny so I converted the entries to floats
# Not a perfect fix but does the job
datafile['Con'] = datafile['Con'].astype(float)

# Because Ana ignores the month column I'm also going to make a version which doesn't have months
# But I do think it's useful data so I'll keep both versions
# NOTE TO SELF: try and get Ana's data by month as well at some point
datafile2 = datafile.drop(columns=['Month'])

# After this rejigging it's important to make sure the index is still accurate
datafile2.reset_index(drop=True, inplace=True)

# Save datafile to a new csv file so I don't have to keep redoing this process at the start of every program
#datafile.to_csv("data/VotingIntentionsFullData.csv")
datafile2.to_csv("data/VotingIntentionsSansMonth.csv")