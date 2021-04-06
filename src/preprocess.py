# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zack

Data Pre-processing

The data is read in as a Pandas Dataframe object and output as a csv file found
in the /data/ folder as Processed-Data.csv.

To use the dataset in your model, read in using pandas as in this file.

References:
    https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o
    https://www.codementor.io/@guidotournois/4-strategies-to-deal-with-large-datasets-using-pandas-qdw3an95k
"""
import pandas
import random

def label_severity(row):
    if row['Severity_None'] == 1:
        return 0
    if row['Severity_Mild'] == 1:
        return 1
    if row['Severity_Moderate'] == 1:
        return 2
    if row['Severity_Severe'] == 1:
        return 3
    
def label_age(row):
    if row['Age_0-9'] == 1:
        return 0
    if row['Age_10-19'] == 1:
        return 1
    if row['Age_20-24'] == 1:
        return 2
    if row['Age_25-59'] == 1:
        return 3
    if row['Age_60+'] == 1:
        return 4
    
def label_gender(row):
    if row['Gender_Transgender'] == 1:
        return 0
    if row['Gender_Female'] == 1:
        return 1
    if row['Gender_Male'] == 1:
        return 2
    
def label_contact(row):
    if row['Contact_No'] == 1:
        return 0
    if row['Contact_Yes'] == 1:
        return 1
    if row['Contact_Dont-Know'] == 1:
        return 2

def preprocess():
    #Sample original dataset for 10% randomly.  
    filename = "../data/Cleaned-Data.csv" 
    n = sum(1 for line in open(filename))-1  # Calculate number of rows in file
    s = n//3  # sample size of 10%
    skip = sorted(random.sample(range(1, n+1), n-s))  # n+1 to compensate for header 
    df = pandas.read_csv(filename, skiprows=skip)
    print("Sample size: {}".format(df.shape[0]))

    #Insert Severity column and populate
    ##Mapping: 0='Severity_None', 1='Severity_Mild', 2='Severity_Moderate', 3='Severity_Severe'
    df['Severity'] = df.apply (lambda row: label_severity(row), axis=1)
    
    #Insert Age-Bracket column and populate
    ##Mapping: 0='Age_0-9', 1='Age_10-19', 2='Age_20-24', 3='Age_25-59', 4='Age_60+'
    df['Age_Bracket'] = df.apply (lambda row: label_age(row), axis=1)
    
    #Insert Gender column and populate
    ##Mapping: 0='Gender_Transgender', 1='Gender_Male', 2='Gender_Female'
    df['Gender'] = df.apply (lambda row: label_gender(row), axis=1)
    
    #Insert Contact column and populate
    #Mapping: 0='Contact_No', 1='Contact_Yes', 2='Contact_Dont-Know'
    df['Contact'] = df.apply (lambda row: label_contact(row), axis=1)
    
    #Remove columns: Country(Not applicable), None_Experiencing(Redundant), Rest(Compressed)
    df = df.drop(columns = ['None_Sympton','Country', 'None_Experiencing', 'Age_0-9', 'Age_10-19', 'Age_20-24'
                            , 'Age_25-59', 'Age_60+', 'Gender_Female', 'Gender_Male', 'Gender_Transgender'
                            , 'Severity_Mild', 'Severity_Moderate', 'Severity_None', 'Severity_Severe'
                            , 'Contact_Dont-Know', 'Contact_No', 'Contact_Yes'])
    
    #Generate report on final processed dataset
    print(list(df))
    print(df['Severity'].value_counts())
    print(df['Age_Bracket'].value_counts())
    print(df['Gender'].value_counts())
    print(df['Contact'].value_counts())
    print() # newline
    
    #Save dataframe to csv
    df.to_csv('../data/Experimental-Data.csv', index=False)
    
preprocess()

