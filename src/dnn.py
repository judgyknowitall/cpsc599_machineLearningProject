# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zack
"""
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import glob
from numpy import asarray
import pandas


def read_data():
    #Read the data in and perform the split
    filename = '../data/Experimental-Data.csv'
    data = pandas.read_csv(filename)
    print(data.shape[0])

    
    X_train, X_test, y_train, y_test = train_test_split(data.drop('Severity', axis=1), data.Severity, train_size=0.9, test_size=0.1)
    return X_train, X_test, y_train, y_test

def train_dnn():
    
    X_train, X_test, y_train, y_test = read_data()
    print("Training Deep Neural Network ...")
    
    #One-hot encode labels
    y_train = to_categorical(y_train, 4)
    y_test = to_categorical(y_test, 4)
    
    #Create model
    model = Sequential()
    model.add(Dense(len(list(X_train)), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    results = model.fit(X_train, y_train, epochs=2, verbose=0)
    print(model.summary())
    
    # Evaluate on test set
    _, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print("\nAccuracy on test set: {:.3f}".format(accuracy))

    print() # newline
    return

train_dnn()