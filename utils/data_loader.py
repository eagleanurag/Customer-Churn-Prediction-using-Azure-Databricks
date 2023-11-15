from pyspark.sql import SparkSession

def load_data(file_path, format="csv", header=True):
    spark = SparkSession.builder.getOrCreate()
    return spark.read.format(format).option("header", header).load(file_path)

def save_data(df, output_path, format="delta"):
    df.write.format(format).mode("overwrite").save(output_path)
