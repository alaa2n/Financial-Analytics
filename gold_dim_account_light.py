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
CREATE OR REPLACE TABLE gold_dim_accounts_light AS
SELECT
    account_number As AccountNumber,
    account_name As AccountName,
    account_type As AccountType,
    currency As AccountCurrency
FROM silver_accounts_light
Order by AccountNumber;
""")

con.commit()

print("created gold_dim_accounts_light table")

con.close()

