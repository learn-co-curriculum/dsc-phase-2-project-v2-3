

BUSINESS UNDERSTANDING:

Stakeholder: Real Estate Agency


BUSINESS PROBLEM:

The real estate agency aims to provide advice to homeowners on how home renovations can increase the estimated value of their homes and by what amount. The agency wants to identify the factors that contribute most significantly to the increase in house prices after renovations. By understanding these factors, they can guide homeowners in making informed decisions about renovations that will yield a higher return on investment.


DATA UNDERSTANDING:

The dataset used for this analysis is the King County House Sales dataset. It contains information about various features of houses in a northwestern county, including the price of the house, the number of bedrooms and bathrooms, square footage measurements, condition, grade, year built, presence of a waterfront, and other relevant details.

The available columns in the dataset are as follows:

•	id: A property identification number

•	date: Date of transaction

•	price: Price of the house

•	bedrooms: Number of bedrooms

•	bathrooms: Number of bathrooms

•	sqft_living: Square footage of the living space

•	sqft_lot: Square footage of the lot

•	floors: Total floors in the house

•	waterfront: Whether the house is on a waterfront (1: yes, 0: no)

•	view: Special view

•	condition: Condition of the house

•	grade: Grading level around the house

•	sqft_above: Square footage of the house apart from the basement

•	sqft_basement: Square footage of the basement area

•	yr_built: Year when the house was built

•	yr_renovated: Year when the house was renovated

•	zipcode: Zip code of the house

•	lat: Latitude coordinate of the house

•	long: Longitude coordinate of the house

It is important to note that some features such as date, view, sqft_above, sqft_basement, yr_renovated, zipcode, lat, and long may not be relevant for this analysis and could be excluded from the modeling process.

THE GOAL:

The goal of the analysis is to build a multiple linear regression model that can predict the impact of home renovations on the estimated value of houses. By identifying the significant predictors, the real estate agency can provide homeowners with actionable recommendations on which renovations are most likely to yield a higher return on investment.

