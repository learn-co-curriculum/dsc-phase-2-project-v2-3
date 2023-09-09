# Phase 2 Project Submission

![King County House Sales](https://github.com/angibor/dsc-phase-2-project-v2-3/assets/137016696/a6703f85-f879-4022-8651-33f10d6830ee)

## Project Overview

We conducted a comprehensive analysis of house sales data in a northwestern county using multiple linear regression modeling. Our goal was to gain insights into the factors that affect house prices and develop a predictive model that can estimate the value of homes based on various features.

## Business Problem

Weichert Realtors needs to provide valuable advice to homeowners regarding how home renovations may impact the estimated value of their homes and by what amount.

By addressing this problem, Weichert Realtors can offer valuable guidance to homeowners, strengthen their relationships with clients, and potentially increase their     
business.

Questions to answer:

1. What influence does the qualitative aspects of a house have on its sale price?
2. Is there a correlation between quantitative features and the selling price of a house?
3. What suggestions can be made to property investors seeking to optimize their returns from commercial real estate investments?

## Data Understanding
This analysis/modelling uses the King County House Sales dataset, which can be found in kc_house_data.csv in the data folder in this assignment's GitHub repository. The description of the column names can be found below;

* id - Unique identifier for a house
* date - Date house was sold
* price - Sale price (prediction target)
* bedrooms - Number of bedrooms
* bathrooms - Number of bathrooms
* sqft_living - Square footage of living space in the home
* sqft_lot - Square footage of the lot
* floors - Number of floors (levels) in house
* waterfront - Whether the house is on a waterfront
* view - Quality of view from house
* condition - How good the overall condition of the house is. Related to maintenance of house.
* grade - Overall grade of the house. Related to the construction and design of the house.
* sqft_above - Square footage of house apart from basement
* sqft_basement - Square footage of the basement
* yr_built - Year when house was built
* yr_renovated - Year when house was renovated
* zipcode - ZIP Code used by the United States Postal Service
* lat - Latitude coordinate
* long - Longitude coordinate
* sqft_living15 - The square footage of interior housing living space for the nearest 15 neighbors
* sqft_lot15 - The square footage of the land lots of the nearest 15 neighbors

More insights on the dataset;-
* Home prices range from 78,000 - 7,700,000
* The mean house price in the dataset is approximately $540,296.
* Most houses have between 3 and 4 bedrooms on average (mean of approximately 3.37)
* There is also a maximum of 33 bedrooms-(This could be an outlier or a data entry error.)
* The average number of bathrooms is approximately 2.12, with a range from 0.5 to 8 bathrooms per house.
* Most houses have 1.494 floors on average, with a minimum of 1 floor and a maximum of 3.5 floors.

NB: We confirmed that the 33 bedrooms is an outlier, using a boxplot.
![image](https://github.com/angibor/dsc-phase-2-project-v2-3/assets/137016696/3d19ce17-9406-4be8-b7d1-63d2e8119c15)

## Exploratory Data Analysis
1. We checked how the house price relate with continuous features by checking the following relationships.
   
* Relationship Between Price and Number of Bathrooms
* Relationship Between Price and Square footage of living space in the home
* Relationship Between Price and Square footage of house apart from basement
* Relationship Between Price vs Square footage of the basement
* Relationship Between Price vs Number of floors (levels) in house
* Relationship Between Price vs Square footage of the lot

2. We also checked how the house price relate with qualitative features.

* Relationship house views condition and price
* Relationship Between House condition and price
* Relationship Between house with waterfronts and price

1. Correlation of other features/variables with House Price
* We calculated the correlation matrix
* We got the correlation of 'price' with all other columns

![image](https://github.com/angibor/dsc-phase-2-project-v2-3/assets/137016696/2f20b3b5-5521-462b-9c0c-9121944101b1)

2. We checked the most correlated column feature with price?

3. We also checked What is the most correlated feature with other features excluding price.

#### Findings 
The most collerated feature with other features excluding price is 'sqft_living'. Since 'sqft_living' has two most auto-correlation with other features after price, we will drop it to avoid multicollinearity issues when modelling.

## Modeling and Regression Results

### 1. Baseline Model

#### Baseline Model Result
The linear regression model fitted above uses the 'grade' as the independent variable to predict the 'price' of houses. The R-squared value of 0.446 indicates that approximately 44.6% of the variance in house prices can be explained by the 'grade.' The coefficient for 'grade' is 209,200, suggesting that, on average, a one-unit increase in the 'grade' results in an increase of $209,200 in the house price. The constant term of -1,062,000 represents the estimated price when 'grade' is zero. The p-values are close to zero, indicating that the 'grade' is statistically significant in predicting house prices. The model fits the data well, although there might be some multicollinearity concerns, given the high coefficient value for 'grade.'

#### Baseline model predictive results.
![image](https://github.com/angibor/dsc-phase-2-project-v2-3/assets/137016696/143c0d5c-6337-4e02-b471-944dcc1b642c)

### 2. Multiple Linear Regression Models

#### a. Using Continuous data and Categorical features to build multiple regression models we did the following;-

#### i. Model Continuous features and grade column
#### Regression Results
The multiple linear regression model, including continuous variables (bedrooms, bathrooms, sqft_lot, sqft_basement, sqft_above, floors) and one categorical variable (grade), shows improved performance compared to the baseline. The R-squared value is 0.550, indicating that approximately 55% of the variance in price is explained by the model. Bedrooms, bathrooms, sqft_lot, sqft_basement, sqft_above, and the grade variable are statistically significant predictors of price, with associated coefficients showing their impact. However, multicollinearity may be a concern due to a high condition number.

#### ii. Model Continuous features and house condition feature
#### Regression Results
This second model, which includes the categorical variable condition along with continuous variables, shows an R-squared of 0.511, indicating 51.1% of price variance explained. All predictors are statistically significant. This model performs similarly to the previous one, suggesting condition may be a valuable predictor alongside the other features. THis model performs better than the baseline model.

### b. Model using only categorical features
#### Regression Results
The third model, using only categorical features (condition, waterfront, grade, view), has an R-squared of 0.525, explaining 52.5% of price variance. All categorical predictors are statistically significant below the chosen p_value of 0.05. This model simplifies the model significantly and performs competitively, suggesting that categorical features alone can provide valuable predictive power.

### c. Model using only continuous variables
#### Regression Results
The fourth model, utilizing only continuous variables, demonstrates an R-squared value of 0.584, indicating that 58.4% of the variance in price is explained. All continuous variables are statistically significant predictors of price. This model outperforms the previous models, suggesting that using only continuous features provides a strong predictive power for price. However, multicollinearity is a potential issue.

### d. Model using specific continuous variables
#### Regression Results
The fifth model, using specific continuous variables (bedrooms, bathrooms, sqft_lot, sqft_basement, sqft_above, floors), exhibits an R-squared value of 0.843, indicating a high explanatory power of 84.3%. All selected continuous variables are statistically significant. The model performs exceptionally well, but the absence of a constant term may affect its generalizability. Thus, we consider evaluating its performance on a validation dataset to ensure its validity given that this is the only model that has strongly fitted the data with high explanatory power of more than eighty percent. 

#### Predictive results of the fifth model.
![image](https://github.com/angibor/dsc-phase-2-project-v2-3/assets/137016696/6675213f-4732-45f0-8f2f-3514b77a5417)

## Conclusions and Recommendations
#### Conclusions
Qualitative Aspects: Qualitative aspects like the property's condition, grade, and view play a crucial role in determining home prices. Renovations that improve these aspects can lead to substantial increases in estimated property values.

Quantitative Features: Quantitative features such as the number of bedrooms, bathrooms, and total square footage are strongly correlated with home prices.

Significant Predictors: The regression models revealed that certain features strongly influence house prices. These include the number of bedrooms, bathrooms, square footage, condition, grade, and view. However, number of bedrooms, bathrooms, square footage of the lot, square footage of the basement, square footage of house apart from basement and Number of floors (levels) in house seemed to be the best in explaining the house prices.

#### Limitations
**Data Completeness:** The dataset did not cover all the features that influence house prices. For instance, the location or neighborhood of a property, local amenities, public transport accessibility, crime rates, or school quality can also play significant roles in determining prices.

**Data Quality:** There might be inconsistencies in the dataset that could have affected the results.

**Multicollinearity:** Features like 'sqft_living', 'sqft_above', and 'grade' might be correlated with each other, leading to multicollinearity. While we addressed this by removing 'sqft_living', other multicollinear variables might still be present. This can cause instability in regression coefficients, making interpretations difficult.

**Time Sensitivity:** House prices change over time due to economic, political, or environmental factors. The dataset did account for temporal aspects or trends in the housing market.

#### Recommendations:
Based on the analysis, several recommendations can be made to assist homeowners and Weichert Realtors:

Client Guidance: Weichert Realtors should provide clients with personalized guidance on home renovations and improvements. Explain how enhancing qualitative aspects like condition, grade and view can boost property values, and suggest specific renovations aligned with their goals.

Educational Resources: Develop educational resources and materials emphasizing the importance of specific renovations, such as increasing number of bedrooms, bathrooms, square footage of the lot, square footage of the basement, square footage of house apart from basement and Number of floors in house. Optimizing these features can lead to higher estimated home values.

Maximizing ROI with the right Renovation Strategies: Emphasize on the importance of quality. Ensure customers understand that renovations should be done to a high standard of quality. Quality renovations not only increase property value but also attract potential buyers or renters.

Marketing Strategies: Highlight unique property features, such as waterfront views or exceptional grades, in marketing materials. Showcasing these features contribute to higher property values.

Further Data Exploration: Exploring additional variables, such as location-related features or neighborhood characteristics, could provide deeper insights into price determinants. Proximity to schools, shopping centers, public transportation, parks, and the overall desirability of the neighborhood can greatly impact the price.

Risk Management: It's essential to acknowledge the potential for multicollinearity in the data, which can affect model accuracy. We recommend further research to mitigate this issue and ensure reliable predictions.

Advanced Modeling: Continue to invest in advanced modeling techniques and data analysis to refine pricing strategies and enhance predictive accuracy by taking into consideration the Market trends, Seasonal Variations and Economic Factors . This will ensure that clients receive the most accurate and up-to-date information.

Client Feedback: Encourage clients to provide feedback on their experiences and preferences. Use this feedback to further tailor services and recommendations to meet their individual needs.

By leveraging these insights and recommendations, Weichert Realtors can offer valuable guidance to homeowners, strengthen client relationships, and potentially increase business in the northwestern county real estate market.
