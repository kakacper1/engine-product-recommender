import pandas as pd

def load_data(file_path="/home/jovyan/app/data/ratings.csv"):
    """Load and clean ratings data with columns: user_id, product_id, rating, timestamp"""
    df = pd.read_csv(file_path)
    
    # Drop rows with missing valuesls
    df = df.dropna(subset=['user_id', 'product_id', 'rating', 'timestamp'])
    
    # Ensure correct data types
    df['user_id'] = df['user_id'].astype(int)
    df['product_id'] = df['product_id'].astype(int)
    df['rating'] = df['rating'].astype(float)
    # Convert entire column to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
    
    return df