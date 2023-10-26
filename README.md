# House Price Forecasting with Regression Modeling

![King County, Washington](https://github.com/Wairimukimm/dsc-phase-2-project-v2-3/blob/main/king_county.jpeg)


## Problem statement
Real estate developers encounter difficulties when assessing the precise influence of individual metrics and attributes on house pricing within the KC housing dataset. Their primary concern is the degree to which these factors interact to affect pricing outcomes. The current lack of clarity in pricing decisions can result in instances of both overpricing and underpricing of properties. And to address this issue, we aim to develop a more comprehensive understanding of the dataset's variables, enabling them to make more accurate pricing decisions based on a combination of factors.

## PROJECT OVERVIEW 
The project focuses on the creation of a machine-learning project for house-price forecasting for investors to owners to buyers.

## BUSINESS UNDERSTANDING
House price forecasting is a crucial task in the real estate industry. Accurate predictions assist homebuyers, sellers, and investors in making informed decisions regarding property transactions.

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

## 1. Data Wrangling
Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling

## 2. Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data vizualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

Most houses are priced around a half million to a million dollars,
while the most expensive houses imply the order of two million dollars and more

**Overview of house features**
- Categorical features of the house include `id`, `date`, `bedrooms`, `floors`, `waterfront`, `view`, `grade`, `year_built`, `yr_renovetd`, `zipcode`, `lat`, `long`.
- Numerical variables include `price`, `sqft_living`, `sqft_lot`, `sqft_above`, `sqft_basement`, `sqft_basement`, `sqft_living_above`, `sqft_lot_below`.
- it is can be noticed that as `bedrooms` increase, so does the house's selling price
- more `floors`, preferably up to 2.5 have a higher price  

## 3. Simple Linear Regression Model
### OLS Regression Results

Here we have the outcome of an Ordinary Least Squares (OLS) linear regression analysis performed on a dataset with 'price' as the dependent variable and 'sqft_living' as the independent variable. 

- R² is approximately 0.495
- F-Statistic the high value (1.868e+04) suggests that the model is statistically significant.
- Intercept: The estimated value of 'price' when 'sqft_living' is 0. The coefficient is approximately -47,430.
- sqft_living (Coefficient for sqft_living): approximately 283.1303.


## 4. Multiple Linear Regression Model
### OLS Regression Results
- RMSE is approximately 186,325.31.
- R-squared (R²) is approximately 0.719
- The high F-statistic value (6096) suggests that the model is statistically significant.

### Random Forest Regression Results
- The RMSE is 125,563 which is lower meaning the model is more accurate
- The R² is 88%


## Conclusions
In conclusion, our predictive model accounts for approximately 72% of the variance in house prices which signifies a strong predictive power. The factors considered include, square footage, location, view and waterfront, which have a substantial impact on property values. It's important to keep in mind, however, that real estate is influenced by many more dynamic variables thus achieving 100% accuracy in predicting house prices is challenging. Our model’s performance is encouraging and can aid in estimating property values in King County thus providing a reliable method for both buyers and sellers. 
Although this model is reliable, it should be used in conjunction with other information for more precise pricing decisions.


## Contributors:
|Name     |  GitHub   |
|---------|-----------------|
|Priscillah Wairimu |https://github.com/Wairimukimm|
|Lewis Kamindu |https://github.com/lewigi|
|Brian Chacha |https://github.com/MarwaBrian|
|Meshael Oduor |https://github.com/Ayangaoduor1|
|Lucy Waruguru |https://github.com/WacekeW|
|Stephen Butiya |https://github.com/obystephen|







