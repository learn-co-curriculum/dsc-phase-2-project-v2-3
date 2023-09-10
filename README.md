## Project Overview

This project aims to provide valuable insights for a real estate agency operating in King County, Washington, USA. Specifically, the agency seeks to provide accurate advice to homeowners on how home renovations can potentially affect the estimated value of their properties and homes, and by how much. This information will help the agency guide their clients towards making informed decisions on home renovations, which can maximize their return on investment when selling their properties.

## Introduction

The goal of this project is to conduct extensive research on the real estate market in King County in order to explore the potential of renovating specific areas of a property to increase its value and make it more attractive to potential buyers. This approach can help homeowners to add functionality and beauty to their property while simultaneously boosting its resale value.

To achieve this objective, we will employ multiple linear regression modeling to analyze house sales data in the King County area. By using statistical techniques, we aim to identify key factors that impact property sales in the region and provide valuable insights to guide our recommendations.

The first sections focus on investigating, cleaning, wrangling, and engineering some new features. The next section contains 3 models and evaluation of each, ultimately leading us to select our best model for predicting house prices that will maximize profit. Finally, we will make recommendations and provide insight on house features that have the biggest impact on sale price to a team of real estate agents that are looking to get into the business of remodeling houses.

## Business Problem

A group of real estate agents are looking to expand their business into renovating houses in addition to selling. They need guidance on assisting clients with recommendations on which home renovations may increase the estimated value of their homes. They want to accurately predict the value of homes based on the features of the house so they can maximize profits for their remodels. In order to accomplish this, they have enlisted our help in building a model to predict the price of homes in the county.

**Objectives:**

To provide insight on house features that have the biggest impact on sale price

To create a complex model using several different independent variables that can swifty and effectively achieve pricing estimates that may increase the estimated value of their homes

To evaluate different models that ultimately lead to selecting our best model for maximizing profit after renovation

## Data Understanding

This data originates from the King County House Sales dataset, accessible through the King County Open Data platform. The dataset contains information on single-family home sales spanning from 2014 to 2015.

 The aspects we will be examining are as follows:
 
1 price - sales price

2 bedrooms - Number of bedrooms

3 bathrooms - Number of bathrooms

4 sqft_living - Square footage of living space in the home

5 sqft_lot - Square footage of the lot

6 floors - Number of floors (levels) in house

7 waterfront - whether the house is on a waterfront

8 grade - Overall grade of the house. Related to the construction and design of the house

9 yr_built - Year when house was built

10 condition - How good the overall condition of the house is. Related to maintenance of house


## Rationale:

In choosing statistical analyses over basic data visualization, we opt for a more nuanced understanding of the intricate relationships within our dataset.
While graphs offer visual representation, regression coefficients provide precise quantification of each feature's impact on house prices. This level of detail is paramount in the complex realm of real estate, where numerous factors converge to determine property values. Through regression analysis, we can discern subtle effects and interactions, offering a comprehensive assessment for our data science audience. Our modeling process was guided by these statistical insights, ensuring the model's accuracy and effectiveness.     

## Modelling

## Baseline model
For this model, we created a model with all features to serve as our baseline.

![baseline model](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/7c247e7f-5fcd-4ca5-a95a-f265df7b9a7d)

##### Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.48e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

### Baseline model Interpretation 
The dependent variable being predicted is "price," which is the house price.

-The model's R-squared value (0.593) indicates how much of the variance in the target variable (house prices) is explained by the features. An R-squared of 0.593 is relatively good but suggests that there may still be room for improvement.

-The model's adjusted R-squared is the same as the R-squared in this case, meaning there are no penalties for the inclusion of additional features.

-The F-statistic (3146) and its associated p-value (0.00) suggest that the model, as a whole, is statistically significant.

-The coefficients (coef) for each feature represent how much the predicted price changes with a one-unit change in that feature, assuming all other features are constant. For example, a one-unit increase in square footage of living space (sqft_living) corresponds to an increase in predicted price of 216.4590 units, holding all other variables constant.

-The p-values associated with each coefficient indicate their statistical significance. In this case, most coefficients have p-values less than 0.05 (usually considered significant), except for "bathrooms" (p-value = 0.007), which suggests that the number of bathrooms might have a weaker effect on house prices in this model.

### Baseline Model Visualization

#### Assumptions Check

![baseline model image 1](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/21fb14da-4c16-4035-bc0c-1f0a82ab32c5)

![baseline model image 2](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/99c9d3eb-c623-401e-8e93-4cd0837512d0)

## Model 1 - Remove Outliers from Price

The interquantile range (IQR) is the difference between the 75th (q75) and 25th percentiles (q25) of the data, therefore the middle 50% of the data. 1.5 multiplied by the IQR is a common way to identify and remove outliers that are less than q25 - (1.5 * IQR) and greater than q75 + (1.5 * IQR). I chose to remove outliers this way instead of 3 * std because the data was not normally distributed in the variables I was removing outliers from.

![model 1 ](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/17979b55-c038-461c-913c-5bce617354be)

##### Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.71e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

#### Interpretation

Overall, while the R-squared value has decreased slightly, the model's predictive accuracy has improved as indicated by lower RMSE values. This means that our model may provide more accurate price predictions, which can be valuable for our business stakeholders when making real estate decisions. However, it's essential to keep refining and iterating on the model to further enhance its performance.

### Model 1 visualizations

![model 1 visuals](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/67002417-588f-43eb-999c-20bfd2f20787)


## Model 2- Remove Outliers from Predictors

![model 2 ](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/071613cb-8a89-4b10-a1bc-a1199e4f928c)

##### Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.07e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

#### Interpretation

Overall, although the R-squared has decreased slightly, our model's predictive accuracy has improved, as evidenced by lower RMSE values. This suggests that our model may provide more accurate price predictions, which can be highly valuable for our business stakeholders in making informed real estate decisions. We should continue to monitor and refine our model to achieve the best possible results.

### Model 2 visualizations

![model 2](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/7363d6b7-6023-4fb4-b51e-1921e25ae3d4)

![model 2](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/7430f875-ecc1-4660-99ad-e10823fd95a5)

## Model 3 - Log Transformation

![model 3](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/0feeb006-df7f-4954-aac1-f7948b8c5ebc)

##### Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.51e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

#### Interpretation 

R2 was 0.458, we have improved in this model to 0.491. Train RMSE: 186,658.29; Test RMSE: 182,969.03. Higher RMSE from ~143,000. Difference between train and test RMSE is acceptable. Model is not overfittted. Distibution of residuals is close to normal, still have some light tails indicating that errors are likely for extreme values. Homoscedasticity has greatly improved! Homes on the lower end now are more overpredicted, but due to the fact that we want a wide range of prices in our model it is acceptable. Even though our RMSE has increased, this is our best performing model because it passes the assumptions of regression.

### Model 3 visualizations

![model 3 visuals](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/cbffbbae-5f61-43c2-88bb-6ffab0e75c3e)


![model 3 visuals](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/0a47c504-af33-4ddf-8e28-4eb6a49a6bd0)


## Scale the Final Model

To determine which features have the most impact on sale price, I will update my model fuction to scale the data using Standard Scaler. This will allow us to compare the effects of each feature on a level playing field.

![final model ](https://github.com/elizabethnyambura/dsc-phase-2-project-v2-3/assets/136367890/f15305e2-7a1f-4ea8-ba01-ce4dc7b6521a)

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
model6.params.sort_values(ascending=False).head(50)

Intercept      12.991108

grade           0.197454

sqft_living     0.187173

condition       0.069224

waterfront      0.039226

floors          0.010650

bathrooms      -0.014737

bedrooms       -0.032194

dtype: float64

Features with the most impact on sale price ranked. The features with the most positive impact on sale price in relation to renovation are grade and sqft_living

## Results:

1.In our final scaled model, we have achieved an R-squared value of 0.491, which indicates that approximately 49.1% of the variation in house prices can be explained by the selected features. This represents a slight improvement in model performance compared to previous iterations.

2.The Root Mean Squared Error (RMSE) values for both the training and test datasets have decreased as well. The training RMSE is approximately 186,658.39, and the test RMSE is approximately 182,969.03. These lower RMSE values suggest that our model's predictions are more accurate and closer to the actual sale prices of houses.

3.Among the key features, "grade" with a coeff of 0.197 and "sqft_living" with a coeff of 0.187 have the most positive impact on sale price, suggesting that investing in improving the quality of the house and increasing its living space could potentially lead to higher resale values. However, it's crucial to note that the impact of some features, such as "bathrooms" and "bedrooms," appears to be negative, which means that simply adding more of these features may not necessarily increase the resale value.

## Limitations

Limitations of this model include the fact that it still relies on simplified linear relationships between features and house prices. It doesn't capture all the nuances and interactions that could exist in the real estate market. Additionally, while the R-squared value has improved, there's room for further refinement.

## Recommendations

In the final model with all features excluding sqft_lot, our model's performance based on the adjusted R-squared improved from 0.458 to 0.491. Meaning that 41.9% of the variation of the price variable within the data is explained by our model. In the final model, all features included in the model have statistical significance relationship with price. All p-values are less than 0.05.

**Coefficient Interpretations:**

For every increase in the grade of a home, it increases the price of a home by 19.7% For every square foot of living added to a home, it increases the price of a home by 18.7% For every increase in condition to a home, it increases the price of a home by 6.9% For every floor added to a home, it increases the price of a home by 1.0% For every bathroom added to a home, it decreases the price of the home by 1.4% For every bedroom added to a home, it decreases the price of the home by 3.2%

**Conclusions for King County Real Estate Agents:**

1.In order to maximize the price of a home, you should recommend to your clients that they should use great quality products when rennovating their home to increase the grade of their home to highest possible level.

2.If the seller is wanting to expand the size of their home, creating another floor is a great option to increase the price of their home.

3.Improving the condition of your home to a minimum, average condition, will increase your home's value by 6.9%.

## Next Steps
1.Add more features to our model to see the affects on adjusted R-squared.

2.Create a similar tool for buyers as well that helps them decide what to offer, or what they can likely negotiate down to for a fair price
