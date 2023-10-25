def calculate_vif(df, target_variable):
    """
    Calculate the Variance Inflation Factor (VIF) for each independent variable in a dataframe.

    Parameters:
        df (DataFrame): The input dataframe containing the independent variables.
        target_variable (str): The name of the target variable.

    Returns:
        vif_data (DataFrame): A dataframe containing the variables and their corresponding VIF values.
    """
    # Separate the target variable
    independent_vars = df.drop(columns=[target_variable])

    vif_data = pd.DataFrame()
    vif_data["Variable"] = independent_vars.columns
    vif_data["VIF"] = [variance_inflation_factor(
        independent_vars.values, i) for i in range(independent_vars.shape[1])]

    # Handle cases with high VIF values (you can choose a threshold) by setting VIF to NaN
    threshold = 5  # You can adjust this threshold based on your analysis
    vif_data.loc[vif_data["VIF"] > threshold, "VIF"] = np.nan

    return vif_data


# Example usage:
vif_results = calculate_vif(df, target_variable="price")
print(vif_results)
