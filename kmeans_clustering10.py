# -*- coding: utf-8 -*-
"""kmeans clustering10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c7sb1LVYaH05AphjI9-6jPwZ6NNSv_Fb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

# Define the dataset
data_dict = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [53, 22, 45, 33, 57, 21, 59, 60, 40, 25],
    "Income": [500, 45, 150, 450, 160, 47, 580, 600, 155, 50]
}

# Create DataFrame
df = pd.DataFrame(data_dict)

# Step 1: Assign labels based on Income range
def income_label(income):
    if income < 100:
        return "Low"
    elif 100 <= income < 170:
        return "Medium"
    else:
        return "High"

df["Income_Label"] = df["Income"].apply(income_label)

# Step 2: Perform K-Means Clustering with K=2 (First two points as initial centroids)
X = df[['Age', 'Income']].values

# Initialize K-Means with first two points as centroids
initial_centroids = np.array([X[0], X[1]])

kmeans = KMeans(n_clusters=2, init=initial_centroids, n_init=1, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Step 3: Compute Purity, Precision, Recall, and F-Measure
# Map labels to numerical values for comparison
label_mapping = {"Low": 0, "Medium": 1, "High": 2}
df["True_Label"] = df["Income_Label"].map(label_mapping)

# Create confusion matrix
cm = confusion_matrix(df["True_Label"], df["Cluster"])

# Compute Purity (max cluster label per group)
purity = np.sum(np.amax(cm, axis=0)) / np.sum(cm)

# Compute Precision, Recall, and F-Measure for each cluster
precision = np.diag(cm) / np.sum(cm, axis=0, where=np.sum(cm, axis=0) != 0)
recall = np.diag(cm) / np.sum(cm, axis=1, where=np.sum(cm, axis=1) != 0)
f_measure = 2 * (precision * recall) / (precision + recall)

# Display results
print(df)
print("\nPurity:", purity)
print("Precision:", precision)
print("Recall:", recall)
print("F-Measure:", f_measure)

