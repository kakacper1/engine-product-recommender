import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def user_recommendations(df, user_id, n=5):
    """
    Return top-N product recommendations for a specific user.
    """
    # Create user-item matrix
    user_item = df.pivot(index='user_id', columns='product_id', values='rating').fillna(0)

    # Compute cosine similarity between users
    similarity = cosine_similarity(user_item)
    similarity_df = pd.DataFrame(similarity, index=user_item.index, columns=user_item.index)

    # Get most similar users (excluding self)
    sim_users = similarity_df[user_id].drop(user_id)

    # Select ratings from similar users only
    similar_users_ratings = user_item.loc[sim_users.index]

    # Weighted average
    weighted_ratings = similar_users_ratings.T.dot(sim_users) / sim_users.sum()

    # Remove products already rated by the user
    already_rated = df[df['user_id'] == user_id]['product_id'].values
    recommendations = weighted_ratings.drop(already_rated, errors='ignore').sort_values(ascending=False).head(n)

    return recommendations
