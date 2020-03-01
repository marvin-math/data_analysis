# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:40:23 2020

@author: marvi
"""
import pandas
import os
import statistics
import numpy
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression


# summary statistics
#%%
filepath = os.path.join('bugs.csv')
df = pandas.read_csv(filepath)
summary_df = {'KillRating': [statistics.mean, statistics.median, min, max, statistics.stdev]}
grouped_df = df.groupby(['Disgust', 'Fear']).aggregate(summary_df)
grouped_df_trial = df.groupby(['Disgust', 'Fear'])
print(grouped_df)



# ///// separation of the data set into different compartments /////
#%% the different compartments reflect the four different categories of bugs

category_low_low = df.loc[(df['Disgust'] == 'low') & (df['Fear'] == 'low')]
#print(category_low_low)

category_low_high = df.loc[(df['Disgust'] == 'low') & (df['Fear'] == 'high')]
#print(category_low_high)

category_high_low = df.loc[(df['Disgust'] == 'high') & (df['Fear'] == 'low')]
#print(category_high_low)

category_high_high = df.loc[(df['Disgust'] == 'high') & (df['Fear'] == 'high')]
#print(category_high_high)


# linear regression
#%%
formula_kill = "KillRating ~ C(Disgust) + C(Fear)"
m_kill = smf.ols(formula_kill, data = df).fit()
print(m_kill.summary())
#linear model: KillRating = 7.95 - 0.75 * Disgust - 1.43 * Fear (where Disgust
# and Fear take the value 1 if low and 0 if high)
# results: 
# low, low: 7.95 - 0.75 - 1.43 = 5.77
# low, high: 7.95 - 0.75 = 7.2
# high, low: 7.95 - 1.43 = 6.52
# high, high: 7.95 - 0 = 7.95
# question: what does he exactly mean with 'the results of a linear model'?