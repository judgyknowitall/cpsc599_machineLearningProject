# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zahra, Abdullah, Zack

Main Function
"""

# External modules
import pandas
from os import path
from sklearn.model_selection import train_test_split


# Local modules
from preprocess import preprocess
from dnn import train_dnn
from bayes import train_bayes
from logReg import train_logReg
from evaluate import compare_models



def read_processed_data():
    
    # Preprocess data if not done so already
    if (not path.exists('../data/Processed-Data.csv')):
        print("Preprocessing Data...\n")
        #preprocess() #TODO
    
    # Read and split processed data properly
    processed_dat = pandas.read_csv('../data/Processed-Data.csv')
    y = processed_dat.Severity
    x = processed_dat.drop('Severity', axis='columns')
    
    # Return tuple (X_train, X_test, y_train, y_test)
    X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, train_size=0.7, test_size=0.3, shuffle=True)

    
    return (X_train, y_train), (X_test, y_test)


def main():

    # train_data = (X_train, y_train), test_data = (X_test, y_test)
    train_data, test_data = read_processed_data()
    
    # Create models
    dnn = train_dnn(*train_data)
    bayes = train_bayes(*train_data)
    logReg = train_logReg(*train_data)
    
    
    # Compare and Evaluate models
    models = [dnn, bayes, logReg]
    best_model_index, _ = compare_models(models, *test_data)
    
    if (best_model_index == 0):
        print("The Best model was: DNN")
    elif (best_model_index == 1):
        print("The Best model was: Bayes")
    elif (best_model_index == 2):
        print("The Best model was: Regressin")
    
    
    # Test user's case
    # TODO...
    
  
  
if __name__ == "__main__":
    main()