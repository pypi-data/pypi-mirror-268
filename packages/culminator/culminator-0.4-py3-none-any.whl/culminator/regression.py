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

def split(X, y, train=0.6, cv=0.2, test=0.2):
    if abs(1.0 - train - cv - test) > 0.000001:
        raise Exception("Train, cv, and test must add up to 1")
    
    zipped = list(zip(X, y))
    np.random.shuffle(zipped)
    X, y = zip(*zipped)
    X = np.array(X)
    y = np.array(y)

    split1 = int(len(X) * train)
    split2 = int(len(X) * cv) + split1

    X_train = X[:split1]
    X_cv = X[split1 : split2]
    X_test = X[split2:]
    y_train = y[:split1]
    y_cv = y[split1 : split2]
    y_test = y[split2:]

    return X_train, X_cv, X_test, y_train, y_cv, y_test

def generate_polynomial_features(X, degree):
    n_samples, n_features = X.shape
    X_poly = np.ones((n_samples, 1))
    for degree in range(1, degree + 1):
        for i in range(n_features):
            X_poly = np.hstack((X_poly, np.power(X[:, i:i+1], degree)))
    return X_poly

def estimate_parameters(X, y, alpha=0.1):
    n = X.shape[1]
    I = np.eye(n)
    return np.linalg.inv(X.T @ X + alpha * I) @ X.T @ y

def mse(y, yhat):
    m = len(y)
    mse = 0.0
    for i in range(m):
        mse += (y[i] - yhat[i]) ** 2
    mse /= 2 * m
    return mse

def predict(X, parameters):
    return X @ parameters

def optimize_degree(X, y, max_degree, num_iters=50, train=0.6, cv=0.2, test=0.2, alpha=0.1):
    err_train = np.zeros((max_degree, num_iters))
    err_cv = np.zeros((max_degree, num_iters))
    err_test = np.zeros((max_degree, num_iters))

    for i in range(num_iters):
        X_train, X_cv, X_test, y_train, y_cv, y_test = split(X, y, train, test, cv)
        for degree in range(1, max_degree + 1):
            try:
                X_train_poly = generate_polynomial_features(X_train, degree)
                X_cv_poly = generate_polynomial_features(X_cv, degree)
                X_test_poly = generate_polynomial_features(X_test, degree)
                parameters = estimate_parameters(X_train_poly, y_train, alpha)
            except:
                err_train = err_train[:degree - 1]
                err_cv = err_cv[:degree - 1]
                err_test = err_test[:degree - 1]
                break

            y_train_pred = predict(X_train_poly, parameters)
            y_cv_pred = predict(X_cv_poly, parameters)
            y_test_pred = predict(X_test_poly, parameters)

            err_train[degree-1, i] = mse(y_train, y_train_pred)
            err_cv[degree-1, i] = mse(y_cv, y_cv_pred)
            err_test[degree-1, i] = mse(y_test, y_test_pred)

    err_train = np.mean(err_train, axis=1)
    err_cv = np.mean(err_cv, axis=1)
    err_test = np.mean(err_test, axis=1)
    return err_train, err_cv, err_test

def create_regression(X, y, degree, alpha=0.1, num_attempts=100, train=0.6, cv=0.2, test=0.2):
    best_parameters = np.array([])
    best_mse = float("inf")
    for _ in range(num_attempts):
        average_mse = 0.0
        X_train, X_cv, X_test, y_train, y_cv, y_test = split(X, y, train, cv, test)
        X_train_poly = generate_polynomial_features(X_train, degree)
        parameters = estimate_parameters(X_train_poly, y_train, alpha)
        
        for _ in range(num_attempts):
            X_train, X_cv, X_test, y_train, y_cv, y_test = split(X, y, train, cv, test)
            X_cv_poly = generate_polynomial_features(X_cv, degree)
            y_cv_pred = predict(X_cv_poly, parameters)
            average_mse += mse(y_cv, y_cv_pred)
        
        average_mse /= 10
        if average_mse < best_mse:
            best_parameters = parameters
    
    return best_parameters

def print_predictions(X, y, degree, parameters, round_digits=None):
    X_poly = generate_polynomial_features(X, degree)
    predictions = predict(X_poly, parameters)
    if round_digits != None:
        predictions = [round(prediction, round_digits) for prediction in predictions]

    avg_err = 0.0
    for i in range(len(y)):
        print(f"prediction {i + 1}: {predictions[i]}, target value: {y[i]}")
        avg_err += abs(predictions[i] - y[i])
    
    avg_err /= len(y)
    print(f"Average error: {avg_err}")
    return predictions

def regression(filename, y_column=None, drop_columns=None, train=0.6, cv=0.2, test=0.2, max_degree=10, alpha=0.1, num_iters=50, num_attempts=100, round_digits=None):
    X, y = load_data(filename, y_column, drop_columns)
    X, mean, std = scale_features(X)
    err_train, err_cv, err_test = optimize_degree(X, y, max_degree, num_iters, train, cv, test, alpha)
    optimal_degree = np.argmin(err_cv) + 1
    parameters = create_regression(X, y, optimal_degree, alpha, num_attempts, train, cv, test)
    predictions = print_predictions(X, y, optimal_degree, parameters, round_digits)
    return X, y, optimal_degree, parameters, predictions, mean, std

def predict_values_regression(input, filename, mean, std, degree, parameters, y_column=None, drop_columns=None, round_digits=None):
    input_scaled = load_data(filename, y_column, drop_columns, True, input)
    input_scaled = (input_scaled - mean) / std
    
    input_poly = generate_polynomial_features(input_scaled, degree)
    predictions = predict(input_poly, parameters)
    if round_digits != None:
        predictions = [round(prediction, round_digits) for prediction in predictions]

    for i in range(len(predictions)):
        print(f"Prediction for {input[i]}: {predictions[i]}")

    return predictions