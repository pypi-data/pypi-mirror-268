# Culminator
Culminator is a Python package designed to facilitate regression, classification, and clustering. It provides functionalities for data loading, preprocessing,  training, and predicting. This README file serves as a guide to understand and utilize the package effectively.

## Installation
To install culminator, you can use pip:

```
pip install culminator
```

## Regression
The regression module provides functions for training and predicting regression models.

**Functions:**
1. regression: Trains a regression model
2. predict_values_regression: Predicts values using a trained regression model

```
from culminator import regression

X, y, degree, parameters, predictions, mean, std = regression(filename="Diamonds Prices V2.csv", y_column=7, drop_columns=[0], round_digits=2)

input_data = np.array([[0.3,"Ideal","I","SI2",62,54,348,4.31,4.34,2.68],
                       [0.42,"Premium","G","VS2",61.9,58,1087,4.82,4.77,2.97],
                       [0.7,"Premium","F","SI2",62.5,60,2373,5.66,5.61,3.52]])
input_predictions = predict_values(input_data, "Diamonds are Forever V2.csv", mean, std, degree, parameters, 7, [0], 2)
```

## Classification
The classification module provides functions for training and predicting classification models.

**Functions:**
1. classification: Trains a classification model
2. predict_values_classification: Predicts values using the trained classification model

```
from culminator import classification

X, y, parameters, predictions, label_map, mean, std = classification(filename="Diabetes.csv", drop_columns=[0,2])

input_data = np.array([[1,95,66,13,38,19.6,0.334,25],
                       [7,81,78,40,48,46.7,0.261,42],
                       [10,101,86,37,0,45.6,1.136,38]])
input_predictions = predict_values(input_data, "Diabetes.csv", mean, std, parameters, label_map, drop_columns=[0,2])
```

## Clustering
The clustering module provides functions for clustering data points.

**Functions:**
1. clustering: Performs clustering on a dataset
2. predict_values_clustering: Predicts cluster assignments for new data points

```
from culminator import clustering

centroids, cluster_assignments, mean, std = clustering(filename="Flower Species.csv", k=3)

input_data = np.array([[13, "Blue, 2.59,2.87],
                       [11, "Purple", 0.74,2.5],
                       [13, "Green", 4.28,2.26]])
input_predictions = predict_values(input_data, "Wine Types.csv", mean, std, centroids)
```

# Notes
- Ensure that the input data files are properly formatted and contain necessary columns.
- This README provides a brief overview of the package and its functionalities. For detailed documentation, including parameter descriptions and usage examples, refer to the [official documentation](https://19pranavvedula.wixsite.com/culminator)