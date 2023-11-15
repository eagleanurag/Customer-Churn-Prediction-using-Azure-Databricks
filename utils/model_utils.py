from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

def prepare_features(df, input_cols, output_col="features"):
    assembler = VectorAssembler(inputCols=input_cols, outputCol=output_col)
    return assembler.transform(df)

def train_model(df, features_col="features", label_col="Churn"):
    lr = LogisticRegression(featuresCol=features_col, labelCol=label_col)
    return lr.fit(df)

def evaluate_model(predictions, label_col="Churn"):
    evaluator = BinaryClassificationEvaluator(labelCol=label_col, metricName="areaUnderROC")
    return evaluator.evaluate(predictions)
