# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:36:29 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
calculate_error_rate

To calculate the error rate, I imported my predicted labels and test_data and
compared values. Each time, I counted the total number. If the numbers were
different, I also added to my wrong_count. At the end I divided wrong_count by
total_count to find my total error rate. 

--------------------------
'''
import create_data
import integerize_labels
import split
import knn

def calculate_error_rate(predicted_labels, test_data):     #Your code here
    i = 0
    total_count = 0 #counts all values being tested
    wrong_count = 0 #counts all values that are wrong
    for label in predicted_labels:
        if label == test_data[i][4]: #comparing values
            total_count += 1 #adding one evry time 
        elif label != test_data[i][4]: #comparing values
            wrong_count += 1 #adding one if its wrong
            total_count +=1 #adding one every time
        i +=1
    error_rate = wrong_count/total_count 
    
    return error_rate

data = create_data.create_data("iris.data.txt")
integerized_data = integerize_labels.integerize_labels(data)
(train_data, test_data) = split.split(integerized_data)
k = 4
predicted_labels = knn.knn(train_data, test_data, k)
calculate_error_rate(predicted_labels, test_data)