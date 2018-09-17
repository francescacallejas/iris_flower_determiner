# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 03:00:03 2016

@author: Fran Callejas
"""
'''
--------------------------
Francesca Callejas
ffc2108
12/01/2016
plot_data

To plot my data, I called on create_data in order to have my data organzied and
in an editable format. I then made variables that would hold the sepal 
lengths, sepal widths, petal lengths, and petal widths of all three types of 
flowers and added those values through a for loop. I then graphed each pair of 
data. 
--------------------------
'''
import create_data
import matplotlib.pyplot as plt

def plot_data(data):
    sepal_L = [] #sepal length
    sepal_W = [] #sepal width
    petal_L = [] #petal length
    petal_W = [] #petal width 
    sepal_L1 = []
    sepal_W1 = []
    petal_L1 = []
    petal_W1 = []
    sepal_L2 = []
    sepal_W2 = []
    petal_L2 = []
    petal_W2 = []

    
    for x in range (0, len(data)):
        if data[x][4] == 'Iris-setosa': #appending all setosa data
            sepal_L.append(data[x][0])
            sepal_W.append(data[x][1])
            petal_L.append(data[x][2])
            petal_W.append(data[x][3])
        elif data[x][4] == 'Iris-versicolor': #appending all versicolor data
            sepal_L1.append(data[x][0])
            sepal_W1.append(data[x][1])
            petal_L1.append(data[x][2])
            petal_W1.append(data[x][3])
        elif data[x][4] == 'Iris-virginica': #appending all virginica data
            sepal_L2.append(data[x][0])
            sepal_W2.append(data[x][1])
            petal_L2.append(data[x][2])
            petal_W2.append(data[x][3])
        
    #sepal length vs sepal width 
    SLSW = plt.plot(sepal_L, sepal_W, 'ro', label = "setosa") 
    #red circles for setosa values
    SLSW = plt.plot(sepal_L1, sepal_W1, 'yv', label = "versicolor") 
    #yellow triangles for versicolor 
    SLSW = plt.plot(sepal_L2, sepal_W2, 'bx', label = "virginica") 
    #blue x's for virginica 

    plt.title("Sepal Length vs Sepal Width") # Add a title
    plt.xlabel('Sepal Length') # Add axis labels
    plt.ylabel('Sepal Width') # Add axis labels
    plt.axis([4, 10, 1.5, 5])
    plt.legend()
    
    plt.show()
    
    #sepal length vs petal length
    SLPL = plt.plot(sepal_L, petal_L, 'ro', label = "setosa")
    SLPL = plt.plot(sepal_L1, petal_L1, 'yv', label = "versicolor")
    SLPL = plt.plot(sepal_L2, petal_L2, 'bx', label = "virginica")
    
    plt.title("Sepal Length vs Petal Length") # Add a title
    plt.xlabel('Sepal Length') # Add axis labels
    plt.ylabel('Petal Length') # Add axis labels
    plt.axis([4, 10, 0, 8])
    plt.legend()

    plt.show()

    #sepal length vs petal width 
    SLPW = plt.plot(sepal_L, petal_W, 'ro', label = "setosa")
    SLPW = plt.plot(sepal_L1, petal_W1, 'yv', label = "versicolor")
    SLPW = plt.plot(sepal_L2, petal_W2, 'bx', label = "virginica")
    
    plt.title("Sepal Length vs Petal Width") # Add a title
    plt.xlabel('Sepal Length') # Add axis labels
    plt.ylabel('Petal Width') # Add axis labels
    plt.axis([4, 10, 0, 3])
    plt.legend()
    
    plt.show()
    
    #sepal width vs petal length 
    SWPL = plt.plot(sepal_W, petal_L, 'ro', label = "setosa")
    SWPL = plt.plot(sepal_W1, petal_L1, 'yv', label = "versicolor")
    SWPL = plt.plot(sepal_W2, petal_L2, 'bx', label = "virginica")
    
    plt.title("Sepal Width vs Petal Length") # Add a title
    plt.xlabel('Sepal Width') # Add axis labels
    plt.ylabel('Petal Length') # Add axis labels
    plt.axis([1.5, 6.5, 0, 8])
    plt.legend()
    
    plt.show()
    
    #sepal width vs petal width 
    SWPW = plt.plot(sepal_W, petal_W, 'ro', label = "setosa")
    SWPW = plt.plot(sepal_W1, petal_W1, 'yv', label = "versicolor")
    SWPW = plt.plot(sepal_W2, petal_W2, 'bx', label = "virginica")
    
    plt.title("Sepal Width vs Petal Width") # Add a title
    plt.xlabel('Sepal Width') # Add axis labels
    plt.ylabel('Petal Width') # Add axis labels
    plt.axis([1.5, 6.5, 0, 3])
    plt.legend()
    
    plt.show()
    
    #petal length vs petal width 
    PLPW = plt.plot(petal_L, petal_W, 'ro', label = "setosa")
    PLPW = plt.plot(petal_L1, petal_W1, 'yv', label = "versicolor")
    PLPW = plt.plot(petal_L2, petal_W2, 'bx', label = "virginica")
    
    plt.title("Petal Length vs Petal Width") # Add a title
    plt.xlabel('Petal Length') # Add axis labels
    plt.ylabel('Petal Width') # Add axis labels
    plt.axis([0, 11, 0, 3])
    plt.legend()
    
    plt.show()

data = create_data.create_data("iris.data.txt")
plot_data(data)