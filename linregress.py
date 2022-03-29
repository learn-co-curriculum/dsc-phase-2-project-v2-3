import pandas as pd
import numpy as np
import datetime as dt
from sklearn import metrics
from sklearn import linear_model
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def linearly_regress(y, X):
    """
    Create a linear regression model from predictors X and dependent variable y
    Returns a tuple containing the model and metrics about the models (R Squared, MAE, RMSE)
    """
    lr = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    lr.fit(X_train, y_train)
    r_squared = lr.score(X_train, y_train)

    y_pred = lr.predict(X_test)
    MAE = mean_absolute_error(y_pred, y_test)
    RMSE = np.sqrt(mean_squared_error(y_pred, y_test))
    
    return (lr, r_squared, MAE, RMSE)


def model_averages(y_model, X_model, y_predict, X_predict, n):
    """
    Creates n models on X_model for y_model and gets n predictions based for X_predict
    Returns a np array of average results over n models
    """

    results_df = pd.DataFrame(y_predict)
    for count in range(n):            
        results_df[str(count)] = linearly_regress(y_model, X_model)[0].predict(X_predict)

    results_df['averages'] = results_df.mean(axis = 1)

    return results_df
