# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 21:24:37 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
majority_vote(neighbors)

The purpose of this code is to find the type of flower that the closest 
neighbors of a point are. I added a count to see how many in the list of 
neighbors were from each type of flower. I then verififeid the flower type with
an if statement. 
--------------------------
'''
import create_data
import integerize_labels
import split
import find_k_nearest_neighbors as fknn

def majority_vote(neighbors):
    setosa_count = 0 
    versicolor_count = 0
    virginica_count = 0 
    
    for i in range (0, len(neighbors)):
        if neighbors[i][4] == 0:
           setosa_count += 1 
           #counting how many neighbors are of the setosa type
        elif neighbors[i][4] == 1:
            versicolor_count += 1
            #counting how many neighbors are of the versicolor type
        elif neighbors[i][4] ==2:
            virginica_count += 1
            #counting how many neighbors are of the virginica type
    
    count_check = [setosa_count, versicolor_count, virginica_count]
    count_check.sort()
    #added the count type to a list and sorted it to see what occurs the most
    
    if setosa_count == count_check[2]:
        majority_label = 0
    elif versicolor_count == count_check[2]:
        majority_label = 1
    elif virginica_count == count_check[2]:
        majority_label = 2
    #whichever is in the third index is the majority count because they are 
    #sorted in ascending order. If the 2nd index is repeated, then it will
    #be assigned to whatever if statement it falls under first: setosa,
    #versicolor, and then virginca
        
    return majority_label

data = create_data.create_data("iris.data.txt")
integerized_data = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
test_point = test_data[0]
k = 6
neighbors = fknn.find_k_nearest_neighbors(test_point, train_data, k)
majority_vote(neighbors)