from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Data Ingestion").getOrCreate()

# Load data
data_path = "/dbfs/data/raw/customer_data.csv"
data = spark.read.csv(data_path, header=True, inferSchema=True)

# Show initial data
data.show(5)

# Save the raw data to a Delta table
data.write.format("delta").mode("overwrite").save("/dbfs/data/processed/customer_data_delta")

print("Data ingestion complete!")
