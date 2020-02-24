# -*- coding: utf-8 -*-
"""
Temporary demo of trial loop
"""

from psychopy import data

#get trials from a file
trial_list = data.importConditions('wordlist.csv')


# create a 'TrialHandler'.
trials = data.TrialHandler(trial_list,2, method = 'fullRandom')


for trial in trials:
    print(trial['word'])
    
