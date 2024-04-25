import pandas as pd
import numpy as np

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
print(df.head())


# Export DataFrame to CSV
df.to_csv("dataset.csv", index=False)

# Binning the 'age' attribute
df['age_binned'] = pd.cut(df['age'], bins=5, labels=['20-30', '30-40', '40-50', '50-60', '60-70'])
print(df.head())
