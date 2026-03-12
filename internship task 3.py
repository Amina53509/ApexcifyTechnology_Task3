import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dark theme for graph
plt.style.use("dark_background")

# Load dataset
df = pd.read_csv("airline_passenger_satisfaction.csv")

# Show dataset preview
print("Dataset Preview:\n")
print(df.head())

# Show column names
print("\nColumns in dataset:\n")
print(df.columns)

# Count satisfaction levels
satisfaction_counts = df["Satisfaction"].value_counts()

# Display results
print("\nSatisfaction Level Counts:\n")
print(satisfaction_counts)

# Create bar chart
plt.figure(figsize=(8,5))
sns.barplot(x=satisfaction_counts.index, y=satisfaction_counts.values)

# Chart labels
plt.title("Passenger Satisfaction Survey Analysis")
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of Responses")

# Show graph
plt.show()