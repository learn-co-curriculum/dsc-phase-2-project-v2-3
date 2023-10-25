# Phase 2 Project - Prediction of House Prices in King County, WA

## Overview

Through this project, we are setting out on a mission to provide homeowners with a thorough awareness of the factors that influence housing pricing. This initiative is a joint venture with our shareholder, a well-known real estate company committed to helping homeowners navigate the complex home-buying and selling process.

<div style='text-align:center'>
  <img src='./images/king_country.jpg'/>
</div>

## Business Understanding

Many people want to buy properties in the vibrant King County, Washington, real estate market. Unfortunately, these prospective customers frequently have to navigate the market in blindness due to the constant information asymmetry. Our goal is to provide a reliable approach for estimating home values so that potential buyers can make educated decisions about their real estate investments. We will do this by providing priceless advisory services to a respectable real estate company that supports families in their quest of homeownership.

### Problem Statement

In the ever-changing King County, Washington, real estate market, potential purchasers frequently encounter difficulties in trying to comprehend the many aspects that influence residential property values. Due to this knowledge gap, homeowners and prospective purchasers may find it difficult to navigate the housing market without a thorough understanding of the major factors that affect property values. People thus find it difficult to make wise choices while purchasing, disposing of, or making investments in real estate.

### Objectives

Our primary objective is to find out how independent factors affect a home's pricing.

1. To evaluate the correlations between independent variables and house prices are the specific objectives.
2. To Examine How Differently Correlated Variables Affect Home Prices.
3. To Create a Sturdy Multilinear Regression Model for Forecasting Home Prices.

## Data Understanding

One dataset was provided and used for this analysis.

The process of data understanding begins with describing the raw dataset - through the help of pandas - by:

- Mentioning the shape of the dataframe (_21507 rows_ and _21 columns_).
- Viewing the data types of the columns, as well as the columns that may have null values (`yr_renovated`, `waterfront` and `view`).
- Generating descriptive statistics for all the columns.
- Understanding what columns could have erroneous/duplicate/null values and formulating a way to deal with them.

## Data Preparation

To clean the dataframe, removal of erroneous and null data as well as handling of duplicate data was done.

Initally, the columns that were deemed surplus to requirements were dropped. These columns are: `date` and `yr_renovated`. An important point of clarification is that **other columns can be dropped at a later stage if deemed necessary**.

Furthermore, records will null values were dropped as well, before converting string-based columns to equivalent integers for easier analysis. Among the columns that were replaced were the `condition` and `waterfront` columns, before splitting the values in the `grade` column to comprise only of numerical ratings rather than a mixture of integers and text.

Lastly, it was noted that in the `sqft_basement` column, 415 records were using a question mark as a placeholder value. As we do not know what the appropriate values for the records with the placeholder value would be, and any attempt at replacing the values would distort the study, these records were dropped.

## Modeling

### EDA

A positively skewed distribution was noticed when looking at the distribution of prices in the dataset.

<div style='text-align:center'>
  <img src='./images/positive_skew.png'/>
</div>

The other columns were then copmarede to the price as seen in the figure below. Some variables, such as `bedrooms` and `floors` were noted to be discrete variables while others were continuous.

<div style='text-align:center'>
  <img src='./images/all_vars.png'/>
</div>

### Impact of Grade of a House on Pricing

## Evaluation
