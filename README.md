# Overview 
The aim of this project is to develop a Multiple Linear Regression Model to accurately predict the sale prices of houses in King County. Through careful data analysis and exploratory data analysis techniques, we will preprocess and clean the dataset to create a data frame for regression modeling. By analyzing key features such as square footage, number of bedrooms, location(waterfront or not), and more, we aim to uncover valuable insights that influence house prices.

# Business Understanding
Business understanding is essential for a real estate agency to effectively serve its clients. It serves as the foundation for successful operations and sustainable growth in the real estate industry. You need to understand the listing prices and how it affects buyers and sellers in making informed decisions. Identifying the expectations, preferences, and needs of the clients, and knowing what the clients want from the agency’s services, especially in terms of property evaluation is crucial.  Factors considered in the evaluation are:
* I.	Size and layout, the size of the property, the number of bedrooms and bathrooms, and the layout are crucial.
* II.	Condition, the property’s condition, including any need for repairs or renovations, can affect its value.
* III.	Location: The property location influences its value, factors like proximity to schools, parks, shopping malls, and transportation can impact the value
Gaining insight into the local housing market dynamics in the dataset such as the fluctuations in supply and demand, seasonality, and regional variations in property value is important.

# Main objective
* To develop a Multiple Linear Regression Model to accurately predict the sale prices of houses in King County
  
# Specif objective 
* Which features are identified as relevant for the Multiple Linear Regression Model, considering factors like size, layout, condition, and location?
* How do house prices vary concerning different features, such as square footage, the number of bedrooms, and location?
* How is the initial Multiple Linear Regression Model developed as a baseline?
* What is the outcome of the Exploratory Data Analysis in terms of understanding the distribution of key variables and relationships?
  

# Data understanding
The King County House Sales project dataset is stored in a file named kc_house_data.csv, accompanied by column descriptions available in column_names.md. It contains information relevant to house sales in King County, providing a comprehensive set of features. 
# Column Names and Descriptions for King County Data Set
* `id` - Unique identifier for a house
* `date` - Date house was sold
* `price` - Sale price (prediction target)
* `bedrooms` - Number of bedrooms
* `bathrooms` - Number of bathrooms
* `sqft_living` - Square footage of living space in the home
* `sqft_lot` - Square footage of the lot
* `floors` - Number of floors (levels) in house
* `waterfront` - Whether the house is on a waterfront
  * Includes Duwamish, Elliott Bay, Puget Sound, Lake Union, Ship Canal, Lake Washington, Lake Sammamish, other lake, and river/slough waterfronts
* `view` - Quality of view from house
  * Includes views of Mt. Rainier, Olympics, Cascades, Territorial, Seattle Skyline, Puget Sound, Lake Washington, Lake Sammamish, small lake / river / creek, and other
* `condition` - How good the overall condition of the house is. Related to maintenance of house.
  * See the [King County Assessor Website](https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r) for further explanation of each condition code
* `grade` - Overall grade of the house. Related to the construction and design of the house.
  * See the [King County Assessor Website](https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r) for further explanation of each building grade code
* `sqft_above` - Square footage of house apart from basement
* `sqft_basement` - Square footage of the basement
* `yr_built` - Year when house was built
* `yr_renovated` - Year when house was renovated
* `zipcode` - ZIP Code used by the United States Postal Service
* `lat` - Latitude coordinate
* `long` - Longitude coordinate
* `sqft_living15` - The square footage of interior housing living space for the nearest 15 neighbors
* `sqft_lot15` - The square footage of the land lots of the nearest 15 neighbors

To streamline the analysis, specific columns such as date, view, sqft_above, sqft_basement, yr_renovated, zip code, lat, long, sqft_living15, and sqft_lot15 can be excluded based on project recommendations. The dataset is the foundation for the primary project goal: regression modeling to predict house prices. Stakeholders are expected to be identified, and the analysis should address pertinent business problems, possibly involving advice for homeowners on how renovations impact home value. The modeling approach centers on linear regression, with a focus on building iterative models. The iterative process involves starting with a basic model, evaluating its performance, and then refining or iterating based on those evaluations. Evaluation metrics for overall model performance are required, and the project encourages the exploration of additional statistical techniques beyond linear regression if they contribute value. Clear documentation, transparency in decision-making, and, optionally, data visualization and analysis are emphasized for effective communication and reproducibility throughout the project.




# Recommendation and Conclusions

## Conclusions


## Recommendations


