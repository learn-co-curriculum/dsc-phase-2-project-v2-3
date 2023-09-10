# Unlocking Insights in Real Estate:
## A Regression Analysis of House Sales Trends in King County
---

> Project Contibutors:
>Elsie Ochieng,
>Richard Taracha,
>Cindy King'ori,
>Peter Muthoma


> Date: 06/09/2023

![cutomer churn header](https://raw.githubusercontent.com/GayasuddinMohd/House-Price_Prediction/main/House%20Image.avif)

---

### Table of Contents
- [Introduction and Business Understanding](#Introduction-and-Business-Understanding)
- [Data Preparation and Preprocessing](#project-deliverable)
- [Exploratory Data Analysis](#recording-the-experimental-design)
- [Regression Modeling](#summary-of-findings)
- [Results and Findings](#summary-of-findings)
- [Conclusion](#challenging-your-solution)
- [References](#challenging-your-solution)

---

## Introduction and Business Understanding

If you want to work for a top company in Seattle, you might be curious about how much it costs to live in King County. This is the largest and most populated county in Washington State, where Seattle and its suburbs are located. About 10 Fortune 500 Companies have their headquarters here, such as Starbucks, Nordstrom, Alaska Airlines, Costco, Expedia, Microsoft, and Amazon. Microsoft and Amazon are among the Big Five tech companies that many people aspire to join.

But finding a house in King County is not easy. There are many factors that affect the price, such as the number of bedrooms, bathrooms, and floors. You might have a different preference than someone else. Wouldn't it be nice if you could estimate the price of your ideal house based on the features you want? That way, you could plan ahead and make your dream house a reality.

Therefore in this data science project, we embark on a journey to analyze house sales data in King County. Our goal is to uncover valuable insights that can aid stakeholders in making informed decisions in the real estate market.

The real estate agency we are partnering with faces a critical challenge: how to provide homeowners with guidance on home renovations that can enhance the estimated value of their properties. To address this problem, we will leverage multiple linear regression modeling to explore the relationships between various features and house sale prices.


#### Technologies and Tools

- Python
- Pandas
- Numpy
- Matplotlib
- Scikit-Learn

#### Project Deliverable
- A non-technical presentation
- A Jupyter Notebook
- A GitHub repository

---

## Data Preparation and Preprocessing

In this phase, we focus on ensuring that our dataset is well-prepared and suitable for analysis by doing the following:

1. **Data Loading:**
      * We began by loading the dataset from the provided kc_house_data.csv file using Python's Pandas library.

2. **Handling Missing Data:**
      * Identified and addressed missing values in certain columns, such as "waterfront," "view," and "yr_renovated."  to ensure data quality.

3. **Feature Engineering:**
      * Created new features, including date-related attributes and a binary "is_renovated" column to indicate whether a property has been renovated.



---

## Exploratory Data Analysis


---
## Regression Modeling
#### Regression Modelling -Multiple Linear Regression using Ordinary Least Squares (OLS)

1. Interpreting the Model Metrics
    * **R-squared:** This is 0.695, which means that about 69.5% of the variance in the dependent variable (price) can be explained by the independent variables in the model.
    * **F-statistic and Prob (F-statistic):** The F-statistic tests whether at least one predictor variable has a non-zero coefficient. A low p-value (here, 0.00) rejects the null hypothesis that all predictor coefficients are zero, meaning at least some predictors are significant.
    * **P>|t|:** This is the p-value associated with each predictor. A small p-value (typically ≤ 0.05) indicates strong evidence that the predictor is a meaningful addition to the model. For example, bedrooms, bathrooms, sqft_living, floors, waterfront, view, condition, grade, yr_built, lat, long, and year are all statistically significant predictors. However, day and day_of_week have p-values greater than the alpha value making them statistically insignificant predictors
    * **Condition Number:** The condition number is large (3.11e+08), indicating potential issues with multicollinearity or other numerical problems.
    * **Coefficients:** These values represent the change in the dependent variable for a one-unit change in the respective predictor, assuming all other predictors are held constant. For instance, for every additional bedroom (bedrooms), the price decreases by approximately $34,710.
    * **Intercept:** -1.04e+08, which means that if all other predictors (like bedrooms, bathrooms, sqft_living, etc.) are zero, the predicted price of a house would be -1.04e+08.

However, in practice, the intercept often doesn’t have a meaningful interpretation, especially when it doesn’t make sense to have all predictors be zero (like in this case, a house cannot have zero bedrooms or zero square footage). It’s more useful in adjusting the model’s predictions to the scale of the dependent variable. It’s also worth noting that the p-value for the intercept is less than 0.05, indicating that it is statistically significant in this model.

2. Communicating Results - Residual Plots
     * The points in the residual plot are randomly dispersed around the horizontal axis, but a granular pattern is not obvious hence a nonlinear model maybe more appropriate for the research question.

3. Communicating Results - QQ Plot
     * The data points fall above or below the line, meaning the data is not normally distributed.
  
4. Communicating Results - Test for Heteroskedasticity
     * We see that a lot of values are scattered around the mean while a fairly large amount are spread further apart from the mean, meaning that there are no obvious patterns. We performed a test for heteroscedasticity to be certain. We will used Bartlett's Test to test the null hypothesis that the variances in this dataset are homogeneous (equal)
     * This is a hypothesis test that establishes a null hypothesis that the variance is equal for all our data points,and the alternative hypothesis is that at least one of the variances is different.
     * The test uses the chi-squared distribution to calculate the test statistic and make a decision about the null hypothesis.
     * 
**Test statistic = 1538.5317150354024**
**p-value = 0.0**
**We reject the null hypothesis because the variances are unequal**

---
## Results and Findings

1. The price (target) has many outliers, and it is positively skewed, which makes it hard to generate a proper model to predict the price.
2. From EDA, we understand several key findings:
     * The living square footage is highly correlated with the price.
     * The grade is highly correlated with the price
     * The number of bathrooms positively correlated with the price.
     * The view also determines the price.
     * Usually, the neighborhood has a similar size of the living space.
     * Houses that have been renovated can sell slightly higher than the houses that are yet to be renovated.
  
3. Our model has room for improvement. Its R2 score is 0.63. This is not a poor result, considering that we are dealing with real world data that has a lot of noise. However, this also implies that the selected input features, cannot account for more than 40% of the variation in housing prices. The linear model would not be suitable model for the specific question as the residuals are not normally distributed.

---

## Recommendations
The company should come up with a solution that caters to customers who make two or more calls to customer service. They should also collect more data, preferably those that will make the current dataset more balanced, e.g., more customers from Area Codes 408 and 510, more customers who churned, and more customers subscribed to the international plan.

[Back To The Top](#Customer-Churn-Predicition--Classification-Analysis)

---

## Conclusion




