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
CREATE OR REPLACE TABLE gold_dim_account_mapping_light AS
SELECT 
    account_number as AccountNumber,
    account_name as AccountName,
    pl_line as PLLine,
    statement_type as StatementType,
    sort_order as SortOrder
FROM silver_account_mapping_light
Order by SortOrder,AccountNumber;
""")

con.commit()

print("gold_dim_account_mapping_light table created")

con.close()

