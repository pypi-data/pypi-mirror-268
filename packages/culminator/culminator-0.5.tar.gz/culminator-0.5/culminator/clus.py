import numpy as np
import pandas as pd

def load_data(filename, drop_columns=None, for_predictions=False, prediction_input=None):
    extension = filename.split('.')[-1]
    if extension == 'csv':
        data =  pd.read_csv(filename)
    elif extension == 'json':
        data = pd.read_json(filename)
    elif extension == 'html':
        data = pd.read_html(filename)[0]
    elif extension in ['xls', 'xlsx']:
        data = pd.read_excel(filename)
    else:
        raise ValueError("Unsupported file type. Supported types are: csv, json, html, xls, xlsx")

    X = data.iloc[:, :]

    if drop_columns != None:
        if isinstance(drop_columns[0], str):
            X = data.drop(drop_columns, axis=1)
        else:
            X = data.drop(data.columns[drop_columns], axis=1)

    if for_predictions:
            input_df = pd.DataFrame(prediction_input, columns=X.columns).apply(pd.to_numeric, errors='ignore')
            X = pd.concat([input_df, X], axis=0)
                    
            string_columns = X.select_dtypes(include=['object']).columns
            X = pd.get_dummies(X, columns=string_columns, dtype=int)
            X = X.values

            altered_input = X[:len(prediction_input)]
            return altered_input

    string_columns = X.select_dtypes(include=['object']).columns
    X = pd.get_dummies(X, columns=string_columns, dtype=int)
    X[X == True] = 1
    X[X == False] = 0
    
    X = X.values
    return X

def scale_features(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std = [x if x != 0 else 0.00000001 for x in std]
    X = (X - mean) / std
    return X, mean, std

def initialize_centroids(X, k):
    num_samples = X.shape[0]
    centroids = X[np.random.choice(num_samples, k, replace=False)]
    return centroids

def calculate_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def assign_clusters(X, centroids):
    num_samples = X.shape[0]
    distances = np.zeros((num_samples, len(centroids)))
    for i, centroid in enumerate(centroids):
        for j, sample in enumerate(X):
            distances[j, i] = calculate_distance(sample, centroid)
    cluster_assignments = np.argmin(distances, axis=1)
    return cluster_assignments

def update_centroids(X, cluster_assignments, k):
    num_features = X.shape[1]
    centroids = np.zeros((k, num_features))
    for i in range(k):
        cluster_points = X[cluster_assignments == i]
        centroids[i] = np.mean(cluster_points, axis=0)
    return centroids

def calculate_cluster_variance(X, centroids, cluster_assignments):
    cluster_variance = 0
    for i, centroid in enumerate(centroids):
        cluster_points = X[cluster_assignments == i]
        cluster_variance += np.sum((cluster_points - centroid) ** 2)
    return cluster_variance

def clustering(filename, k, drop_columns=None, max_iters=10000, initializations=100):
    best_centroids = []
    best_cluster_assignments = []
    best_cluster_variance = float('inf')
    
    X = load_data(filename, drop_columns)
    X, mean, std = scale_features(X)
    
    for _ in range(initializations):
        centroids = initialize_centroids(X, k)
        for _ in range(max_iters):
            prev_centroids = centroids.copy()
            cluster_assignments = assign_clusters(X, centroids)
            centroids = update_centroids(X, cluster_assignments, k)
            if np.all(prev_centroids == centroids):
                break
        
        cluster_variance = calculate_cluster_variance(X, centroids, cluster_assignments)
        if cluster_variance < best_cluster_variance:
            best_cluster_variance = cluster_variance
            best_centroids = centroids
            best_cluster_assignments = cluster_assignments
    
    for i, assignment in enumerate(cluster_assignments): print(f"Data point {i} is assigned to cluster {assignment}")
    return best_centroids, best_cluster_assignments, mean, std

def predict_values_clustering(input, filename, mean, std, centroids, drop_columns=None):
    input_scaled = load_data(filename, drop_columns, True, input)
    input_scaled = (input_scaled - mean) / std

    num_samples = input_scaled.shape[0]
    num_clusters = centroids.shape[0]
    distances = np.zeros((num_samples, num_clusters))
    for i, centroid in enumerate(centroids):
        for j, sample in enumerate(input_scaled):
            distances[j, i] = calculate_distance(sample, centroid)
    predictions = np.argmin(distances, axis=1)

    for i in range(len(predictions)):
        print(f"Data point {input[i]} is assigned to cluster {predictions[i]}")

    return predictions