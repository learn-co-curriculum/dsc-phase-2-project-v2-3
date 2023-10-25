# Predicting House Prices

This multiple linear regression project was completed as part of Moringa School Data Science Bootcamp (Phase 2 Final Project).

## Problem statement
Sometimes investors know how certain metrics and attributes affect house pricing, but they are not sure to what extent the metrics affect the pricing. Additionally, there are a combination of factors that affect the overall pricing of the houses. Unfortunately, the investors also cannot tell how the different combinations may affect the house pricing. They struggle to decide how much to price the houses based on the different combinations, and the random assumption may lead to overpricing or underpricing of the units

## Components

* **Jupyter Notebook**
The [Jupyter Notebook](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/main/student.ipynb) is our key deliverable and contains details of our approach and methodology, data cleaning, exploratory data analysis and model building and validation.

I recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the Jupyter Notebook.

* **Presentation**
The [presentation](https://) gives a high-level overview of our approach, findings and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

* **Data**

The dataset can be found in the file *"kc_house_data.csv"* in the Data folder, in this repository. It was originally provided in the following [repository](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/main/data/kc_house_data.csv). 

## Technologies/ Packages

* Python version: 3.6.9
* Matplotlib version: 3.1.3
* Seaborn version: 0.9.0
* Pandas version: 0.25.1
* Numpy version: 1.16.5
* Statsmodels version: 0.10.1
* Scikit-learn version: 0.21.2  

## To get started

1. Clone this repository - [guidance](https://help.github.com/articles/cloning-a-repository/).
2. Dataset can be found in the file "kc_house_data.csv".
3. Check requirements in Technologies section above and download libraries if necessary.

## Data Wrangling
Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling

## Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data vizualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

Most houses are priced around a half million to a million dollars,
while the most expensive houses imply the order of two million dollars and more

**Overview of house features**
- it is can be noticed that as `bedrooms` increase, so does the house's selling price
- more `floors`, preferably up to 2.5 have a higher price  

## Simple Linear Regression Model
### OLS Regression Results

Here we have the outcome of an Ordinary Least Squares (OLS) linear regression analysis performed on a dataset with 'price' as the dependent variable and 'sqft_living' as the independent variable. 

R² is approximately 0.495
F-Statistic the high value (1.868e+04) suggests that the model is statistically significant.
Intercept The estimated value of 'price' when 'sqft_living' is 0. The coefficient is approximately -47,430.
sqft_living (Coefficient for sqft_living): approximately 283.1303.


## Multiple Linear Regression Model
RMSE is approximately 186,325.31.
R-squared (R²) is approximately 0.738





