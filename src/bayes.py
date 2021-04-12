# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra

Create and Train a Naive Multinomial Bayes Model
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score


def train_bayes(X_train, y_train):
    
    print("Training Multinomial Bayes Model...")
    
    # Use K-Fold Cross Validation to pick best alpha smoothing value
    folds = 5
    
    best_alpha = 0
    best_score = 0
    
    for alpha in [x/10.0 for x in range(11)]:

        model = MultinomialNB(alpha=alpha)
        score = cross_val_score(model, X_train, y_train, scoring='accuracy', cv=folds, n_jobs=-1).mean()
        
        if (score > best_score):
            best_score = score
            best_alpha = alpha
        

    # Evaluate the model and collect the scores
    print('Best Accuracy achieved with alpha %.1f: %.3f' % (best_alpha, best_score))
    
    bayes = MultinomialNB(alpha=best_alpha)
    bayes.fit(X_train, y_train)
        
    print() # newline    
    return bayes
