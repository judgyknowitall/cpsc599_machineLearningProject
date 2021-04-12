# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zack

Data Pre-processing v2.0
Used for experimenting
"""
import pandas
import random
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

def preprocess():
    #Sample original dataset for 10% randomly.  
    filename = "../data/Cleaned-Data.csv" 
    n = sum(1 for line in open(filename))-1  # Calculate number of rows in file
    s = 1000  # sample size of 10%
    skip = sorted(random.sample(range(1, n+1), n-s))  # n+1 to compensate for header 
    data = pandas.read_csv(filename, skiprows=skip, sep=';')
    print("Sample size: {}".format(data.shape[0]))
    
    # Preparing columns
    data[['Fever', 'Tiredness','Dry-Cough','Difficulty-in-Breathing',
          'Sore-Throat','None_Sympton','Pains','Nasal-Congestion','Runny-Nose',
          'Diarrhea','None_Experiencing','Age_0-9','Age_10-19','Age_20-24','Age_25-59',
          'Age_60+','Gender_Female','Gender_Male','Gender_Transgender','Severity_Mild',
          'Severity_Moderate','Severity_None','Severity_Severe','Contact_Dont-Know','Contact_No',
          'Contact_Yes','Country']] = data['Fever,Tiredness,Dry-Cough,Difficulty-in-Breathing,Sore-Throat,None_Sympton,Pains,Nasal-Congestion,Runny-Nose,Diarrhea,None_Experiencing,Age_0-9,Age_10-19,Age_20-24,Age_25-59,Age_60+,Gender_Female,Gender_Male,Gender_Transgender,Severity_Mild,Severity_Moderate,Severity_None,Severity_Severe,Contact_Dont-Know,Contact_No,Contact_Yes,Country'].str.split(',', 26, expand=True)
    
    del data['Fever,Tiredness,Dry-Cough,Difficulty-in-Breathing,Sore-Throat,None_Sympton,Pains,Nasal-Congestion,Runny-Nose,Diarrhea,None_Experiencing,Age_0-9,Age_10-19,Age_20-24,Age_25-59,Age_60+,Gender_Female,Gender_Male,Gender_Transgender,Severity_Mild,Severity_Moderate,Severity_None,Severity_Severe,Contact_Dont-Know,Contact_No,Contact_Yes,Country']
    del data['Country']
     
    # Target features
    y = data[['Severity_Mild','Severity_Moderate','Severity_None','Severity_Severe']]
    
    # Input features
    X = data.drop(['Severity_Mild','Severity_Moderate','Severity_None','Severity_Severe'], axis=1)
    
    X, y = make_blobs(n_samples=100, n_features=26, centers=100,
        random_state=0)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2, 
                                                        random_state=123,
                                                        stratify=y)
    return X_train, X_test, y_train, y_test