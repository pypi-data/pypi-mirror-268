import numpy as np
import pandas as pd

def load_data(filename, y_column=None, drop_columns=None, for_predictions=False, prediction_input=None):
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
    if y_column == None:
        y_column = data.shape[1] - 1
    try:
        if isinstance(y_column, str):
            y_column = data.columns.get_loc(y_column)
    except:
        pass
    y = data.iloc[:, y_column]
    
    drop_columns = [] if drop_columns == None else drop_columns
    try:
        if isinstance(drop_columns[0], str):
            drop_columns = [data.columns.get_loc(column) for column in drop_columns]
    except:
        pass
    drop_columns.append(y_column)
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

    X = X.values
    y = y.values

    return X, y

def scale_features(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std = [x if x != 0 else 0.00000001 for x in std]
    X = (X - mean) / std
    return X, mean, std

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def gradient_descent(X, y, parameters, alpha, num_iters):
    m = len(y)
    for _ in range(num_iters):
        h = sigmoid(X.dot(parameters))
        gradient = (1 / m) * X.T.dot(h - y)
        parameters -= alpha * gradient
    return parameters

def predict(X, parameters):
    probabilities = sigmoid(X.dot(parameters))
    return np.argmax(probabilities, axis=1)

def print_predictions(X, y, parameters, label_map):
    predictions = predict(X, parameters)
    predictions = [label_map[label] for label in predictions]
    wrong = 0
    
    for i in range(len(y)):
        print(f"prediction {i + 1}: {predictions[i]}, target value: {y[i]}")
        if (y[i] != predictions[i]):
            wrong += 1
    print(f"Amount wrong: {wrong}")
    
    return predictions

def classification(filename, y_column=None, drop_columns=None, alpha=0.01, num_attempts=100000):
    X, y = load_data(filename, y_column, drop_columns)
    X, mean, std = scale_features(X)
    m, n = X.shape

    unique_classes = np.unique(y)
    num_classes = len(unique_classes)
    
    label_map = {i: species for i, species in enumerate(unique_classes)}
    parameters = np.zeros((n + 1, num_classes))

    for i, cls in enumerate(unique_classes):
        binary_y = (y == cls).astype(int)
        X_train = np.hstack((np.ones((m, 1)), X))
        parameters[:, i] = gradient_descent(X_train, binary_y, parameters[:, i], alpha, num_attempts)
    
    predictions = print_predictions(X_train, y, parameters, label_map)

    return X, y, parameters, predictions, label_map, mean, std

def predict_values_classification(input, filename, mean, std, parameters, label_map, y_column=None, drop_columns=None):
    input_scaled = load_data(filename, y_column, drop_columns, True, input)
    input_scaled = (input_scaled - mean) / std
    m = input_scaled.shape[0]
    input_scaled = np.hstack((np.ones((m, 1)), input_scaled))

    predictions = predict(input_scaled, parameters)
    predictions = [label_map[label] for label in predictions]

    for i in range(len(predictions)):
        print(f"Prediction for {input[i]}: {predictions[i]}")
    return predictions