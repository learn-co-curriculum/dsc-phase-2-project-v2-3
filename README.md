# Phase 2 Project For Group 7

The following are the group members that completed the project
* Abdihakim S Mohamed
* Jennifer Njeri
* Caleb Ochieng
* Bedan Njoroge

## Project Overview

For this project, you will use multiple linear regression modeling to analyze house sales in a northwestern county.

### Business Problem

Our data analysis project addresses a pressing issue in King County's real estate market: increasing home values. We aim to dissect the King County Sales dataset to provide actionable insights for homeowners. We explored house design's impact on sale values, analyzed the relationship between dimensions and prices, assessed numeric and categorical variables, and evaluated location's role in pricing. Our goal is to empower homeowners to make informed decisions and enhance their property values in this dynamic market.

### The Data

The data in this project comes from King County of Washington State. The county includes both Seattle and Bellevue, so we're looking at a large number of houses - over 21K. The dependent variable in this analysis will be home prices.

To help predict the price, we will be using the following explanatory variables:

* Rooms
* Square footage in each house, and the square footage of the houses' 15 closest neighbors
* Year built
* Year renovated (if applicable)
* Condition (overall condition of the house)
* Grade (overall grade given to each house by the King County Grading System)
* Zipcode
* Latitude and longitude
* Using these variables, and others we create, we will attempt to create a quality model (defined by satisfying the assumptions of linear regression, a high R2, and a low root mean squared error) that can accurately predict the price of a house and also provide clarity into how different variables affect the price.



### Method
Our data frame starts has 21,597 pieces of data. We cleaned the data accordingly, taking out null values when necessary and dropping irrelevant columns. Once our data frame was complete, we performed log transformations, standardization, and normalization techniques to get more accurate coefficients. We tested for multicollinearity in order to remove features that overlapped. Afterward, we built our model, reflected on the results, and made adjustments accordingly. And repeat


## Results
#### Histogram 
![Hist](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/9d9c3f1a-10c6-4936-8254-bd6c0a837990)

#### Heatmap to visualize the correlation between all the variables.
![Heatmap](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/7e7f0069-27c4-4179-855f-3e8242b4780e)

#### Normality Assumption (for the Baseline Model)
![Nomality](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/c931cd59-823b-49f2-a25d-3117de2c1b37)

#### Price vs square feet living area
![price](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/e409c754-39e8-4d2c-a96d-b18d90f2351e)

#### The effect of all variables on the sale value of the houses.
![coef](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/0e903d3f-0395-480f-9857-a31e756160f2)

#### Multicollinearity on Price and Zipcode
![model](https://github.com/EngCS254/dsc-phase-2-project-v2-3/assets/133906913/350f8939-951b-4180-b007-c470c67483b9)

Observation: Our regression model above showed strong multicollinearity between one or more predictor variables. This can affect the reliability and interpretability of the results.


### Conclusion
* After conducting an extensive analysis of our dataset, it becomes evident that the Ordinary Least Squares (OLS) regression model emerges as a highly effective choice. This is substantiated by its impressive R-squared value of 0.801, signifying its ability to account for approximately 80.1% of the variance in property prices accurately. The OLS model's exceptional predictive prowess underscores its reliability.

* While we initially encountered challenges related to multicollinearity among specific predictor variables, we proactively addressed this concern through the strategic use of Ridge and Lasso regularization techniques. This proactive approach significantly improved the overall stability and performance of our model. Additionally, the Ridge regression model, one of the regularization methods employed, exhibited an outstanding R-squared score of 0.002478465766104665, reaffirming its precision in predicting property prices. Simultaneously, the Lasso regression model demonstrated favorable results with a low Mean Squared Error (MSE) of 0.002478465252112816, further affirming the effectiveness of our strategy

*  In conclusion, we confidently recommend maintaining our reliance on the OLS regression model. Its consistent alignment with our objective of establishing a dependable predictive tool for property price estimation is underscored by its robust performance, augmented by regularization techniques. These findings not only elevate the quality of our analysis but also empower our organization to make well-informed, data-driven decisions that drive overall success.


### Recommendations
* We find that the conclusion makes a compelling case for using the Ordinary Least Squares (OLS) regression model, especially given its high R-squared value. However, we believe there are areas for enhancement. For instance, we suggest clarifying the disparity between the R-squared values of the OLS and Ridge models, especially if the lower value for Ridge is not a typographical error.

* Additionally, we recommend providing more details on how multicollinearity was managed using Ridge and Lasso regularization, including their impact on the predictor variables. Incorporating information on cross-validation methods used, and possibly discussing statistical measures like p-values or confidence intervals, would add depth to the analysis.

* Lastly, while the conclusion states that the OLS model aligns well with organizational objectives, We think it would be beneficial to specify its practical applications. This could involve outlining the types of decisions the model could influence and suggesting directions for future research to make the recommendations more actionable. Overall, these refinements would make the conclusion even more robust and comprehensive.








