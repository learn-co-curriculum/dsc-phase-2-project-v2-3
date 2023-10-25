# Phase 2 Project - Prediction of House Prices in King County, WA

## Overview

Through this project, we are setting out on a mission to provide homeowners with a thorough awareness of the factors that influence housing pricing. This initiative is a joint venture with our shareholder, a well-known real estate company committed to helping homeowners navigate the complex home-buying and selling process.

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

Initally, the columns that were deemed surplus to requirements were dropped. These columns are: `date, view, lat, long, sqft_living15` and `sqft_loft15`.

## Modeling

## Evaluation
