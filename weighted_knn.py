# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 02:54:09 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
weighted_knn

The purpose of this code is to find the type of flower that the closest 
neighbors of a point are. I added a count to see how many in the list of 
neighbors were from each type of flower. I then verififeid the flower type with
an if statement. This time, instead of importing majority vote, I imported 
weighted_majority_vote to calculate a weighted KNN.
--------------------------
'''
     #Your code here
import create_data
import integerize_labels
import split
import find_k_nearest_neighbors as fknn
import weighted_majority_vote as wmv

def weighted_knn(train_data, test_data, k):
    weighted_predicted_labels = []
    
    for row in test_data:
        neighbors = fknn.find_k_nearest_neighbors(row, test_data, k)
        #this uses find_k_nearest_neighbors to calculate the neighbors
        weighted_predicted_labels.append(wmv.weighted_majority_vote(row, \
                                                                    neighbors))
        #this uses weighted majority vote to predict what flower it will be
    return weighted_predicted_labels

data = create_data.create_data("iris.data.txt")
(integerized_data,x) = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
weighted_knn(train_data, test_data, 4)
    