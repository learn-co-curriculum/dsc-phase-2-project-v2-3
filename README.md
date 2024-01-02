## Kings County Real Estate Insights House-Sales-Prices-Analysis-Using-Multi-Linear-Regression
![WhatsApp Image 2024-01-02 at 8 49 28 PM](https://github.com/Rgmoogachiri/dsc-phase-2-project-v2-3/assets/45751215/c526c43b-b8c9-4622-a078-68cc4bb0678a)

## BUSINESS STAKEHOLDER
### Rittenhouse Brothers - Real Estate Flipping Company

## INTRODUCTION

This study aims to address the importance of identifying the factors that significantly influence home costs, Because conventional methods rely on anecdotal evidence or limited research, they often yield incorrect findings. This knowledge gap makes it more difficult for stakeholders to predict and assess changes in house prices. To solve this issue, we are using multiple regression modeling techniques to thoroughly analyze home sales data. Multiple regression is a useful tool for analyzing the relationship between different attributes and home sales prices since it takes into consideration the combined impact of several independent variables.


## PROBLEM STATEMENT

Real estate valuation poses significant challenges for Rittenhouse Brothers, particularly when determining property values influenced by unique features and the impact of renovations or upgrades. The subjective nature of valuation, varying interpretations among appraisers and professionals, and the absence of a purely objective methodology contribute to valuation discrepancies.

## MAIN OBJECTIVE

This Analysis aims to establish an objective property valuation model, focusing specifically on Property's Unique features and the impact of renovations or upgrades. The primary goal is to minimize variations in valuation estimates and provide Rittenhouse Brothers with a more standardized and reliable method for assessing property values.

## SPECIFIC OBJECTIVES

Perform exploratory data analysis to uncover connections between various variables and the target variable. This process aids in identifying pertinent variables for inclusion in a regression model.

Create a multiple regression model to forecast house sale prices by taking into account chosen independent variables and examining their influence on the dependent variable. Validate the model assumptions, evaluate its fitness for the data, and refine the model as needed.

Analyze the coefficients of the independent variables within the model to discern their contributions to house prices. Identify the most impactful factors influencing house sale prices and delineate their respective effects.

Assess and confirm the efficacy of the model.

Offer practical insights and recommendations derived from the analysis to aid Rittenhouse Brothers in making well-informed decisions related to property investment.


## NOTEBOOK STRUCTURE
1. Reading the data.
2. Data cleaning and preprocessing.
3. Data Analysis
4. Multiple Regression Modelling.
5. Model Evaluation and Understanding
   
## BUSINESS UNDERSTANDING

The insights from regression analysis empower real estate professionals to grasp the forces behind house prices. This knowledge allows agents to refine price estimates, spotlight essential property features, and offer knowledgeable advice to clients. Similarly, homeowners and sellers can utilize this analysis to appraise their property's potential worth. Understanding influential features helps them gauge the impact of enhancements on property value, guiding their decisions on pricing and marketing tactics.


## DATA UNDERSTANDING

The dataset used here contains housing-related information, encompassing variables like date, square footage above ground level (sqft_above), property view indicators, and basement square footage (sqft_basement). An exploratory analysis will examine missing values, validate data types, identify outliers, and extract pivotal features for analysis. This process aims to thoroughly comprehend the dataset's intricacies, laying the groundwork for a comprehensive understanding of factors influencing housing prices. Through meticulous scrutiny, this analysis endeavors to ensure data integrity, facilitate informed decision-making, and enable accurate modeling in the realm of housing price determination.

## METHODOLOGY

The methodology lays out a clear plan to analyze using multiple regression modeling. It helps manage the data properly, choose the right factors, build the model, and check if it works well. This way, we get trustworthy and accurate insights into what things affect how much houses are sold for.

## RESULTS AND INTERPRETATION

Based on the correlation matrix, correlation heatmap, and the model results for the standardized data, the square foot living variable is the single most significant variable in affecting house prices, then followed by a view based on our model.

For houses with an average 'sqft_living', 'floors', 'condition', and 'view', the house price is about 540,500 dollars. A unit increase in square feet of sqft_living leads to a $253.5 increase in house price. While our models explain 54.3 percent of the variability in house prices, its error increases with increasing house prices as seen in the residual plot

## RECOMENDATIONS & CONCLUSIONS
1. Further to no.3 above, more analysis is required to show how the geographical location of a house affects its price
2. Ways to improve the accuracy, especially for high-value homes, so we can provide even more reliable estimates across the entire range of house prices are needed.
3. Market Segmentation: To determine market segmentation or particular buyer preferences, examine the link between the independent factors and housing prices. For example, a market sector of luxury or high-end homes may be indicated if the prices of houses tend to be higher.
