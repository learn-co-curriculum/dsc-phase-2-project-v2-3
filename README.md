## Project Overview

This project aims to provide valuable insights for a real estate agency operating in King County, Washington, USA. Specifically, the agency seeks to provide accurate advice to homeowners on how different factors such as number of bedrooms and bathrooms,sqft-living,sqft-lot,floors,waterfront,house condition, grade and year built  can potentially affect the estimated value of their properties and homes, and by how much. This information will help the agency guide their clients towards making informed decisions considering such factors, which can maximize their return on investment when selling their properties.

## Introduction

The goal of this project is to conduct extensive research on the real estate market in King County in order to explore the potential of renovating specific areas of a property to increase its value and make it more attractive to potential buyers. This approach can help homeowners to add functionality and beauty to their property while simultaneously boosting its resale value
To achieve this objective, we will employ multiple linear regression modeling to analyze house sales data in the King County area. By using statistical techniques, we aim to identify key factors that impact property sales in the region and provide valuable insights to guide our recommendations.
The first sections focus on investigating, cleaning, wrangling, and engineering some new features. The next section contains 2 models and evaluation of each, ultimately leading us to select our best model for predicting house prices thhat will maximize profit. Finally, we will make recommendations and provide insight on house features that have the biggest impact on sale price to a team of real estate agents that are looking to get into the business of remodeling houses.

## Problem statement

The problem at hand is to provide homeowners with accurate advice on how the named factors can impact the estimated value of their properties and homes, and the amount by which it can increase. This information is crucial for the real estate agency to guide their clients towards making informed decisions which in return will help homeowners to maximize their return on investment when selling their properties. Therefore, the primary objective of this project is to analyze the impact of the above named factors on the estimated value of properties and provide recommendations that can help the real estate agency and their clients to make sound investment decisions.

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

## Objectives
Our objectives for the project are as follows:

1 To create a complex model using several different independent variables that can swifty and effectively achieve pricing estimates closer to realized housing 
  prices
2 To evaluate different models that ultimately lead to selecting our best model for predicting house prices
3 To provide insight on house features that have the biggest impact on sale price

## Rationale:

In choosing statistical analyses over basic data visualization, we opt for a more nuanced understanding of the intricate relationships within our dataset. While graphs offer visual representation, regression coefficients provide precise quantification of each feature's impact on house prices. This level of detail is paramount in the complex realm of real estate, where numerous factors converge to determine property values. Through regression analysis, we can discern subtle effects and interactions, offering a comprehensive assessment for our data science audience. Our modeling process was guided by these statistical insights, ensuring the model's accuracy and effectiveness.        

## Results:

In our final scaled model, we have achieved an R-squared value of 0.491, which indicates that approximately 49.1% of the variation in house prices can be explained by the selected features. This represents a slight improvement in model performance compared to previous iterations.

Among the key features, "grade" and "sqft_living" have the most positive impact on sale price, suggesting that investing in improving the quality of the house and increasing its living space could potentially lead to higher resale values. However, it's crucial to note that the impact of some features, such as "bathrooms" and "bedrooms," appears to be negative, which means that simply adding more of these features may not necessarily increase the resale value.

## Limitations

Limitations of this model include the fact that it still relies on simplified linear relationships between features and house prices. It doesn't capture all the nuances and interactions that could exist in the real estate market. Additionally, while the R-squared value has improved, there's room for further refinement.

## Recommendations

Stakeholders looking to remodel houses and maximize resale value should consider that this model provides valuable insights into feature importance but may not account for external factors or market dynamics that can influence pricing. To achieve the best results, they should continue to gather local market information, consult with real estate experts, and consider other factors like location and market demand when making renovation decisions. Ultimately, a holistic approach that combines data-driven insights with market expertise will lead to the most profitable post-renovation strategy.
