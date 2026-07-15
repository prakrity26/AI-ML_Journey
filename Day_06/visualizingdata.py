import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# # Bar Chart: Survival Count
# df["Survived"].value_counts().plot(kind="bar", color=["salmon", "steelblue"])
# plt.title("Survival Count")
# plt.xlabel("Survived (0=No, 1=Yes)")
# plt.ylabel("Number of Passengers")
# plt.xticks(rotation=0)
# plt.show()

# # Histogram: Age Distribution
# df["Age"].dropna().plot(kind="hist", bins=20, color="steelblue", edgecolor="black")
# plt.title("Age Distribution of Passengers")
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.show()

# # Bar Chart: Survival Rate by Gender
# df.groupby("Sex")["Survived"].mean().plot(kind="bar", color=["lightcoral", "steelblue"])
# plt.title("Survival Rate by Gender")
# plt.ylabel("Survival Rate")
# plt.xticks(rotation=0)
# plt.show()

# # Scatter Plot: Age vs Fare
# survived = df[df["Survived"] == 1]
# not_survived = df[df["Survived"] == 0]

# plt.scatter(not_survived["Age"], not_survived["Fare"], alpha=0.5, label="Died", color="salmon")
# plt.scatter(survived["Age"], survived["Fare"], alpha=0.5, label="Survived", color="steelblue")
# plt.title("Age vs Fare by Survival")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.legend()
# plt.show()

# Heatmap: Correlation Matrix
numeric_cols = df[["Survived", "Pclass", "Age", "Fare", "SibSp", "Parch"]]
correlation = numeric_cols.corr()

# sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation Matrix")
# plt.show()                  

# Pclass has negative correlation with Survived (-0.34)
# meaning higher class number = lower survival
# Fare has positive correlation (0.26) - richer passengers survived more

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

df.groupby("Sex")["Survived"].mean().plot(kind="bar", ax=axes[0], color=["lightcoral","steelblue"])
axes[0].set_title("Survival by Gender")

df.groupby("Pclass")["Survived"].mean().plot(kind="bar", ax=axes[1], color=["gold","silver","brown"])
axes[1].set_title("Survival by Class")

plt.suptitle("Titanic Survival Analysis", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("titanic_analysis.png", dpi=150)  # save the figure
plt.show()