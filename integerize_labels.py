# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:06:59 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
integerize_labels

In this set of code, I changed my flower names from strings to numerical
values corresponding to 0 for Iris-setosa, 1 for Iris-versicolor, and 2 for 
Iris-virginica. I did this by making a for loop that iterated through each 
fourth index of every sublist in data and changing them to numerical values in
integerized_data (a copy of data). It then adds these values to a dictionary
in which the key is the string flower name and the value is its corresponding
integer value. 
--------------------------
'''
import create_data

def integerize_labels(data):
    integerized_data = data[:] #makes exact copy of data
    label_dict = {}

    for i in range(len(data)):
        if data[i][4] == "Iris-setosa":
            integerized_data[i][4] = 0 #replace "Iris-setosa" with 1
            label_dict["Iris-setosa"] = 0
        elif data[i][4] == "Iris-versicolor":
            integerized_data[i][4] = 1 #replace "Iris-versicolor" with 2
            label_dict["Iris-versicolor"] = 1
        elif data[i][4] == "Iris-virginica":
            integerized_data[i][4] = 2 #replace "Iris-virginica" with 3
            label_dict["Iris-virginica"] = 2
    
    return (integerized_data, label_dict)

data = create_data.create_data("iris.data.txt")
integerize_labels(data)

