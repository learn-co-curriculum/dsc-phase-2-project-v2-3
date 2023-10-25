def fit_linear_regression(df, dependent_variable, independent_variables):
    """
    Fit a linear regression model to the given data.

    Args:
        df (pandas.DataFrame): The input dataframe containing the data.
        dependent_variable (str): The name of the dependent variable.
        independent_variables (list): The list of independent variables.

    Returns:
        tuple: A tuple containing the fitted model and its summary.

    Raises:
        None

    Example:
        >>> df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 4, 6]})
        >>> fit_linear_regression(df, 'y', ['x'])
        (model, model_summary)
    """
    if len(independent_variables) == 1:
        # Simple Linear Regression
        model_formula = f"{dependent_variable} ~ {independent_variables[0]}"
        model = ols(model_formula, data=df).fit()
    else:
        # Multiple Linear Regression
        X = df[independent_variables]
        X = sm.add_constant(X)  # Add a constant for the intercept
        y = df[dependent_variable]
        model = sm.OLS(y, X).fit()

    model_summary = model.summary()

    return model, model_summary


def model_metrics(df, dependent_variable, independent_variables):
    """
    Calculate the root mean squared error (RMSE) and mean absolute error (MAE) for a linear regression model.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.
    - dependent_variable (str): The name of the dependent variable column in the DataFrame.
    - independent_variables (list): A list of names of the independent variable columns in the DataFrame.

    Returns:
    - rmse (float): The root mean squared error.
    - mae (float): The mean absolute error.
    """
    # Create and fit the linear regression model
    X = df[independent_variables]
    X = sm.add_constant(X)  # Add a constant for the intercept
    y = df[dependent_variable]
    model = sm.OLS(y, X).fit()

    # Calculate RMSE
    y_pred = model.predict(X)
    rmse = (mean_squared_error(y, y_pred)) ** 0.5

    # Calculate MAE
    mae = mean_absolute_error(y, y_pred)

    return rmse, mae
