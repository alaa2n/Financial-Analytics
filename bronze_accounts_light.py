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
CREATE OR REPLACE TABLE bronze_accounts_light AS
SELECT
    account_number,
    account_name,
    account_type,
    currency
FROM raw__accounts_light;
""")

con.commit()

print("created bronze_accounts_light table")

con.close()

