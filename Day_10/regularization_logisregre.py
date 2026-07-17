import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                              f1_score, classification_report, confusion_matrix)

# Load and prepare Titanic data
df = pd.read_csv("Titanic-Dataset.csv")
features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
df_model = df[features + ["Survived"]].copy()
df_model["Age"].fillna(df_model["Age"].mean(), inplace=True)
df_model["Sex"] = df_model["Sex"].map({"male": 0, "female": 1})

X = df_model[features]
y = df_model["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)

from sklearn.linear_model import LogisticRegression

# C parameter controls regularization
# Small C = strong regularization = simpler model
# Large C = weak regularization = complex model

for C in [0.001, 0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    print(f"C={C:6} | Train: {train_acc:.2f} | Test: {test_acc:.2f}")