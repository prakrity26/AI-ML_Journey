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