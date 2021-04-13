# -*- coding: utf-8 -*-
"""
CPSC 599 - Machine Learning Project
Team 7

@author: Zack
Deep Neural Network 
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


def train_dnn(X_train, y_train):

    print("Training Deep Neural Network...")
    
    # One-hot encode labels
    y_train = to_categorical(y_train, 4)
    
    # Create model
    model = Sequential()
    model.add(Dense(len(list(X_train)), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=20, verbose=1)

    print(model.summary())


    print() # newline
    return model
