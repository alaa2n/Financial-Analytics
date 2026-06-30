import duckdb
import os
import pandas as pd
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "finance_analytics_light_raw.duckdb"
)
excel_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "account_mapping_light.xlsx"
)


df_mapping_raw = pd.read_excel(excel_path)
con = duckdb.connect(db_path)

#register the dataframe so we can select from it 
con.register("df_account_mapping_raw", df_mapping_raw)

con.execute("""
CREATE OR REPLACE TABLE bronze_account_mapping_light AS
SELECT *
FROM df_account_mapping_raw;
""")

con.commit()

print("bronze_account_mapping_light table")

con.close()

