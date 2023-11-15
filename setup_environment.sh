#!/bin/bash

# Step 1: Install necessary libraries
echo "Installing necessary libraries..."
databricks libraries install --cluster-id <your-cluster-id> \
    --pypi-package pyspark==3.4.1 \
    --pypi-package pandas==2.1.0 \
    --pypi-package numpy==1.26.0 \
    --pypi-package scikit-learn==1.4.0 \
    --pypi-package mlflow==2.7.1

# Step 2: Upload data files to DBFS
echo "Uploading data files to DBFS..."
databricks fs cp data/raw/customer_data.csv dbfs:/data/raw/customer_data.csv

# Step 3: Set up project folders
echo "Setting up project folders on DBFS..."
databricks fs mkdirs dbfs:/data/processed
databricks fs mkdirs dbfs:/data/output
databricks fs mkdirs dbfs:/models

echo "Environment setup complete!"
