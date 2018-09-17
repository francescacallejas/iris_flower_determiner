# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:16:04 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
euclidean_distance

In this code I found the euclidean distance by using the distance formula. I
made a for loop that first found the squared difference between the correspo-
nding values. It then found the sum of all the numbers. Finally outside the
loop, once all values had been calculated (minus the last one because that is 
just the value indicating the flower), I calculated the square root.
--------------------------
'''
import math
def euclidean_distance(x1, x2):
    num_difference = 0 
    num_sum = 0 
    
    for i in range (0, len(x1)-1): #the -1 accounts for integer value of flower
        num_difference = (x1[i]-x2[i])**2 #difference squared
        num_sum += num_difference #sum of all values in list
    distance = math.sqrt(num_sum)
    return distance

'''test cases:
x1 = [32, 61, 18, 95, 0]
x2 = [74, 21, 58, 24, 1]
euclidean_distance(x1, x2) = 100.024996875781 '''