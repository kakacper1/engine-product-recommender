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

---

## 🐳 Run with Docker

### 1. **Build the image**
```bash
docker build -t my-python-app .
2. Run CLI mode (default)
Top-N products:

bash
Copy code
docker run --rm -v $(pwd)/data:/home/jovyan/app/data my-python-app \
    python app.py top-products --n 10 --start 2024-01-01 --end 2024-12-31
User recommendations:

bash
Copy code
docker run --rm -v $(pwd)/data:/home/jovyan/app/data my-python-app \
    python app.py recommend --user 42 --n 5
3. Run in Jupyter Notebook mode
bash
Copy code
docker run -it --rm -p 8888:8888 -v $(pwd)/data:/home/jovyan/app/data \
    my-python-app start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''
Then open http://localhost:8888 in your browser.

🧩 Example CLI Usage
Top 5 products in 2024
bash
Copy code
python app.py top-products --n 5 --start 2024-01-01 --end 2024-12-31
Recommend 5 products for user 42
bash
Copy code
python app.py recommend --user 42 --n 5
🧹 Data Cleaning
The dataset (ratings.csv) must contain:

user_id — integer

product_id — integer

rating — float (1–5 scale)

timestamp — either datetime string or Unix timestamp (seconds since 1970)

Timestamps are automatically converted to dates during loading.

Example:

c
Copy code
user_id,product_id,rating,timestamp
1,101,5,1476640644
2,102,4,2024-06-15 09:20:00
🧠 Recommendation Logic
1. Top-N Products
Filters data by optional start/end date

Groups by product_id

Computes mean rating per product

Returns top-N results

2. User Recommendations
Builds a user-item matrix

Computes cosine similarity between users

Aggregates ratings from the most similar users

Excludes products already rated by the target user

🛠️ Development (without Docker)
Install dependencies
bash
Copy code
pip install pandas scikit-learn click
Run locally
bash
Copy code
python app.py top-products --n 10
python app.py recommend --user 42 --n 5
