Project 2023 Programming and Scripting
This repository consists of my analysis of the Fisher's Iris dataset as specified in the 2023 Project document Link to Project PDF

How to download this repository
1. Logon to GitHub to locate my specific repository dedicated to this project located at this link My repositry for pands-project on GitHub.
2. Click the download button.
3. To run the code, ensure you have Python installed.

Analysis of Fisher's Iris Dataset

Introduction
Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in 1936, as an example of *linear discriminant analysis* i.e. a method used in statistics to find a linear combination of features that characterizes or separates two or more classes of objects or events. 
In this study, Fisher wished to investigate if the species of an Iris flower could be identified by examining its petal and sepal length and width.

## The Data
The data was collected by Fisher’s colleague, Edgar Anderson, in order to quantify the scientific variation of Iris flowers of three related species. Two of the three species (setosa and versicolor) were collected in the Gaspé Peninsula in Quebec, Canada - with a high level of consistency in the collection process:-  
>all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus <sup>[Reference 2](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)</sup>

The third species (virginica) was collected from a different colony.


![Figure 1: Species of Iris collected](https://github.com/gabrielmulligan/fishersirisdataset/blob/master/Iris_Flowers.png)
##### Figure 1: The three species of Iris collected and analyzed by Anderson and Fisher

The data set consists of fifty samples from each of three species of Iris (setosa, versicolor and virginica). Four features were measured (in cm) from each sample:-
- Length of Petal
- Width of Petal
- Length of Sepal* (i.e. the firm green part that supports the petal once it has bloomed) 
- Width of Sepal

Based on the combination of these four features, Fisher developed a *linear discriminant model* (defined above) to distinguish the species from each other.

## Statistical Summary Tables

These tables detail the mean (average), standard deviation and min/max (incl. 25th/50th/75th percentiles) of the data for the three Iris species, as collected and documented by Edgar Anderson.

### Setosa

| IRIS SETOSA |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count of sample data| 50 | 50 | 50 | 50 |
| Mean (Average)| 5.006 | 3.418 | 1.464 | 0.244 |
| Standard Deviation | 0.35249 | 0.381024 |0.173511 | 0.10721 |
| Minimum Value | 4.3 | 2.3 |1.0 | 0.1 |
| 25th percentile | 4.8 | 3.125 |1.4 | 0.2 |
| 50th percentile | 5.0 | 3.4 |1.5 | 0.2 |
| 75th percentile | 5.2 | 3.675 |1.575 | 0.3 |
| Maximum Value | 5.8 | 4.4 |1.9 | 0.6 |

### Versicolor

| IRIS VERSICOLOR |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count of sample data | 50 | 50 | 50 | 50 |
| Mean (Average)| 5.936 | 2.77 | 4.26 | 1.326 |
| Standard Deviation | 0.516171 | 0.313798 |0.469911 | 0.197753 |
| Minimum Value | 4.9 | 2.0 |3.0 | 1.0 |
| 25th percentile | 5.6 | 2.525 |4.0 | 1.2 |
| 50th percentile | 5.9 | 2.8 |4.35 | 1.3 |
| 75th percentile | 6.3 | 3.0 |4.6 | 1.5 |
| Maximum Value | 7.0 | 3.4 |5.1 | 1.8 |

### Virginica

| IRIS VIRGINICA |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count of sample data| 50 | 50 | 50 | 50 |
| Mean (Average)| 6.588 | 2.974 | 5.552 | 2.026 |
| Standard Deviation | 0.63588 | 0.322497 |0.551895 | 0.27465 |
| Minimum Value | 4.9 | 2.2 |4.5 | 1.4 |
| 25th percentile | 6.225 | 2.8 |5.1 | 1.8 |
| 50th percentile | 6.5 | 3.0 |5.55 | 2.0 |
| 75th percentile | 6.9 | 3.175 |5.875 | 2.3 |
| Maximum Value | 7.9 | 3.8 |6.9 | 2.5 |

## Scatterplot Diagrams

These are the two scatterplot diagrams showing the distribution of a) Sepal Length and Width and b) Petal Length and Width across the three species of Iris.

![Figure 2: Scatterplot Diagrams of Fisher's Iris Dataset](https://github.com/gabrielmulligan/fishersirisdataset/blob/master/Fisher_Scatterplots.png)
##### Figure 2: Scatterplot Diagrams of Fisher's Iris Dataset


This is a summary of the main statistics of the dataset, per species:-

![Figure 3: Tabular Summary of the Primary Statistics of each Iris species](https://github.com/gabrielmulligan/fishersirisdataset/blob/master/Fisher_Summary.png)
##### Figure 3: Tabular Summary of the Primary Statistics of each Iris species

# Findings

From the scatterplot diagrams above, **Iris Setosa is linearly separable from the other two**, while there is considerable overlap between Iris Virginica and Iris Versicolor, particularly in the analysis of sepal length and width - as can be seen from both figures in the diagrams (generated from the Python program below).

Iris Setosa is seperable by the fact that its *Petal Length and Width* are significantly less than the other two species. This is represented by the clustering of the Setosa points in the two scatterplot diagrams and the mimimum of overlap with the other two species. 

Iris Virginica and Versicolor are more difficult to segregate based on this data collection, highlighted by the closeness and overlap of the clusters. However, the Virginica species does have a slightly longer petal length vs. Versicolor, and significantly longer than Setosa.

Setosa's petal length ranges from 1.0-1.9cm and petal width from 0.1-0.6cm, substantially less than Versicolor's (Len 3.0-5.1cm and Wid 1.0-1.8cm) and Virginica's (Len 4.5-6.9cm and Wid 1.4-2.5cm). Visually, the Setosa is a much smaller flower, compared to the other two species.

|      |Setosa|Versicolor|Virginica|
| --- | --- | --- |--- |
| Min Petal Length | **_1.0_** | 3.0 |4.5 |
| Max Petal Length| **_1.9_** | 5.1 |6.9 |
| | |  | |
| Min Petal Width| **_0.1_** | 1.0 |1.4 |
| Max Petal Width| **_0.6_** | 1.8 |2.5 |

# Legacy

This dataset has become a renowned test case for many statistical and machine learning projects, given Fisher's *linear discriminant model* and how the data collected by Anderson could be used to find a linear combination of features that characterize or separate two or more classes of objects/events i.e. the length and width of the sepals and petals of these three Iris species being used to infer which species that data sample belongs to.

The fact that this dataset is available as part of the Scikit machine-learning library in Python - and therefore analyzed as part of many third-level courses - means that more and more students over a range of disciplines (e.g. IT, Maths, Biology) access and analyze this dataset each year to understand the groundbreaking work undertaken by Fisher and Anderson.

# Python Program 
## fisher_scatterplot.py

This outputs both a statistical analysis (mean,min,max,standard deviation) of the Iris Dataset using the `describe` function in Python and plots the findings of the 150 samples into a scatterplot diagram to highlight specific patterns in the two diagrams. Both outputs are shown in Figure 2 and 3 above.

# REFERENCES
I used the following online resources in compiling the Management Summary documented above, including researching how to code scatterplot diagrams in Python, specifically Reference 3 below - Abhishek Gupta on kaggle.com - which greatly helped explain how the arrays and features of a dataset are setup in order to accurately create scatterplots once the program is run.


1. [Downloadable CSV file of Fisher's Dataset from GitHub User Content](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)
2. [Source Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Ann. Eugenics 7, Pt. II, 179-188.](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)
3. [Abhishek Gupta's analysis of the Fisher Dataset on kaggle.com](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
4. [An overview of the Iris Dataset from Codebag NG incl. some programs to help analyze it](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)
5. [Edukast's Youtube video on Machine Learning Classification - specifically using Fisher's Iris Dataset](https://www.youtube.com/watch?v=wIubuU7gejM)
6. [Dr. Ian McLoughlin's GMIT lectures](https://web.microsoftstream.com/video/6db924ef-af13-47da-a620-0e5b59e1c0ff)
7. [Writing readme.md files on Github](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
8. [Creating tables in markdown](https://www.makeuseof.com/tag/create-markdown-table/)


