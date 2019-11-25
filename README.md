# 0-1-Knapsack-Problem-Using-Genetic-Algorithm
The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
### Requirements
1. Python >= 3.4.2 
2. bitarray library (pip install bitarray) 
3. fnmatch (pip install fnmatch) 
4. re (pip install re)
### Repository Structure
#### dataset (folder)
The dataset folder contains all the datasets provided in reference [2]. I have made txt files from the website. The txt files contains Capacity (*_c.txt*), Weights (*_w.txt*), Profits (*_p.txt*) and Optimal Solution (*_s.txt*). There are 8 (eight) cases in the original datasets with 32 files.
#### Knapsack.py
This file contains the functions for population generation, crossover, mutation and fitness evaluation.  
#### main.py
This file reads the dataset and runs knapsack optimization for all 8 (eight) datasets.
#### read_dataset.py
This file reads the values from the dataset files.
### References
1. Wiki: https://en.wikipedia.org/wiki/Knapsack_problem
2. Base Code: https://github.com/Hellisotherpeople/Genetic-Algorithims-Python 
3. Dataset: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
