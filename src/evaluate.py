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
    https://stackoverflow.com/questions/54589669/confusion-matrix-error-classification-metrics-cant-handle-a-mix-of-multilabel
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import f1_score, accuracy_score


# Calculate accuracies
def compare_models(models, X_test, y_test):
    
    print("Calculating Model accuracies...")
    
    best_model_index = -1
    best_score = 0
    
    # Iterate over models
    for i in range(len(models)):
        
        # No model should be null
        if (models[i] == None):
            continue
    
        # Calculate prediction and make sure labels are single-digit instead of oneHot encoded
        y_pred = models[i].predict(X_test)
        if (i == 0):
            y_pred = np.argmax(y_pred, axis=1)
    
        # Calculate accuracy
        score = accuracy_score(y_test, y_pred)
        
        # Update best model
        if score > best_score:
            best_score = score
            best_model_index = i
            
            
        # Extra Evaluations
        
        # F1 score
        f1 = 0
        f1 = f1_score(y_test, y_pred, average='macro') 
        
        
        # Print results
        print("Model", i)
        print("\tAccuracy =  {:.3f}".format(score))
        print("\tF1 scores = {:.3f}".format(f1))
        plot_conf_matrix(y_test, y_pred, "Model " + str(i))
        print() # newline

    
    print() # newline
    return best_model_index, best_score



# Plot confusion matrix
def plot_conf_matrix(y_test, y_pred, model_name):
    
    # Calculate matrix
    cm = confusion_matrix(y_test, y_pred, labels=[0,1,2,3])
    
    # Plot
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    disp.ax_.set_title(model_name + " Confusion Matrix")
    
    plt.show()