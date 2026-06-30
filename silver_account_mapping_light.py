import duckdb
import os
import pandas as pd
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "finance_analytics_light_raw.duckdb"
)
con = duckdb.connect(db_path)

con.execute("""
CREATE OR REPLACE TABLE silver_account_mapping_light AS
SELECT 
    Cast(AccountNumber AS INTEGER) as account_number,
    TRIM(AccountName) as account_name,
    TRIM(PLLine) as pl_line,
    UPPER(TRIM(StatementType)) as statement_type,
    Cast(SortOrder AS INTEGER) as sort_order,
FROM bronze_account_mapping_light;
""")

con.commit()

print("silver_account_mapping_light table")

con.close()

