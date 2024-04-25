import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(0)
data = {
    'Age': np.random.randint(40, 51, size=50),
    'Occupation': np.random.choice(['Business', 'Job', 'none'], size=50),
    'Lifestyle': np.random.choice(['Sedentary', 'Active'], size=50),
    'Family Diabetic History': np.random.choice(['Yes', 'No'], size=50),
    'Eating habits' : np.random.choice(['Nutritional', 'Junk food'], size=50),
    'Pre-diabetic condition' : np.random.choice(['Yes', 'No'], size=50),
}
# Creating DataFrame
df = pd.DataFrame(data)

# Export DataFrame to CSV
df.to_csv("dataset.csv", index=False)

# Bar Chart of Occupation
plt.figure(figsize=(8, 6))
df['Occupation'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Occupation Distribution')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.show()

# Histogram of Age
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, color='salmon', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot of Age
plt.figure(figsize=(8, 6))
plt.boxplot(df['Age'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Box Plot of Age')
plt.xlabel('Age')
plt.show()

# Scatter Plot of Age vs Pre-diabetic Condition
plt.figure(figsize=(8, 6))
colors = {'Yes': 'red', 'No': 'blue'}
plt.scatter(data['Age'], range(len(data)), c=data['Pre-diabetic condition'].map(colors))
plt.title('Scatter Plot of Age vs Pre-diabetic Condition')
plt.xlabel('Age')
plt.ylabel('Index')
plt.legend(handles=['Pre-diabetic condition'])
plt.show()


# Occupation Distribution : if a significant portion of the population is employed in jobs that involve sedentary behavior, it may indicate a need for
# workplace wellness programs or interventions to promote physical activity.

#Age Distribution : if a large portion of the population falls within an age range associated with increased risk of diabetes, targeted screening
# and education programs can be implemented to detect and manage pre-diabetic conditions early

# Box Plot of Age : It can help identify outliers and understand the variability in age among the surveyed individuals. This insight can inform
# healthcare providers about the diversity of age groups they serve and guide the development of age-specific healthcare services and programs.

# Scatter Plot of Age vs Pre-diabetic Condition : It can help identify any patterns or trends that may exist, such as whether pre-diabetic conditions
# are more prevalent in certain age groups. This insight can inform targeted interventions and preventive measures to reduce the incidence of pre-diabetes
# and promote healthier lifestyles.