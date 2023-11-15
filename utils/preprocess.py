from pyspark.sql.functions import col, when

def clean_data(df):
    return df.dropna()

def encode_target(df, target_col="Churn"):
    return df.withColumn(target_col, when(col(target_col) == "Yes", 1).otherwise(0))
