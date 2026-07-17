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

from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(model, X, y, title):
    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y, cv=5,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring="accuracy"
    )

    plt.plot(train_sizes, train_scores.mean(axis=1), label="Training Accuracy", color="steelblue")
    plt.plot(train_sizes, test_scores.mean(axis=1), label="Validation Accuracy", color="salmon")
    plt.title(title)
    plt.xlabel("Training Set Size")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

plot_learning_curve(
    DecisionTreeClassifier(random_state=42), X, y,
    "Learning Curve — Decision Tree (Overfit)"
)

plot_learning_curve(
    DecisionTreeClassifier(max_depth=3, random_state=42), X, y,
    "Learning Curve — Decision Tree (Constrained)"
)