import pandas as pd

df = pd.read_csv('restaurants.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved to cleaned_data.csv")