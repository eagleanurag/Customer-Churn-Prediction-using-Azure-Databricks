from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Model Evaluation").getOrCreate()

# Load test data and model
test_data = spark.read.format("delta").load("/dbfs/data/processed/preprocessed_data_delta")
model = LogisticRegressionModel.load("/dbfs/models/logistic_regression_model")

# Predictions
predictions = model.transform(test_data)

# Evaluation
evaluator = BinaryClassificationEvaluator(labelCol="Churn", metricName="areaUnderROC")
roc_auc = evaluator.evaluate(predictions)

print(f"ROC-AUC: {roc_auc}")
