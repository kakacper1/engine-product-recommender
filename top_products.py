import pandas as pd

def top_n_products(df, n=10, start_date=None, end_date=None):
    if start_date:
        df = df[df['datetime'] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df['datetime'] <= pd.to_datetime(end_date)]
    
    # Average rating per product
    top_products = df.groupby('product_id')['rating'].mean().sort_values(ascending=False).head(n)
    return top_products