import duckdb
import os

db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "finance_analytics_light_raw.duckdb"
)

print(db_path)

con = duckdb.connect(db_path)

con.execute("""
CREATE OR REPLACE TABLE silver_accounts_light AS
SELECT
   CAST(account_number AS INTEGER) as account_number,
   TRIM(account_name) as account_name,
   UPPER(TRIM(account_type)) as account_type,
   UPPER(TRIM(currency)) as currency
FROM bronze_accounts_light;
""")

con.commit()

print("created silver_accounts_light table")

con.close()

