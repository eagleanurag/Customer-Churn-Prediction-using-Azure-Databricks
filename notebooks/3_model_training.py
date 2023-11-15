from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Model Training").getOrCreate()

# Load preprocessed data
data = spark.read.format("delta").load("/dbfs/data/processed/preprocessed_data_delta")

# Feature engineering
assembler = VectorAssembler(inputCols=["Age", "MonthlyCharges", "TotalCharges"], outputCol="features")
data = assembler.transform(data)

# Split data
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# Train model
lr = LogisticRegression(featuresCol="features", labelCol="Churn")
model = lr.fit(train_data)

# Save model
model.save("/dbfs/models/logistic_regression_model")

print("Model training complete!")
