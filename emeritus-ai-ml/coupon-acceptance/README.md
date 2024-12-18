# Data Exploration for Coupon Acceptance Possibility by Drivers for Restaurants While Driving


## **Overview**

The goal of this project is to use what you know about visualizations and probability distributions to distinguish between customers who accepted a driving coupon versus those that did not.

**Data**

This data comes to us from the UCI Machine Learning repository and was collected via a survey on Amazon Mechanical Turk. 
The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. 
Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’.  
There are five different types of coupons -- less expensive restaurants (under \\$20), coffee houses, carry out & take away, bar, and more expensive restaurants (\\$20 - $50).

**Steps**
Data is loaded into pandas dataframe and Seaborn library is used for plotting. Count plot is generated for each dependent variables against the target variable, which is "0" or "1": 1 means coupon will be accepted and 0 means not accepted.

**Findings**
Based on the count plots the variables are analysed for the impact and findings are shared. 
Here are the findings from the Exploratory Data Analysis and plots. Here are some factors that can increase acceptances.
- Coupons with 1 day expiration has higher chance of acceptance.
- Restaurant "less than $20" or "Carry Out" restaurants have higher chances of acceptance
- Sunny and warmer temperatures have higher rates of acceptance
- Drivers driving alone or with friends have accepted more
- Time 6 pm and 2 pm are more favorable to accept coupons by drivers

**Recommendations**
Next step is to build a model. A classification model can be used to predict "Y" based on features e.g. Logistic Regression.
Split the data into train and test data sets and train the model on the training set. 
