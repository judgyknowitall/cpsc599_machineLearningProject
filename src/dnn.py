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
    filename = '../data/Small-Data.csv'
    data = pandas.read_csv(filename, index_col=False)
    

    y = data.Severity
    #x = data.drop("Severity", axis=1)
    x = data.Fever
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3)
    return X_train, X_test, y_train, y_test


def train_dnn():
    
    X_train, X_test, y_train, y_test = read_data()
    print("Training Deep Neural Network ...")
    
    #One-hot encode labels
    y_train = to_categorical(y_train, num_classes=2)
    y_test = to_categorical(y_test, num_classes=2)
    
    print("X_train shape: {}, y_train shape: {}".format(X_train.shape, y_train.shape))
    print("X_test shape: {}, y_test shape: {}".format(X_test.shape, y_test.shape))
    
    #Create model
    model = Sequential()
    model.add(Dense(12, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    results = model.fit(X_train, y_train, epochs=10, verbose=1)
    #print(model.summary())
    
    # Evaluate on test set
    _, accuracy = model.evaluate(X_test, y_test, verbose=1)
    print("\nAccuracy on test set: {:.3f}".format(accuracy))
    
    predict = model.predict(X_test)
    print(predict)

    print() # newline
    return

train_dnn()