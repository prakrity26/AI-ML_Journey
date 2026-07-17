# Conceptually this is what happens during model.fit():
# 1. Model makes a prediction
# 2. Loss function measures how wrong it was
# 3. Model adjusts parameters to be less wrong
# 4. Repeat thousands of times
# 5. Stop when loss stops improving

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("Titanic-Dataset.csv")

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
df_model = df[features + ["Survived"]].copy()
df_model.fillna({"Age": df_model["Age"].mean()}, inplace=True)
df_model["Sex"] = df_model["Sex"].map({"male": 0, "female": 1})

X = df_model[features]
y = df_model["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42     # makes split reproducible
)