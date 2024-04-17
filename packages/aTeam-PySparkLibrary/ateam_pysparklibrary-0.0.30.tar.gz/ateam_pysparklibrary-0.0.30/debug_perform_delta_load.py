from pyspark.sql import SparkSession
from delta import *
from pyspark.sql.types import *
from delta.tables import *
from pyspark.sql.functions import *

from src.aTeam_PySparkLibrary.perform_delta_load import perform_delta_load


storage_account_name = "pedataplatformdev"
bronze_path = "manual/VarigPropertiesMappedToFazileProperties.csv"
file_extension = 'csv'
dataset_type = 'dim'
dataset_name = 'property_management_group'
business_key_column_name = 'asset_id'

debugBool = True

builder = SparkSession.builder.appName("debugSession").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

perform_delta_load(storage_account_name, bronze_path, file_extension, dataset_type, dataset_name, business_key_column_name, spark, debugBool)


spark.stop()