# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:07:22 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
knn

In this code, I created a one-dimensional list that corresponds to all the KNN
for every row in test_data. I did this by creating a loop that iterated through 
every row in test_data and found the k nearest neighbor of each one and 
predicted what the label would be. 
--------------------------
'''
import create_data
import integerize_labels
import split
import find_k_nearest_neighbors as fknn
import majority_vote as mv

def knn(train_data, test_data, k):
    predicted_labels = []
    
    for row in test_data:
        neighbors = fknn.find_k_nearest_neighbors(row, test_data, k)
        #this uses find_k_nearest_neighbors to calculate the neighbors
        predicted_labels.append(mv.majority_vote(neighbors))
        #this uses majority vote to predict what flower it will be
        
    return predicted_labels

data = create_data.create_data("iris.data.txt")
integerized_data = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
print("train_data")
print(train_data)
print("test_data")
print(test_data)
print("knn")
print(knn(train_data, test_data, 4))
