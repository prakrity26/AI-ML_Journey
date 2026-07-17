import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("Titanic-Dataset.csv")

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
df_model = df[features + ["Survived"]].copy()
df_model["Age"].fillna(df_model["Age"].mean(), inplace=True)
df_model["Sex"] = df_model["Sex"].map({"male": 0, "female": 1})

X = df_model[features]
y = df_model["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Predict FARE (a number) instead of survival (a category)
# This is regression
X_fare = df_model[["Pclass", "Age", "SibSp", "Parch"]]
y_fare = df["Fare"].fillna(df["Fare"].mean())

X_train, X_test, y_train, y_test = train_test_split(
    X_fare, y_fare, test_size=0.2, random_state=42
)

reg_model = LinearRegression()
reg_model.fit(X_train, y_train)
predictions = reg_model.predict(X_test)

print("R2 Score:", r2_score(y_test, predictions))
print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))




# Why do we split data into train and test sets?
# We split the dataset so that the model is trained on one part of the data and tested on unseen data.
# Training set: Used to teach the model by learning patterns from the data.
# Testing set: Used to evaluate how well the model performs on new data it has never seen.
# This helps us determine whether the model has truly learned patterns or 
# has simply memorized the training data. Testing on unseen data gives a more realistic estimate 
# of how the model will perform in real-world situations.
# What is cross validation and why is it better than a single split?
# Uses all the data for both training and testing (at different times).
# Produces a more reliable and stable estimate of model performance.
# Reduces the chance that the result depends on one lucky or unlucky train-test split.
# Helps detect overfitting more effectively.
# What does a loss function do during training?
# A loss function measures how far the model's predictions are from the actual answers.
# If the predictions are close to the correct values, the loss is small.
# If the predictions are far from the correct values, the loss is large.