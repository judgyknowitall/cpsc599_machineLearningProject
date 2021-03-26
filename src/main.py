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
from linReg import train_linReg
from evaluate import compare_models



def main():
    
    # Data Preprocessing
    data = preprocess()
    
    # Create models
    dnn = train_dnn(data)
    bayes = train_bayes(data)
    linReg = train_linReg(data)
    
    
    # Compare and Evaluate models
    models = [dnn, bayes, linReg]
    best_model = compare_models(models)
    
    
    # Test user's case
    # TODO...
    
  
  
if __name__ == "__main__":
    main()