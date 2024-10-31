from pyspark.sql import SparkSession

# Creazione di una sessione Spark
spark = SparkSession.builder.appName("example_spark_job").getOrCreate()

# Creazione di un DataFrame di esempio
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
df = spark.createDataFrame(data, ["name", "age"])

# Esecuzione di un'operazione Spark
df.show()

# Terminare la sessione
spark.stop()
