import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(0)
data = {
    'age': np.random.randint(22, 60, size=50),
    'education': np.random.choice(['graduate', 'post graduate'], size=50),
    'salary': np.round(np.random.uniform(3, 20, size=50), 2),
    'married_status': np.random.choice(['yes', 'no'], size=50)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Export DataFrame to CSV
df.to_csv("dataset.csv", index=False)

# Bar plot for Education Level Distribution
plt.figure(figsize=(8, 6))
df['education'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Education Level Distribution')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.show()

# Histogram for Salary Distribution
plt.figure(figsize=(8, 6))
plt.hist(df['salary'], bins=10, color='salmon', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary (in Lakhs)')
plt.ylabel('Frequency')
plt.show()

# Box plot for Age Distribution
plt.figure(figsize=(8, 6))
plt.boxplot(df['age'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# Scatter plot for Salary vs Age
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['salary'], c=df['married_status'].map({'yes': 'blue', 'no': 'red'}))
plt.title('Salary vs Age')
plt.xlabel('Age')
plt.ylabel('Salary (in Lakhs)')
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Married'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Unmarried')])
plt.show()


# Education: Businesses offering educational products or services could target both graduate and post-graduate segments.

# Salary: Companies targeting consumers should consider the income distribution in their pricing and marketing strategies.
# For example, they might offer more affordable products or special discounts to cater to individuals with lower incomes.

# Age: Businesses could develop products or services that appeal to a broad age range, considering the diverse representation of ages in the dataset.

# Salary vs Age: Companies could use this insight to develop targeted marketing campaigns based on age and marital status, focusing on segments with higher
# purchasing power or specific needs.