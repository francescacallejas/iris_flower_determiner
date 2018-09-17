# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:45:57 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
find_k_nearest_neighbors

In this set of code, I found the KNN of the flower indicated up until the value
of k using train_data. I did this by creating a distance list and dictionary.
I added the distances from test_point to all values of train_data to a list.
I also added this value to dictionary. I did this so that when I was making my
list of k_nearest neighbors, it was easy to find the row corresponding to the 
shortest distances by making the distance the key. 
--------------------------
'''
import create_data
import integerize_labels
import split
import euclidean_distance as ed

def find_k_nearest_neighbors(test_point, train_data, k):
    k_nearest_neighbors = [] #list to be returned
    e_d = [] #list corresponding to all distances calculated
    e_d_dict = {} #key is distance and value is the row that belongs to it
    for row in train_data : #iterates through each row
        d = ed.euclidean_distance(test_point, row) #caluclates distances
        e_d.append(d) #appends the distance to distance list
        e_d_dict[d] = row #adds distance and list to dictionary
    e_d.sort() #sorts list in ascending order
   
    for i in range (0, k): #will only add a k value near neighbors
        a = e_d[i] #finds row corresponding to shortest distance      
        k_nearest_neighbors.append(e_d_dict[a]) #adds row to knn list
        
    return k_nearest_neighbors

data = create_data.create_data("iris.data.txt")
(integerized_data, x) = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
test_point = test_data[0]
k = 6
find_k_nearest_neighbors(test_point, train_data, k)
