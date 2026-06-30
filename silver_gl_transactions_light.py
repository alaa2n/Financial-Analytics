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
CREATE OR REPLACE TABLE silver_gl_transactions_light AS
SELECT
    transaction_id,
    STRFTIME(transaction_date, '%d.%m.%y') AS transaction_date,
    store_code,
    account_number,
    amount_local,
    UPPER(Trim(currency)) AS currency, 
    document_number,
    TRIM(description) AS description
FROM bronze_gl_transactions_light;
""")


con.commit()

print("created bronze_accounts_light table")

con.close()

