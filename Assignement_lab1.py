
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "Semester": [f"Sem {i}" for i in range(1, 9)],
    "compouer vision":     [82, 79, 88, 84, 90, 85, 87, 89],
    "machine_learning":  [75, 80, 85, 83, 87, 80, 84, 86],
    "deep_learning":[88, 84, 86, 81, 88, 82, 85, 87],
    "Web_development":  [91, 86, 89, 90, 92, 88, 90, 91],
    "python":       [85, 90, 87, 89, 91, 86, 89, 92]
}

# Create DataFrame and melt to long format
df = pd.DataFrame(data)
df_melted = df.melt(id_vars="Semester", var_name="Subject", value_name="Marks")

# Set style
sns.set(style="whitegrid")

# Box plot by Semester
plt.figure(figsize=(12, 6))
sns.boxplot(x="Semester", y="Marks", data=df_melted, palette="pastel")
plt.title("Box Plot: eesa's Marks Distribution by Semester")
plt.show()

# Violin plot by Semester
plt.figure(figsize=(12, 6))
sns.violinplot(x="Semester", y="Marks", data=df_melted, palette="muted")
plt.title("Violin Plot: eesa's Marks Distribution by Semester")
plt.show()