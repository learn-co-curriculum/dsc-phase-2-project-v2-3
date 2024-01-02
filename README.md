![image](https://github.com/PritcyVeke/dsc-phase-2-project-v2-3/assets/137262765/9364517c-0960-4ba3-95de-bd83f76e96ed)
Authors: TRIXIE CHEROP, EVALYNE MACHARIA, JOSEPHINE GATHENYA, LAURA MUTHEU, PRISCILLA VEKE, MERCY CHEROTICH.

Business Problem

Real estate is a highly dynamic market influenced by numerous factors.This makes it challenging for real estate investors to accurately predict house prices.

Inaccurate pricing models can lead to reduced profitability, missed opportunities, and dissatisfied customers.

The current pricing strategy of the real estate company is suboptimal, leading to potential loss of revenue and increased customer dissatisfaction.

Hence, the need of a robust predictive pricing model to enable companies stay competitive and adapt to market fluctuations.

Project Overview

This project is an attempt to help real estate investors make informed decision on what type of houses they should invest in.

This is in terms of the most impactful features, both positively and negatively, on House prices.

The components of the analysis include: Data preparation,Feature selection and Engineering, Model Development, Evaluation and Validation.

The Data

For this project, we use the King County House Sales dataset, which can be found in kc_house_data.csv in the data folder in this GitHub repository.
Methods

The methods used on the dataset include: Data Preparation, Feature selection and Engineering, Model Development, Evaluation and Validation.
Results

From the model created and analysis, we were able to note that:

i). The 'grade' feature has the greatest impact on house prices in general.

ii). Features with higher grade classiffication i.e grade_13 Mansion,grade_12 Luxury and grade_11 Excellent, have the most positive impact on house prices.

iii). Features with lower grade classification i.e grade_7 Average and smaller square footage above ground(log_sqft_above) ,have the most negative impact on house prices.

iv). Houses with a waterfront were highly priced compared to those without.

Conclusions

Based on the results obtained, the following conclusions were made:

1). Real estate investors seeking premium returns should consider the grade of the house.

2). Real estate investors should recognize the positive impact of larger living areas as indicated by the log_sqft_living variable to fetch higher returns.

3). Real estate investors should also consider waterfront views as they also positively impact house prices.

4). Investors should be mindful of features with a negative impact on house prices such as lower-grade classifications ("Average") and smaller square footage above ground(log_sqft_above).

For more information

Kindly check the Jupyter Notebook or review the presentation for moe information about the project.
