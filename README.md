## Project Overview

This project aims to provide valuable insights for a real estate agency operating in King County, Washington, USA. Specifically, the agency seeks to provide accurate advice to homeowners on how home renovations can potentially affect the estimated value of their properties and homes, and by how much. This information will help the agency guide their clients towards making informed decisions on home renovations, which can maximize their return on investment when selling their properties.

## Introduction

The goal of this project is to conduct extensive research on the real estate market in King County in order to explore the potential of renovating specific areas of a property to increase its value and make it more attractive to potential buyers. This approach can help homeowners to add functionality and beauty to their property while simultaneously boosting its resale value.

To achieve this objective, we will employ multiple linear regression modeling to analyze house sales data in the King County area. By using statistical techniques, we aim to identify key factors that impact property sales in the region and provide valuable insights to guide our recommendations.

The first sections focus on investigating, cleaning, wrangling, and engineering some new features. The next section contains 2 models and evaluation of each, ultimately leading us to select our best model for predicting house prices that will maximize profit. Finally, we will make recommendations and provide insight on house features that have the biggest impact on sale price to a team of real estate agents that are looking to get into the business of remodeling houses.

## Business Problem

A group of real estate agents are looking to expand their business into renovating houses in addition to selling. They need guidance on assisting clients with recommendations on which home renovations may increase the estimated value of their homes. They want to accurately predict the value of homes based on the features of the house so they can maximize profits for their remodels. In order to accomplish this, they have enlisted our help in building a model to predict the price of homes in the county.

Objectives:

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

model1 = model(X_train,X_test,y_train,y_test);
Train R2:  0.5930690032174879
Test R2:  0.5846682459099573
Train RMSE:  237521.44455420846
Test RMSE:  223472.84687545706
OLS Regression Results
Dep. Variable:	price	R-squared:	0.593
Model:	OLS	Adj. R-squared:	0.593
Method:	Least Squares	F-statistic:	3146.
Date:	Sun, 10 Sep 2023	Prob (F-statistic):	0.00
Time:	05:05:17	Log-Likelihood:	-2.3836e+05
No. Observations:	17276	AIC:	4.767e+05
Df Residuals:	17267	BIC:	4.768e+05
Df Model:	8		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
Intercept	-6.505e+05	1.84e+04	-35.284	0.000	-6.87e+05	-6.14e+05
bedrooms	-4.209e+04	2586.958	-16.272	0.000	-4.72e+04	-3.7e+04
bathrooms	-1.081e+04	3983.539	-2.714	0.007	-1.86e+04	-3004.189
sqft_living	216.4590	3.961	54.648	0.000	208.695	224.223
sqft_lot	-0.4135	0.045	-9.252	0.000	-0.501	-0.326
floors	-2.208e+04	4088.337	-5.400	0.000	-3.01e+04	-1.41e+04
waterfront	8.419e+05	2.25e+04	37.499	0.000	7.98e+05	8.86e+05
condition	5.971e+04	2901.930	20.577	0.000	5.4e+04	6.54e+04
grade	1.039e+05	2561.007	40.566	0.000	9.89e+04	1.09e+05
Omnibus:	12569.877	Durbin-Watson:	1.996
Prob(Omnibus):	0.000	Jarque-Bera (JB):	723771.545
Skew:	2.928	Prob(JB):	0.00
Kurtosis:	34.164	Cond. No.	5.48e+05

### Baseline model Interpretation 
The dependent variable being predicted is "price," which is the house price.

-The model's R-squared value (0.593) indicates how much of the variance in the target variable (house prices) is explained by the features. An R-squared of 0.593 is relatively good but suggests that there may still be room for improvement.

-The model's adjusted R-squared is the same as the R-squared in this case, meaning there are no penalties for the inclusion of additional features.

-The F-statistic (3146) and its associated p-value (0.00) suggest that the model, as a whole, is statistically significant.

-The coefficients (coef) for each feature represent how much the predicted price changes with a one-unit change in that feature, assuming all other features are constant. For example, a one-unit increase in square footage of living space (sqft_living) corresponds to an increase in predicted price of 216.4590 units, holding all other variables constant.

-The p-values associated with each coefficient indicate their statistical significance. In this case, most coefficients have p-values less than 0.05 (usually considered significant), except for "bathrooms" (p-value = 0.007), which suggests that the number of bathrooms might have a weaker effect on house prices in this model.



## Results:

In our final scaled model, we have achieved an R-squared value of 0.491, which indicates that approximately 49.1% of the variation in house prices can be explained by the selected features. This represents a slight improvement in model performance compared to previous iterations.

Among the key features, "grade" and "sqft_living" have the most positive impact on sale price, suggesting that investing in improving the quality of the house and increasing its living space could potentially lead to higher resale values. However, it's crucial to note that the impact of some features, such as "bathrooms" and "bedrooms," appears to be negative, which means that simply adding more of these features may not necessarily increase the resale value.

## Limitations

Limitations of this model include the fact that it still relies on simplified linear relationships between features and house prices. It doesn't capture all the nuances and interactions that could exist in the real estate market. Additionally, while the R-squared value has improved, there's room for further refinement.

## Recommendations

Stakeholders looking to remodel houses and maximize resale value should consider that this model provides valuable insights into feature importance but may not account for external factors or market dynamics that can influence pricing. To achieve the best results, they should continue to gather local market information, consult with real estate experts, and consider other factors like location and market demand when making renovation decisions. Ultimately, a holistic approach that combines data-driven insights with market expertise will lead to the most profitable post-renovation strategy.
