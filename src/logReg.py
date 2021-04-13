# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Abdullah

Logistic Regression model

References:
    https://machinelearningmastery.com/multinomial-logistic-regression-with-python/
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def train_logReg(X_train, y_train):
    
    print("Training Logistic Regression Model ...")
    
    
    # Use K-Fold Cross Validation to pick best solver function
    folds = 5
    
    best_solver = 'lbfgs'
    best_score = 0
    
    # For multiclass problems, can only use ‘newton-cg’, ‘sag’, ‘saga’ and ‘lbfgs’
    for solver in ['newton-cg', 'sag', 'saga', 'lbfgs']:

        model = LogisticRegression(multi_class='multinomial', solver=solver)
        score = cross_val_score(model, X_train, y_train, scoring='accuracy', cv=folds, n_jobs=-1).mean()
        
        if (score > best_score):
            best_score = score
            best_solver = solver
        

    # Evaluate the model and collect the scores
    print('Best Accuracy achieved with solver "' + best_solver + '": %.3f' % (best_score))
    
    logReg = LogisticRegression(multi_class='multinomial', solver=best_solver)
    logReg.fit(X_train, y_train)
    
    print() # newline
    return logReg