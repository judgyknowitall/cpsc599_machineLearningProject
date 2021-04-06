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
    y_train = to_categorical(y_train, 4)
    
    #Create model
    model = Sequential()
    model.add(Dense(len(list(X_train)), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=2, verbose=0)
    print(model.summary())


    print() # newline
    return model
