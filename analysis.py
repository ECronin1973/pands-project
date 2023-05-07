# analysis.py
# The program will analyze Fisher’s dataset by generating a summary for each variable and exporting it to a single text file. 
# Additionally, the program will create a histogram for each variable and output a scatter plot for each pair of variables.
# Author: Edward Cronin

# Designing a Python program to 
# a) output a statistical summary (mean,min,max,standard deviation) of the Iris Dataset and
# b) plot this data in a Scatterplot diagram.

# To analyze the data fully the following Python libraries are imported 

# Load the Pandas Libraries with the alias of pd
import pandas as pd
from pandas import DataFrame

# Load the NumPy Libraries with the alias of np
import numpy as np
from numpy import array

# statistical data visualization 
import seaborn as sns
import matplotlib.pyplot as plt

# Edgar Anderson/Ronald Fisher's Iris dataset data are read in from fishers_iris_dataset.csv 
# This is stored in this working directory.
iris = pd.read_csv("fishers_iris_dataset.csv",delimiter = ',') 

# print a statistical summary by Species
# Firstly, define each species in the dataset i.e. how Python knows which of the three Iris varieties it is
setosa=iris[iris['species']=='setosa']
versicolor =iris[iris['species']=='versicolor']
virginica =iris[iris['species']=='virginica']


with open('summary_Analysis.txt', 'a') as file:
    file.write('\nSummary Statistical Analysis - Iris Setosa\n')
    file.write(setosa.describe().to_string())
    file.write('\n\nSummary Statistical Analysis - Iris Versicolor\n')
    file.write(versicolor.describe().to_string())
    file.write('\n\nSummary Statistical Analysis - Iris Virginica\n')
    file.write(virginica.describe().to_string())

# Now, for each Species, output a scatterplot of 1) Sepal Length and Width and 2) Petal Length and Width
# we are going to output a diagram titled graphs.png.  There are two subplots (two diagrams)
# ax[0], ax[1]
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))
# (fig, ax = plt.subplots(1,2,figsize=(21, 10)) is a line of code in Python that creates a figure with two subplots arranged in one row and two columns. The figsize parameter sets the size of the figure. The first parameter 1 specifies the number of rows and the second parameter 2 specifies the number of columns. The resulting figure is returned as fig, 
# and the two subplots are returned as ax. You can use these subplots to plot different data on each subplot.)


# specifying the data for diagram 1 [ax[0] - The Sepal Length and Width
# the x, y and label values represent the headings in the csv file above
# the kind reflects the type of graph, colour represents the colour of the dots in the scatter graph.
setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

# specifying the data for diagram 2 [ax[1] - the Petal Length and Width
setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

# Set the title, X/Y Labels and Legend of each diagram 
ax[0].set(title='Sepal Comparison Graph ', xlabel='Sepal Length (cm)', ylabel='Sepal Width (cm)')
ax[1].set(title='Petal Comparison Graph',  xlabel='Petal Length (cm)', ylabel='Petal Width (cm)')


# I want to draw attention to specific distribution patterns in the Scatterplots so I use the annotate and arrowprops
# functions to point out the data that shows a specific pattern.
# the text is the text I want to output, the xy is the scatterpoint co-ordinates that I want to point the arrow to. 
# The xytext are the co-ordinates where I want to start printing the text.

plt.annotate('Satosa petals are easier to segregate as they are smaller than other varieties', xy=(1.6, 0.6), xytext=(1.7, 0.7),
        arrowprops=dict(arrowstyle="->", facecolor='red'),
        )
plt.annotate('Versicolor and Virginica are bunched closer together', xy=(4.5, 1.7), xytext=(1.0, 2.0),
        arrowprops=dict(arrowstyle="->", facecolor='green'),
        )
plt.annotate('so harder to seperate', xy=(4.5, 1.7), xytext=(1.0, 1.9))

# output the legend for each graphs
ax[0].legend()
ax[1].legend()

# output the graphs
plt.savefig('scatter_plot_graphs.png')  # saves the plot as an image
plt.close()

#This code is used to create a histogram of the sepal length of the iris dataset. 
sns.set_style("darkgrid")
plt.figure(figsize = (10, 7)) 
x = iris["sepal_length"] 

sns.distplot(x, bins = 20, color = "blue",)
plt.title("Histagram - Sepal Length(cm)") # set title
plt.xlabel("Sepal_Length_cm") # set length
plt.ylabel("Count") # set yaxis to count
plt.grid(True)
plt.savefig('sepal_length.png') # saves the plot as an image


# #This code is used to create a histogram of the sepal width of the iris dataset. 
sns.set() 
plt.figure(figsize = (10, 7))
x = iris["sepal_width"]  

sns.distplot(x, bins = 20, color = "blue")
plt.title("Histagram- Sepal Width (cm)") # set title
plt.xlabel("Sepal_width_cm") # set width
plt.ylabel("Count") # set yaxis to count
plt.savefig('sepal_width.png') # saves the plot as an image


#This code is used to create a histogram of the petal length of the iris dataset. 
sns.set()
plt.figure(figsize = (10, 7)) 
x = iris["petal_length"] 

sns.distplot(x, bins = 20, color = "blue")
plt.title("Histagram - Petal Length(cm)") # set title
plt.xlabel("Petal_Length_cm") # set length
plt.ylabel("Count") # set yaxis to count
plt.savefig('petal_length.png') # saves the plot as an image


#This code is used to create a histogram of the petal width of the iris dataset. 
sns.set()
plt.figure(figsize = (10, 7))  # Code sets the size of the figure to 10 inches by 7 inches 
x = iris["petal_width"]  # Code selects the petal width column from the iris dataset and assigns it to the variable

# Create histogram of the petal width data
sns.distplot(x, bins = 20, color = "blue")
plt.title("Histagram - Petal Width(cm)") # set title
plt.xlabel("Petal_Width_cm") # set width
plt.ylabel("Count") # set yaxis to count
plt.savefig('petal_width.png') # saves the plot as an image
