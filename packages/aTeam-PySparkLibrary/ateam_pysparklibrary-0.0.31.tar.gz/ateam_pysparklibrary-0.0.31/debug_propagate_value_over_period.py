from pyspark.sql import SparkSession
from delta import *
from pyspark.sql.types import *
from delta.tables import *
from pyspark.sql.functions import *

#Denne henter fra pip, jeg vil hente lokale endringer hele tiden.
from src.aTeam_PySparkLibrary.propagate_value_over_period import propagate_value_over_period

from datetime import timedelta
from dateutil.relativedelta import relativedelta

storage_account_name = "pedataplatformdev"
silver_path = "Facts/tmp/PropertyEnergyLabelNonMonthly"
new_silver_path = "Facts/PropertyEnergyLabel"

start_date_column_in_input_table = "issuedDate"
end_date_column_in_input_table = "expireDate"
business_key_in_input_table = "asset_id"

date_column_in_output_table = "first_date_in_month"

months_added_in_case_of_null_end_date = 12

time_periods = ["monthly", "quarterly", "yearly"]
time_period = time_periods[2]

debugBool = True

builder = SparkSession.builder.appName("debugSession").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

propagate_value_over_period(storage_account_name, silver_path, new_silver_path,start_date_column_in_input_table, end_date_column_in_input_table, business_key_in_input_table, date_column_in_output_table,months_added_in_case_of_null_end_date,time_period, spark, debugBool)

spark.stop()