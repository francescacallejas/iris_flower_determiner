# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:55:41 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
split

In this code, I split my data into two lists: one is a randomized list of 15 of
each type of flowers and the second is the remaining data. I did this by 
creating a while loop inside of which I added conditonals that made sure that
15 of each type of data went into the loop. 
--------------------------
'''
import random 
import create_data
import integerize_labels
 
def split(integerized_data):
    test_data = []
    j = 1
    k = 1
    l = 1
    
    while len(test_data) < 45 : #15 of each type of flower = 45
        r = random.randint(0,len(integerized_data)-1) #picks random data 
        #from among all data
        #the if statements check to see which flower value each random 
        #corresponds to and adds 15 of each to to test_data 
        if integerized_data[r][4] == 0 and integerized_data[r] not in \
        test_data and j<16:
            test_data.append(integerized_data[r])
            j += 1 #counter to make sure only 15 are added
        elif integerized_data[r][4] == 1 and integerized_data[r] not in \
        test_data and k<16:
            test_data.append(integerized_data[r])
            k += 1 #counter to make sure only 15 are added
        elif integerized_data[r][4] == 2 and integerized_data[r] not in \
        test_data and l<16:
            test_data.append(integerized_data[r])
            l += 1 #counter to make sure only 15 were added
         
    train_data = integerized_data[:] #copy of integerized_data
    
    for row in test_data:
        train_data.remove(row) #removes every one that appears in test_data
    
    return train_data,test_data

data = create_data.create_data("iris.data.txt")
(integerized_data, x) = integerize_labels.integerize_labels(data)
split(integerized_data)