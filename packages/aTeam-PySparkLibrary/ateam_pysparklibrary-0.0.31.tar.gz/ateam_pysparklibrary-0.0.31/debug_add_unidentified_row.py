from pyspark.sql import SparkSession
from delta import *
from pyspark.sql.types import *
from delta.tables import *
from pyspark.sql.functions import *

from src.aTeam_PySparkLibrary.add_unidentified_row import add_unidentified_row


directoryLevel = 'silver'
folderPath = "Dimensions/PropertyManagementGroup/"
businessKeyColumn  = "asset_id"
dimensionKeyColumn = "pk_dim_property_management_group_key"
storageAccName = "pedataplatformdev" #TODO: retrieve from key vault
debugBool = True

builder = SparkSession.builder.appName("debugSession").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

add_unidentified_row(directoryLevel, folderPath, businessKeyColumn, dimensionKeyColumn, storageAccName, spark, debugBool)
spark.stop()