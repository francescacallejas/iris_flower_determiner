# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 00:40:03 2016
@author: francescacallejas
# -*- coding: utf-8 -*-
Created on Sun Nov 27 00:40:03 2016
@author: francescacallejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/10/2016
create_data

To create the data, I opeend the file in which the data was stored and read it 
line-by-line. For each line I removed the \n and split it after each comma, 
since that is what separates the data. This returns a list which I then 
appened to my overall list of data, making a two dimensional list. I then use
the numpy function to create a numpy matrix.

--------------------------
'''

def create_data(input_data_file):     #Your code here

    file = open(input_data_file,"r") #open file
    
    data_list = []
    line = file.readlines() #reading every line

    for l in line:
        info_split = l.rstrip('\n').split(',') #removing "new line" and 
        #splitting into lists by commas
        data_list.append(info_split) #appending this list to my data_list
        
    for x in range (0, len(data_list)): #replaicing string values with floats
        data_list[x][0] = float(data_list[x][0])
        data_list[x][1] = float(data_list[x][1])
        data_list[x][2] = float(data_list[x][2])
        data_list[x][3] = float(data_list[x][3])
        
    data = data_list
    file.close() #close file
    
    return data

create_data("iris.data.txt")