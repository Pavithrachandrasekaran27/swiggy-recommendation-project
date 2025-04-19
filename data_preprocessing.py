import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

df = pd.read_csv('cleaned_data.csv')
categorical_cols = ['name', 'city', 'cuisine']
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
numerical_cols = ['rating', 'rating_count', 'cost']
final_df = pd.concat([df[numerical_cols].reset_index(drop=True), encoded_df], axis=1)
final_df.to_csv('encoded_data.csv', index=False)
with open('encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)
print("Preprocessing complete. Files saved: encoded_data.csv, encoder.pkl")