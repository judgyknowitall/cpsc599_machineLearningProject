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

def train_dnn(X_train, y_train):

    print("Training Deep Neural Network ...")
    
    #One-hot encode labels
    y_train = to_categorical(y_train, num_classes=2)
    #y_test = to_categorical(y_test, num_classes=2)
    
    # print("X_train shape: {}, y_train shape: {}".format(X_train.shape, y_train.shape))
    # print("X_test shape: {}, y_test shape: {}".format(X_test.shape, y_test.shape))
    
    #Create model
    model = Sequential()
    model.add(Dense(12, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=20, verbose=1)
    print(model.summary())
    print() # newline
    return model
