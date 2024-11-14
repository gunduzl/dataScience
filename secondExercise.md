Predicting Missing Values in a Dataset Using Linear Regression

This example demonstrates how to use a linear regression model to predict and fill missing values in a dataset. The dataset includes columns 'x', 'y', and 'z', where some values in 'z' are missing. We use the relationship between 'x', 'y', and 'z' to estimate and replace the missing values in 'z'.

Code

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create the dataset with some missing values in column 'z'

d = {'x': [2, 7, 8, 10, 15, 17, 30, 41], 'y': [4, 15, 17, 20, 24, 28, 41, 56], 'z': [8, 15, np.nan, 20, np.nan, np.nan, 35, np.nan]}
df = pd.DataFrame(data=d)

print("Initial Data:")
print(df)

# Drop rows with missing values in 'z' for training

df_m = df.dropna()
X = df_m.loc[:, df_m.columns != 'z']
y = df_m['z']

# Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train the linear regression model

LR = LinearRegression()
LR.fit(X_train, y_train)

# Identify rows where 'z' is missing for prediction

to_predict = df[df['z'].isna()]
print('\nRows with Missing Values in "z":')
print(to_predict)

# Predict missing values

print('\nPredictions for Missing Values:')
predictions = LR.predict(np.array(to_predict[['x', 'y']]))
print(predictions)

# Fill in the missing values in 'z'

to_predict['z'] = predictions
print('\nData with Filled Missing Values in "z":')
print(to_predict)

Explanation

    1.	Data Creation: We create a DataFrame with columns 'x', 'y', and 'z'. Some values in 'z' are missing (NaN values).
    2.	Data Preparation: Rows with missing values in 'z' are excluded to create a complete dataset (df_m) for model training.
    3.	Train-Test Split: The complete data is split into training and testing sets. (Note: Testing is not explicitly evaluated in this example.)
    4.	Model Training: A linear regression model is trained to learn the relationship between columns 'x' and 'y' (features) and column 'z' (target).
    5.	Predict Missing Values: The model predicts values for rows where 'z' is missing.
    6.	Fill Missing Values: The predicted values are inserted into the original DataFrame to replace the missing values in 'z'.

Output

Initial Data:

    x   y     z

0 2 4 8.0
1 7 15 15.0
2 8 17 NaN
3 10 20 20.0
4 15 24 NaN
5 17 28 NaN
6 30 41 35.0
7 41 56 NaN

Rows with Missing Values in “z”:

    x   y   z

2 8 17 NaN
4 15 24 NaN
5 17 28 NaN
7 41 56 NaN

Predictions for Missing Values:

[16.5, 23.7, 27.2, 50.4]

Data with Filled Missing Values in “z”:

    x   y     z

2 8 17 16.5
4 15 24 23.7
5 17 28 27.2
7 41 56 50.4

Summary

This approach provides an efficient way to fill missing values in a dataset where relationships between variables can be approximated with linear regression. This method is useful in situations where data is incomplete but exhibits a predictable pattern.
