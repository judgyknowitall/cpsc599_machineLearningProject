# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra

Data Pre-processing
"""

def compare_models(models, X_test, y_test):
    
    print("Printing Model accuracies:")
    
    best_model_index = -1
    best_score = 0
    
    for i in range(len(models)):
        
        # temporary #TODO delete later
        if (models[i] == None):
            continue
        
        score = models[i].score(X_test, y_test)
        print("Model", i, ":     {:.3f}".format(models[i].score(X_test, y_test)))
        
        if score > best_score:
            best_score = score
            best_model_index = i
    
    print() # newline
    return best_model_index, best_score