# KING COUNTY HOUSING PROJECT 
* Presented by;
    • Beatrice Kirui
    • Cliff Shitote
    • Winfred Muthoni
    • Leornard Rotich
    • Brian Kabugih

!DALL·E 2023-04-19 05.32.45 - picture of housing estates in the US.png

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

!seasons output.png

We see that prices start rising from spring to summer and start dropping during summer to spring

!relationship between Age and price output.png

Here we see that the age of a house has no relationship with the price of the house

!Viewing a house vs the price.png

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
  !OLS regression results.png
  !Residual QQ plot output.png
  !Residual scatterplot output.png

  **Regression results**

  ## Conclusion
  The creation of these models will enable the Real Estate Agency to provide precise valuations of residential properties to their customers. Moreover, by comprehending the aspects that significantly affect the selling price, the agency can suggest homeowners on how to boost their home's worth via enhancements or modifications. Overall, this venture can furnish meaningful understandings about the determinants that sway the sale price of a house in King County, benefiting both the Real Estate Agency and their clientele.

