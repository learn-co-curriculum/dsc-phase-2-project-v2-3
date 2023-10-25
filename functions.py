def fit_simple_linear_regression(df, dependent_variable, independent_variable):
    """
    Fits a simple linear regression model to the given dataframe.

    :param df: The pandas dataframe containing the data.
    :param dependent_variable: The name of the dependent variable column.
    :param independent_variable: The name of the independent variable column.

    :return: A tuple containing the root mean squared error (rmse),
      the mean absolute error (mae), and the model summary.
    """

    # Create and fit the simple linear regression model
    y = df[dependent_variable]
    X = df[independent_variable]
    X = sm.add_constant(X)  # Add a constant for the intercept
    model = sm.OLS(y, X).fit()

    # Calculate RMSE and MAE
    predictions = model.predict(X)
    residuals = y - predictions
    rmse = np.sqrt(np.mean(residuals**2))
    mae = np.mean(np.abs(residuals))

    # Get the model summary
    model_summary = model.summary()

    return rmse, mae, model_summary
