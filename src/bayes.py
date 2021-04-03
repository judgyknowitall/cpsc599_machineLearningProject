# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra

Create and Train a Naive Multinomial Bayes Model
"""

from sklearn.naive_bayes import MultinomialNB



def train_bayes(X_train, y_train):
    
    print("Training Multinomial Bayes Model ...")
        
    bayes = MultinomialNB()
    bayes.fit(X_train, y_train)
        
    print() # newline    
    return bayes
