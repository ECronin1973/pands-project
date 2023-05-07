# Project 2023 Programming and Scripting

This repository consists of my analysis of the Fisher's Iris dataset as specified in the 2023 Project document [Link to Project PDF](https://vlegalwaymayo.atu.ie/pluginfile.php/857740/mod_label/intro/Project%202023.pdf?time=1678806986892 )
Author: Edward Cronin g00425645

# How to download this repository

1. Logon to GitHub to locate my specific repository dedicated to this project located at [My repository for pands-project on GitHub]( https://github.com/ECronin1973/pands-project) .
2. Click the download button.
3. To run the code, ensure you have Python installed.  Type command ‘python analysis.py to generate summary_Analysis.txt file along with various image (PNG) files ’.

# Analysis of Fisher's Iris Dataset

# Introduction

The Fisher’s Iris data set is a famous data set in statistics and machine learning.  The data set contains three species of Iris flowers with four features measured from each sample.  The data set was used by Fisher to demonstrate linear discriminant analysis, a method to classify objects based on linear combinations of features.  Two of the data set was collected by Edgar Anderson from the same pasture in the Gaspé Peninsula.  The third species (virginica) was collected from a different colony.

# literature Review

After studying many different articles, books and videos on Fishers data set analyses which presented numerous different approaches to analysing the data set, I concluded that a simplified exploratory data analysis would work best. [13] While a study by Kozak and Lotocka (2013) raised the question: Do Iris flowers have sepals?, which makes the data less interesting for botanists, statisticians have successfully used the data set for years. Exploratory Data Analysis is the process of analysing data by using simple concepts from statistics and probability and presenting the results in easy-to-understand pictorial format (Nabria, 2019). The data would be analysed using Python, Pandas, Matplotlib, Pyplot and Seaborn libraries. Histograms and scatterplots would also be produced to help visualise data and aid comparative analysis. [13]

# Plan

At the commencement of this project, I made a plan of how the assessment criteria and objectives could most accurately, and efficiently, be met.  This was laid out in the Project Guideline Document (https://vlegalwaymayo.atu.ie/pluginfile.php/857740/mod_label/intro/Project%202023.pdf?time=1678806986892).  My approach to this project was four pronged;  1. Firstly I Identified the inputs - what data was needed and where to get it. 2. I then Identified the processes - How to manipulate the data to produce meaningful results. 3. Next I Identified the outputs - What outputs need to be returned and in what format. 4. Finally I broke the project down into smaller parts, and what processes need to happen in each section.  These again were outlined in the Project Guideline Document.
I followed a similar approach to that outlined in the repository of Willie2511[13].  The first part of the project entailed researching the methods which would be implemented, and importing the necessary libraries into the python file which would be used to meet the aims and objectives of this project. The iris dataset was downloaded online as a .csv file titled fishers_iris_dataset.csv and saved into the pands-project folder.   Once all necessary libraries were imported, the next part focused on writing up the first piece of code, which when run on the terminal, would produce desired results and would meet the assesment criteria. Code to Dissect the dataset, acquire descriptions, calculate averages and standard deviations, and group the data into classes were all carried out in this section of the project.
The third section of this project was to produce four histograms and two scatter plots of each pair of variables, and to export each histogram as a .png file. As part of this section of the project, research was also conducted into how to export a summary of each variable into a .txt file when the program was run. From researching online others approaches to generating this content and outputting the content into a text file , I was able to write code which would perform this function as accurately as possible.
The Final step of the project was to investigate some interesting approaches and results from other studies on the dataset, which would require learning how to use new libraries and developing new code. The majority of research conducted on this dataset used different types of visual representation. This opened up the potential to explore new graphs and libraries which may be beneficial in effectively displaying results in future research. Scatterplot Diagrams were chosen to best represent the sepal and petal length and widths.  This allowed for better visualisation of the three petals as was stated by Prateek  ‘We can also plot a single graph for multiple samples which helps in more efficient data visualization’ (Prateek,2019).

## Code of Conduct

A code of conduct governs the use of this repository and has been uploaded within the repository for ease of reference.

## The Data

According to the site Kaggle, “the data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.”  Data for this project was downloaded by the author and saved in the pands-project folder[1] and titled ‘fishers_iris-dataset.csv’.

## Statistical Summary Tables

The tables contained in the summary_Analysis.txt file detail the count, mean (average), standard deviation and min/max (incl. 25th/50th/75th percentiles) of the data for the three Iris species (Iris Setosa, Iris Versicolor Iris Virginica), as collected and documented by Edgar Anderson.  Zeros were removed from each table for ease of viewing.  (* use of pipe character (|) separates the individual columns in the following tables [9].)
 
### Summary Statistical Analysis - Iris Setosa.  

IRIS SETOSA |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count of sample data| 50. | 50.  | 50.  | 50.  |
| Mean (Average)| 5.006 | 3.418 | 1.464 | 0.244 |
| Standard Deviation | 0.35249 | 0.381024 |0.173511 | 0.10721 |
| Minimum Value | 4.3 | 2.3 |1.0 | 0.1 |
| 25th percentile | 4.8 | 3.125 |1.4 | 0.2 |
| 50th percentile | 5.0 | 3.4 |1.5 | 0.2 |
| 75th percentile | 5.2 | 3.675 |1.575 | 0.3 |
| Maximum Value | 5.8 | 4.4 |1.9 | 0.6 |

### Summary Statistical Analysis - Iris Versicolor
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

### Summary Statistical Analysis - Iris Virginica

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

## Histogram Diagrams

Four histogram Diagrams are generated from the which will display Petal length (petal_length.png), Petal width (petal_width.png), Sepal length (sepal_length.png) and Sepal width(sepal_length.png).  Each histogram gives a count value on the Y axis and describes what the histogram relates to along with length /  width in cm on the X axis.
   

  
## Scatterplot Diagrams
Two scatterplot diagrams are generate which show the distribution of a) Sepal Length and Width and b) Petal Length and Width across the three species of Iris.
   
(* note: Setosa petals are smaller so are easier to segregate, they are red in color.  The other two are harder to separate

# Findings
The text shows how the scatterplot diagrams above can separate Iris Setosa from the other two species by a linear boundary, while Iris Virginica and Versicolor have more overlap and are harder to distinguish, especially by their sepal size - as seen in both diagrams (made by the Python program analysis.py).   
Iris Setosa has much smaller petals than the other two species, which can be seen in the bottom left of the scatterplot diagram “petal_length.png”. Iris Virginica and Versicolor are more similar in their petal size, but Virginica has slightly longer petals than Versicolor and much longer than Setosa. 
Setosa’s petals are length 1.0 to 1.9cm long and 0.1 to 0.6cm wide as can be seen in the bottom left of the scatterplot diagram “petal_length.png”.  These are much smaller than Versicolor’s which has a length of 3.0 to 5.1cm long and a width 1.0 to 1.8cm wide and Virginica’s  which has a length of 4.5 to 6.9cm long and a width of 1.4 to 2.5cm wide.  
In conclusion,  visually, Setosa is a much smaller flower in comparison to the other two species.

# Python Program 
The program analysis.py takes 150 samples contained in fishers_iris_dataset.csv and performs a statistical analysis utilising the describe() function to output various statistical information such as mean, min, max, standard deviation.

# REFERENCES
The following online resources were used to complete this project and compile this README.md document. 
1. [CSV file of Fisher's Dataset Downloaded from GitHub User Content](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)
2. [Dr. Andrew Beatty, ATU lectures](https://vlegalwaymayo.atu.ie/course/view.php?id=6208)
3. [Source Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Ann. Eugenics 7, Pt. II, 179-188.](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)
4. [The Problem of Species in the Northern Blue Flags, Iris versicolor L. and Iris virginica L.](https://www.jstor.org/stable/2394087?origin=crossref)
5. [Abhishek Gupta's analysis of the Fisher Dataset on kaggle.com](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
6. [Exploritory Data Analysis on Iris Dataset](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
7. [Edukast's Youtube video on Machine Learning Classification - specifically using Fisher's Iris Dataset](https://youtu.be/f3ZJbTyz_pU)
8. [Writing readme.md files on Github](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
9. [Creating tables in markdown](https://www.makeuseof.com/tag/create-markdown-table/)
10. Prateek, S. (2019) "KDE Plot Visualization with Pandas and Seaborn" Geeks For Geeks. Available at: https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/ Accessed on: 07.05.2023.
11. Kozak, M., Lotocka, B. (2013) 'What should we know about the famous Iris data?' CURRENT SCIENCE, VOL. 104, NO. 5. Available at: https://www.researchgate.net/profile/Marcin_Kozak/publication/237010807_What_should_we_know_about_the_famous_Iris_data/links/02e7e51be9229f3495000000.pdf Accessed on: 30-03-2020.
Other Repositories were researched on the world wide web and viewed as to their approach to researching the Fishers Iris Dataset.  The following are repositories viewed
11. Analysis of the Fisher's Iris Dataset by Geetha Karthikesan , 2019 [Link to Project PDF] (GitHub - geetharamson/Fisher-s-Iris-Dataset)
12. Analysis of the Fisher's Iris Dataset by Ian McLoughlin, 2019  [Link to Project PDF ](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf )
13. Analysis of the Fisher's Iris Dataset by Gabriel Mulligan, 2019  [Link to Project PDF ](GitHub - gabrielmulligan/fishersirisdataset: An analysis of Fisher's Iris Dataset)
14. Analysis of the Fisher's Iris Dataset by “Willie2511”, 2020  [Link to Project PDF ](GitHub - Willie2511/Fishers-Iris-Project: Fisher's Iris Dataset)

