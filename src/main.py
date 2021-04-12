# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7
@author: Zahra, Abdullah, Zack
Main Function
"""
# External modules
import pandas
from tkinter import Tk
from sklearn.model_selection import train_test_split

# Local modules
from preprocess import preprocess
from dnn import train_dnn
from bayes import train_bayes
from logReg import train_logReg
from evaluate import compare_models
from gui import App


# Read CSV files and extract features and labels
def read_processed_data():

    # Preprocess data and save as a csv file
    preprocess()
    
    # Read and split processed data properly
    processed_data = pandas.read_csv('../data/Processed-Data.csv')
    
    y = processed_data.Severity
    x = processed_data.drop("Severity", axis=1)

    return x, y


# Main function
def main():

    x, y = read_processed_data()
    X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, train_size=0.7, shuffle=True)
    

    # Create models
    dnn = train_dnn(X_train, y_train)
    bayes = train_bayes(X_train, y_train)
    logReg = train_logReg(X_train, y_train)

    # Compare and Evaluate models
    models = [dnn, bayes, logReg]
    best_model_index, best_score = compare_models(models, X_test, y_test)

    if (best_model_index == 0):
        print("The Best model was: DNN")
    elif (best_model_index == 1):
        print("The Best model was: Bayes")
    elif (best_model_index == 2):
        print("The Best model was: Regression")
    
    print("The Highest score was: {:.3f}".format(best_score))

    # Start GUI. User input is taken and predicition is made
    print("Starting GUI...")
    root = Tk()
    App(root, models[best_model_index])
    root.mainloop()
    print("GUI Closed...")
  
    
if __name__ == "__main__":
    main()