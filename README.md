# Unlocking Insights in Real Estate:
## A Regression Analysis of House Sales Trends in King County
---

> Project Contributors:
>Elsie Ochieng,
>Richard Taracha,
>Cindy King'ori,
>Peter Muthoma


> Date: 06/09/2023

![cutomer churn header](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/Untitled%20design%20(6).jpg)

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
![The Price Hist](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/price_dist.png)
The column of interest was price. It had a right skewed distribution with a positive skewness value of 4.02 indicating that a small number of houses have significantly higher prices in comparison to the majority.

![Sqft_Living](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/sqft_dist.png)
The variable with the highest correlation to the prices of houses was sqft living which referred to the square footage of living space in the home.

The distribution was right skewed distribution with a positive skewness value of 1.47. This means that there are a few houses with very spacious living areas.

Other variables that we considered key to the pricing of homes were the number of bathrooms and number of bedrooms.

![Bed_rooms](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/avg_price_per_bedroom.png)

For bedrooms the trend was that houses with more bedrooms tend to fetch higher prices than those with few bedrooms.

![Bathrooms](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/avg_price_per_bathroom.png)

Houses with more bathrooms generally command higher prices. The trend is clear until around 6-7 bedrooms beyond which price variations become more scattered



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

![Sqft_Living](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/residual_plot.png)
- The points in the residual plot are randomly dispersed around the horizontal axis, but a granular pattern is not obvious hence a nonlinear model maybe more appropriate for the research question.

4. Communicating Results - QQ Plot
![SQQ](https://github.com/PeterMuthoma/dsc-phase-2-project-v2-3/blob/main/plots/qqplot.png)

-The data points fall above or below the line, meaning the data is not normally distributed.
  
6. Communicating Results - Test for Heteroskedasticity
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

## Conclusion

* All three models provide valuable insights into the factors affecting house prices.
* Model 2 has the highest R-squared value, indicating the best fit and explanatory power.
* The presence of multicollinearity is a concern in all models, especially in Models 2 and 3. Care should be taken when interpreting the individual variable effects.
* Normality assumptions of the residuals are not fully met, indicating that further exploration and refinement of the models may be necessary.
* Model 2, with a broader set of independent variables, provides the most comprehensive understanding of house price determinants.
* Further analysis, such as variable transformations or more feature engineering, may improve model performance and the ability to make accurate price predictions.

In summary, these models can be valuable tools for understanding and predicting house prices, but further refinement and consideration of multicollinearity and non-normality are recommended for more accurate predictions and insights.

---
## Recommendation

Based on the analysis of the three regression models and their respective coefficients, we can provide the following professional recommendations regarding the factors that significantly influence house prices:

1. **Square Footage of Living Space (sqft_living):** Across all three models, the square footage of living space consistently demonstrates a strong positive correlation with house prices. As such, when considering the purchase or valuation of a property, it is advisable to prioritize residences with larger living areas. Investing in properties with more extensive interior space is likely to yield a higher resale value.
2. **Grade:** Model 2 highlights the importance of the "grade" variable, which reflects the overall quality of a property. A higher grade is associated with significantly higher house prices. Therefore, when evaluating potential properties, it is wise to consider those with superior quality ratings. Investing in properties with higher grades is likely to result in greater long-term value appreciation.
3. **Waterfront View:** Model 2 also emphasizes the positive impact of a waterfront view on house prices. Properties with waterfront views command a substantial premium. Therefore, individuals seeking homes with potential for long-term value growth may wish to explore options with scenic waterfront vistas
4. **Latitude and Longitude:** Both latitude and longitude play significant roles in determining house prices in Model 2. Specific geographic locations are associated with higher or lower prices. Buyers and investors should take into account the desirability of a property's geographic coordinates, as these can affect its future value.
5. **Year Built:** Model 2 indicates that the year of construction can influence house prices. Older properties tend to have lower prices, while newer constructions command higher values. Buyers and investors should be mindful of a property's age and consider its potential for renovation or improvement to enhance its market value.
6. **Bathrooms and Floors:** Model 2 underscores the importance of the number of bathrooms and floors in influencing house prices positively. Properties with more bathrooms and multiple floors tend to have higher prices. Potential buyers should assess these attributes when making investment decisions.
7. **Condition:** Model 2 also highlights the significance of a property's condition in determining its price. Well-maintained properties with higher condition ratings generally command higher prices. Prioritizing homes in good condition can lead to more substantial long-term returns.
8. **Bedrooms:** While Model 2 suggests that the number of bedrooms may have a negative impact on price, it's essential to interpret this in context. The relationship between bedrooms and price may vary depending on other factors. Buyers should consider their specific needs and preferences regarding the number of bedrooms when selecting a property.
9. **Month and Day:** Model 2 includes variables related to the month and day of property transactions. While these variables may have a statistically significant impact, their practical significance may be limited. Buyers should focus on other more substantial factors when assessing property value.
10. **Day of the Week:** Model 2 shows that the day of the week of a transaction does not significantly influence house prices. Therefore, buyers need not be overly concerned about the specific day of the week when engaging in real estate transactions.

In conclusion, the factors that significantly affect house prices, as revealed by the three regression models, encompass square footage, grade, waterfront views, geographic location, year built, bathrooms, floors, condition, and the number of bedrooms. These findings should guide prospective buyers, sellers, and investors in making informed decisions to maximize the value of their real estate investments.

---

## Future Plans

#### Buyers:

1. **Define Your Goals:** Clarify your long-term goals for the property. Are you buying for personal use or investment? Knowing your objectives will help you make informed decisions.

2. **Budgeting:** Determine your budget, considering not only the purchase price but also potential renovation or improvement costs. Ensure your budget aligns with the type of property you're targeting.

3. **Prioritize Features:** Prioritize the features that matter most to you. If square footage is essential, focus on properties with larger living spaces. If quality matters, prioritize homes with higher grades.

4. **Location Matters:** Consider the geographic location carefully. Assess factors like proximity to schools, workplaces, amenities, and future development plans in the area.

5. **Property Condition:** Pay attention to the condition of the property. Well-maintained homes with higher condition ratings may require less immediate investment.

6. **Consult Real Estate Experts:** Engage with real estate agents and professionals who have local market knowledge. They can provide valuable insights and help you find the right property.

7. **Home Inspection:** Invest in a thorough home inspection to identify any hidden issues or needed repairs. This can help you negotiate a fair price.

8. **Financing:** Secure financing with favorable terms. Explore mortgage options, interest rates, and down payment requirements.

#### Sellers:

1. **Pre-Listing Preparation:** If you're selling a property, consider making necessary improvements to enhance its condition and appeal to potential buyers.

2. **Pricing Strategy:** Set a competitive yet realistic price for your property based on market conditions and the features it offers.

3. **Marketing:** Invest in professional marketing to showcase the property's strengths. High-quality photos and virtual tours can attract more buyers.

4. **Timing:** Be mindful of the timing of your listing. Consider market trends and seasons that may affect the demand for your property.

5. **Negotiation:** Be prepared for negotiations with potential buyers. Understand your property's value and be flexible when appropriate.

#### Investors:

1. **Diversification:** Consider diversifying your real estate portfolio by investing in properties with different features and in various locations.

2. **Market Research:** Continuously monitor real estate market trends and economic indicators that can affect property values.

3. **Property Management:** If investing in rental properties, implement effective property management practices to maximize returns and tenant satisfaction.

4. **Long-Term Strategy:** Align your investment strategy with your long-term financial goals. Real estate can be a valuable part of a diversified investment portfolio.

5. **Tax Planning:** Consult with tax professionals to optimize your tax strategy, taking advantage of deductions and incentives for real estate investors.

6. **Risk Management:** Mitigate risks associated with real estate investments by diversifying, conducting due diligence, and having contingency plans.

7. **Exit Strategy:** Plan your exit strategy, whether it's selling for capital gains, renting for passive income, or long-term holding for appreciation.

8. **Network:** Build a network of real estate professionals, including agents, contractors, and property managers, to support your investment endeavors.

In summary, the future plans and steps for buyers, sellers, and investors should be tailored to their specific goals and circumstances. Whether buying a home, selling a property, or investing in real estate, informed decisions and a well-thought-out strategy are essential for success in the dynamic real estate market.
