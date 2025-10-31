# 🧠 Product Recommendation Engine

A data science project that implements two recommendation strategies using Python and Docker.  
The engine uses product ratings data (`ratings.csv`) to provide:

1. **Top-N best-rated products** in a given timeframe (e.g., last year, last month)
2. **User-specific product recommendations** based on similar users’ preferences

This project can be run as a **Python CLI app** or explored interactively in **Jupyter Notebook**.

---

## 🚀 Features

- Cleans and normalizes input data (`ratings.csv`)
- Supports filtering by date or timeframe
- User-based collaborative filtering (cosine similarity)
- Easily extendable for model-based recommendations
- Ready-to-run with Docker or directly with Python

---

## 📂 Project Structure

project/
│
├── app.py # CLI entry point
├── data_loader.py # Handles data loading and cleaning
├── top_products.py # Top-N recommendation logic
├── user_recommend.py # User-based collaborative filtering
├── data/
│ └── ratings.csv # Input dataset (user_id, product_id, rating, timestamp)
├── Dockerfile # Docker configuration (based on jupyter/datascience-notebook)
└── README.md # Documentation
