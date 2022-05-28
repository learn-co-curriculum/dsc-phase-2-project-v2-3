## Predicting housing values in King County based on home improvements

#### Below is an assessment for homeowners to increase their property value in King County, Washington.  I looked at the King County Washington housing dataset to build a model that will ascertain which aspects of property improvement would entice homeowners to put their houses on the market.  The goal is to find the ways that will best increase the property values for the homeowner.

##### Looking at the data we can see that it is comprised of 21 columns, all of which are relevant to home property values in King County, Washington.

![df info](https://user-images.githubusercontent.com/96254640/169474662-390fe75c-977e-45d7-ac44-d4ee6ee3ba03.PNG)

##### The dataset needed to be cleaned, as there were several items that needed transformed (objects) to be used in the set in a meaningful way.  Once those were cleaned, I was able to start removing outliers to check for correlations in price and the variables.

![gradesnip](https://user-images.githubusercontent.com/96254640/169477263-97eddaa0-d133-4925-94a4-04c20c476fe9.PNG)

##### Here we can see that there is a good correlation between the variable and price.  There were several variables that correlated well with price.  Many of the variables were dropped due to multicollinearity issues.  Other variables were dropped since they do not pertain to renovations homeowners could not perform.

![test](https://user-images.githubusercontent.com/96254640/169478944-df0eae51-c42a-4985-be97-da569627cfee.PNG)

#####  The final test represents 56% of the variability of price around its mean.  The null hypothesis is that there is no relationship between the price and the other variables.  Since the P-values for the variables were 0, we are able to reject the null hypothesis.  What I found was that increases grade, condition, and square footage of the living space gave the homeowner the best increase in value should they decide to upgrade these aspects of their property.  Other factors that were not taken into account but may have an effect on the values could be crime by location, local infrastructure, and proximity to amenities.
