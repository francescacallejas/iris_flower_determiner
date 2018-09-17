# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 02:04:54 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
weighted_majority_vote

For my weighted_majority_vote, I found the average distance between the 
test_point and and each type of flower in neighbors. Whichever average was 
smallest, I assigned that value as the label.  
 
--------------------------
'''

import create_data
import integerize_labels
import split
import find_k_nearest_neighbors as fknn
import euclidean_distance as ed

def weighted_majority_vote(test_point, neighbors):     #Your code here
    distance_0 = []
    distance_1 = []
    distance_2 = []
    total_distance = []
    mean_0 = None
    mean_1 = None
    mean_2 = None
    weighted_majority_label = 0
    
    for i in neighbors: 
    #this for loops finds distances of all flower types 
        if i[4] == 0: #if it is labelled 0 then add to distance_0 list
            dist = ed.euclidean_distance(test_point, i)
            distance_0.append(dist)
        elif i[4] == 1: #if it is labelled 1 then add to distance_1 list
            dist = ed.euclidean_distance(test_point, i)
            distance_1.append(dist)
        elif i[4] == 2:  #if it is labelled 2 then add to distance_2 list
            dist = ed.euclidean_distance(test_point, i)
            distance_2.append(dist)

    if len(distance_0) > 0: #if its not an empty list
        mean_0 = sum(distance_0)/len(distance_0) #find average distance for 0
        total_distance.append(mean_0) #add this average to my total distance
    if len(distance_1) > 0: #if it is not an empty list
        mean_1 = sum(distance_1)/len(distance_1) #find average distance for 1
        total_distance.append(mean_1) #add this average to my total distance
    if len(distance_2) > 0: #if it is not an empty list
        mean_2 = sum(distance_2)/len(distance_2) #find average distance for 2
        total_distance.append(mean_2) #add this average to my total distance
    
    '''for these statements, I also added the conditional \"if != None\"  
    to make sure that that value exists'''
    if min(total_distance) == mean_0 and mean_0 != None: #if 0 is shortest
        weighted_majority_label = 0
    elif min(total_distance) == mean_1 and mean_1 != None: #if 1 is shortest
        weighted_majority_label = 1
    elif min(total_distance) == mean_2 and mean_2 != None: #if 2 is shortest
        weighted_majority_label = 2
        
    return weighted_majority_label
        
data = create_data.create_data("iris.data.txt")
(integerized_data, x) = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
test_point = test_data[0]
k = 6
neighbors = fknn.find_k_nearest_neighbors(test_point, train_data, k) 
print(test_point)
print(weighted_majority_vote(test_point, neighbors))


