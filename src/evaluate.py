# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra

Model Evaluation
Calculates the accuracy, Confusion matrix, as well as the f1-score of each model
Returns the model with the highest accuracy.

- F1-score: Calculates metrics for each label, and finds their unweighted mean. This does not take label imbalance into account.

References:
    https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
"""

import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import f1_score

# Calculate accuracies
def compare_models(models, X_test, y_test):
    
    print("Calculating Model accuracies...")
    
    best_model_index = -1
    best_score = 0
    
    for i in range(len(models)):
        
        #TODO: temporary, delete later
        if (models[i] == None):
            continue
    
        
        # Calculate accuracy
        score = models[i].score(X_test, y_test)
        
        # Update best model
        if score > best_score:
            best_score = score
            best_model_index = i
            
            
        # Extra Evaluations
        plot_conf_matrix(models[i], X_test, y_test)
        f1 = f1_score(y_test, models[i].predict(X_test), average='macro') 
        
        # Print results
        print("Model", i)
        print("\tAccuracy =  {:.3f}".format(score))
        print("\tF1 scores = {:.3f}\n".format(f1))


    
    print() # newline
    return best_model_index, best_score



# Plot confusion matrix
def plot_conf_matrix(model, X_test, y_test):
    
    disp = plot_confusion_matrix(model, X_test, y_test,cmap=plt.cm.Blues)
    disp.ax_.set_title("Confusion matrix")
    
    plt.show()