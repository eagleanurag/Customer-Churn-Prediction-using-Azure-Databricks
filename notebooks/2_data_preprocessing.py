from pyspark.sql.functions import col, when
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Data Preprocessing").getOrCreate()

# Load data from Delta table
data = spark.read.format("delta").load("/dbfs/data/processed/customer_data_delta")

# Data cleaning
data = data.dropna()  # Drop missing values
data = data.withColumn("Churn", when(col("Churn") == "Yes", 1).otherwise(0))  # Encode target

# Feature selection
selected_cols = ["Age", "MonthlyCharges", "TotalCharges", "Churn"]
data = data.select(*selected_cols)

# Save processed data
data.write.format("delta").mode("overwrite").save("/dbfs/data/processed/preprocessed_data_delta")

print("Data preprocessing complete!")
