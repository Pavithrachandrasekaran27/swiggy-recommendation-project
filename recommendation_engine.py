import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

cleaned_df = pd.read_csv('cleaned_data.csv')
encoded_df = pd.read_csv('encoded_data.csv')

def recommend(city, cuisine, rating, cost, top_n=5):
    mask = (cleaned_df['city'].str.lower() == city.lower()) & (cleaned_df['cuisine'].str.lower().str.contains(cuisine.lower()))
    filtered_encoded = encoded_df[mask]
    filtered_original = cleaned_df[mask]
    if filtered_encoded.empty:
        return pd.DataFrame({'Message': ["No matching restaurants found. Try changing your inputs."]})
    user_input = pd.DataFrame([[rating, 0, cost] + [0] * (filtered_encoded.shape[1] - 3)], columns=filtered_encoded.columns)
    similarity = cosine_similarity(user_input, filtered_encoded)
    top_indices = similarity[0].argsort()[-top_n:][::-1]
    return filtered_original.iloc[top_indices]