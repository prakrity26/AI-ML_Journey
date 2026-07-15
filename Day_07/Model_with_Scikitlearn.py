import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

# Select features
features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
df_model = df[features + ["Survived"]].copy()

# Handle missing values
df_model["Age"].fillna(df_model["Age"].mean(), inplace=True)

# Convert Sex to numbers 
df_model["Sex"] = df_model["Sex"].map({"male": 0, "female": 1})

# Split features and target
X = df_model[features]
y = df_model["Survived"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)
print(X.head())

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Model 1 — Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)

# Model 2 — Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)


# Accuracy
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predictions))
print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_predictions))

# Detailed report
print("\nDecision Tree Report:")
print(classification_report(y_test, dt_predictions))

print("\nLogistic Regression Report:")
print(classification_report(y_test, lr_predictions))

# Confusion Matrix for better model
cm = confusion_matrix(y_test, lr_predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Died","Survived"],
            yticklabels=["Died","Survived"])
plt.title("Logistic Regression Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()


# Decision trees can tell us which features mattered most
importances = pd.Series(
    dt_model.feature_importances_,
    index=features
).sort_values(ascending=False)

importances.plot(kind="bar", color="steelblue")
plt.title("Feature Importance — Decision Tree")
plt.ylabel("Importance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
