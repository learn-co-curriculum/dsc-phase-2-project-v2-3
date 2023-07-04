# KING COUNTY HOUSING PROJECT 
* Presented by;
    • Beatrice Kirui
    • Cliff Shitote
    • Winfred Muthoni
    • Leornard Rotich
    • Brian Kabugih

![DALL·E 2023-04-19 05.32.45](https://github.com/WinnieKabuya/dsc-phase-2-project-v2-3/blob/main/DALL%C2%B7E%202023-04-19%2005.32.45%20-%20picture%20of%20housing%20estates%20in%20the%20US.png) 

## Project Overview

This project aims to use data science techniques to analyze house sales in North Western County

### Business Problem

The Real Estate Agency aims to provide advice to homeowners about how home renovations might increase the estimated value of their homes, and by what amount.

### The Data

We'll be using the King County House Sales dataset.

The dataset contains:
1. Sale price
2. Condition
3. Grade
4. Number of bedrooms
5. Number of floors

## Data Cleaning and EDA

Minimal data cleaning was required, however there was a need to manage missing values,  duplicates, and outliers.
The exploratory data analysis(EDA) sought answers to the following questions:

    How does price vary with the month sold?
    Does the age of the house affect it's price?
    How does viewing a house affect price?
    Which factors are most correlated with price?

This picture shows the home sale prices within our first time home buyers criteria by the season the house was sold. The seasons are split between spring , summer , fall  and winter. 

![seasons output.png](https://github.com/Leon380/dsc-phase-2-project-v2-3/blob/main/seasons%20output.png)

We see that prices start rising from spring to summer and start dropping during summer to spring

![relationship between Age and price output.png](https://github.com/Leon380/dsc-phase-2-project-v2-3/blob/main/relationship%20between%20Age%20and%20price%20output.png)

There is a relationship between the age of the house and its price. Specifically, the analysis may have found that newer houses tend to be more expensive than older houses, all other things being equal. This could be because newer houses are typically in better condition and have more modern amenities than older houses.

![Viewing a house vs the price.png](https://github.com/Leon380/dsc-phase-2-project-v2-3/blob/main/Viewing%20a%20house%20vs%20the%20price.png)

Also in the above plot we see that the number of times a house was viewed may have increased the proce of the house since the number of views means potential customers and increases the chances of the house being sold compared to the houses with little or no views.

Based on the questions you provided, here are some possible answers that the exploratory data analysis (EDA) may have found:

    How does price vary with the month sold?
    There is a seasonal effect on the home sale prices, with prices being higher during certain months and lower during others. For example, the analysis may have found that prices tend to be higher in the spring and summer months when the weather is better and people are more likely to be interested in buying a house. On the other hand, prices may be lower in the winter months when there are fewer buyers in the market.

    Does the age of the house affect its price?
    There is a relationship between the age of the house and its price. Specifically, that newer houses tend to be more expensive than older houses, all other things being constant. This could be because newer houses are typically in better condition and have more modern amenities than older houses.

    How does viewing a house affect price?
    The number of times a house is viewed by potential buyers is positively correlated with its sale price. In other words, the more people view a house, the more likely it is to sell for a higher price. This could be because more interest in a property can create a sense of competition among buyers, which drives up the price.

    Which factors are most correlated with price?
    Certain factors are more strongly correlated with the sale price of a house than others. For example, the size of the house (measured in square feet) may be strongly correlated with the sale price, with larger houses selling for higher prices. Other factors that may be strongly correlated with price include the location of the house (e.g., proximity to schools or public transportation), the number of bedrooms and bathrooms, and the condition of the house.

  ## Modeling and Predictions
  !https://github.com/WinnieKabuya/dsc-phase-2-project-v2-3/blob/main/Ols%20regression.png
  
Overall the model performed marginally better. We were off by about 149171 rather than 173560 in a given prediction, and explained 62.9% rather than 49.2% of the variance in price.
  
  !https://github.com/WinnieKabuya/dsc-phase-2-project-v2-3/blob/patch-1/Residual%20QQ%20plot%20output.png
  
  Since almost all of the data points fall along a straight line in this QQ-plot, we can consider the normality assumption satisfied.
 
  !https://github.com/WinnieKabuya/dsc-phase-2-project-v2-3/blob/patch-1/Residual%20scatterplot%20output.png
  
The scatterplot appears to show a roughly symmetrical and consistent spread of the residuals around the lowess regression line, suggesting that the homoscedasticity assumption is met for the Model.

  **Regression results**
Model 1:The p_value  are zero therefore  less than the of 0.05 therefore the model is statistically significant

Model 2:The model explains about 58.1% of the variance in price.
The p_value  are zero therfore  less than the of 0.05 therefore the model is statistically significant

Final- model:The model explains about 63% of the variance in price which is an improvement from the previous model.

  ## Conclusion
  The creation of these models will enable the Real Estate Agency to provide precise valuations of residential properties to their customers. Moreover, by comprehending the aspects that significantly affect the selling price, the agency can suggest homeowners on how to boost their home's worth via enhancements or modifications. Overall, this venture can furnish meaningful understandings about the determinants that sway the sale price of a house in King County, benefiting both the Real Estate Agency and their clientele.

