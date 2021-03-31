# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra, Abdullah, Zack

Main Function
"""


from preprocess import preprocess
from dnn import train_dnn
from bayes import train_bayes
from logReg import train_logReg
from evaluate import compare_models



def main():
    
    # Data Preprocessing
    data = preprocess()
    
    # Create models
    dnn = train_dnn(data)
    bayes = train_bayes(data)
    logReg = train_logReg(data)
    
    
    # Compare and Evaluate models
    models = [dnn, bayes, logReg]
    best_model = compare_models(models)
    
    
    # Test user's case
    # TODO...
    
  
  
if __name__ == "__main__":
    main()