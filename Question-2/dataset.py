import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Generate random data for each attribute
np.random.seed(0)
data = {
    'Age': np.random.randint(40, 51, size=50),
    'Occupation': np.random.choice(['Business', 'Job', 'none'], size=50),
    'Lifestyle': np.random.choice(['Sedentary', 'Active'], size=50),
    'Family Diabetic History': np.random.choice(['Yes', 'No'], size=50),
    'Eating habits' : np.random.choice(['Nutritional', 'Junk food'], size=50),
    'Pre-diabetic condition' : np.random.choice(['Yes', 'No'], size=50),
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df.head())

# Export DataFrame to CSV
# df.to_csv("dataset.csv", index=False)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the 'Age' attribute
df['Age'] = scaler.fit_transform(df[['Age']])
print(df.head())

# Check for missing values
missing_values = df['Lifestyle'].isnull().sum()

if missing_values > 0:
    # Fill missing values with the most frequent value
    most_frequent_lifestyle = df['Lifestyle'].mode()[0]
    df['Lifestyle'].fillna(most_frequent_lifestyle, inplace=True)



