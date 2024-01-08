# Here I do some haphazard, DiD-inspired stuff to quantify whether the two clusters observed in Conservative plot are significant

# Import relevant libraries
import pandas as pd
import plotly.express as px
import numpy as np
from statsmodels.formula.api import ols

# Get data
df=pd.read_csv('data/combined_data_ii.csv')

# Reduce to just Conservative party
df1=df[df['Party'].isin(['Tory'])]

# Ensure year column is in a format we can maths
df1['Year'] = df1['Year'].astype(int)

# Create a variable that is 1 if the date is after David Cameron becomes PM and 0 otherwise
df1['post']=np.where(df1['Year']>=2010,1,0)

# Apply Ordinary Least Squares to this new, split-up data
did_model = ols('Mean_Centrality ~  Mean_Vote + post', df1).fit()
print(did_model.summary())