from pyspark.ml.classification import LogisticRegressionModel
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Model Deployment").getOrCreate()

# Load model
model = LogisticRegressionModel.load("/dbfs/models/logistic_regression_model")

# New data simulation
new_data = spark.createDataFrame(
    [(25, 70.5, 2000.0), (45, 90.0, 4000.0)],
    ["Age", "MonthlyCharges", "TotalCharges"]
)

# Predictions
predictions = model.transform(new_data)
predictions.select("Age", "MonthlyCharges", "TotalCharges", "prediction").show()
