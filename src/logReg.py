# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Abdullah

Logistic Regression model
"""

import pandas as pd
from numpy import mean
from numpy import std
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold

def train_logReg(X_train, y_train):
    
    print("Training Logistic Regression Model ...")
    # For multiclass problems, can only use ‘newton-cg’, ‘sag’, ‘saga’ and ‘lbfgs’
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    
    # Separate labels from data
    '''labels = data["Severity"]
    data.drop("Severity", axis=1, inplace=True)
    data.drop("Contact", axis=1, inplace=True)
    
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, stratify=labels, test_size=0.3)'''

    # Training set summary
    # print(X_train.shape, y_train.shape)
    # print(Counter(y_train))
    
    # Define the model evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    # Evaluate the model and collect the scores
    n_scores = cross_val_score(
        model, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1)
    
    print('Mean Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

    
    model.fit(X_train, y_train)
    
    print() # newline
    return model


'''
Driver function

def main():
    data = pd.read_csv("../data/Processed-Data.csv")
    train_logReg(data)

if __name__ == "__main__":
    main()
    '''