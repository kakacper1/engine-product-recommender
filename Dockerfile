# Base image with Jupyter and common data science libraries
FROM jupyter/datascience-notebook:latest

# Set working directory
WORKDIR /home/jovyan/app

# Copy project files
COPY . /home/jovyan/app

# Install dependencies (Click is required for CLI)
RUN pip install --no-cache-dir click scikit-learn pandas

# Expose the default Jupyter port
EXPOSE 8888

# Default command: start CLI (can be overridden)
CMD ["python", "app.py"]
