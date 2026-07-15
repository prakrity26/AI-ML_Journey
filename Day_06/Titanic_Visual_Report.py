import matplotlib.pyplot as plt
import pandas as pd

# Load Titanic Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Create a figure with 4 subplots (2 rows × 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Survival Count Bar Chart
df["Survived"].value_counts().plot(
    kind="bar",
    ax=axes[0, 0],
    color=["salmon", "steelblue"]
)
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xlabel("Survived (0 = No, 1 = Yes)")
axes[0, 0].set_ylabel("Number of Passengers")
axes[0, 0].tick_params(axis='x', rotation=0)

# 2. Age Distribution Histogram
df["Age"].dropna().plot(
    kind="hist",
    bins=20,
    ax=axes[0, 1],
    color="steelblue",
    edgecolor="black"
)
axes[0, 1].set_title("Age Distribution")
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_ylabel("Count")


# 3. Survival Rate by Passenger Class

df.groupby("Pclass")["Survived"].mean().plot(
    kind="bar",
    ax=axes[1, 0],
    color=["gold", "silver", "brown"]
)
axes[1, 0].set_title("Survival Rate by Passenger Class")
axes[1, 0].set_xlabel("Passenger Class")
axes[1, 0].set_ylabel("Survival Rate")
axes[1, 0].tick_params(axis='x', rotation=0)


# 4. Survival Rate by Gender
df.groupby("Sex")["Survived"].mean().plot(
    kind="bar",
    ax=axes[1, 1],
    color=["lightcoral", "steelblue"]
)
axes[1, 1].set_title("Survival Rate by Gender")
axes[1, 1].set_xlabel("Gender")
axes[1, 1].set_ylabel("Survival Rate")
axes[1, 1].tick_params(axis='x', rotation=0)

# Main Title

plt.suptitle("Titanic EDA — Visual Report", fontsize=16, fontweight="bold")

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure
plt.savefig("titanic_visual_report.png", dpi=300)

# Display the figure
plt.show()