import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset: 'tips' dataset comes with Seaborn
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex")

# Add labels and title
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

# Show the plot
plt.show()