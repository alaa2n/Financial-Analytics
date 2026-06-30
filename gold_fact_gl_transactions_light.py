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
CREATE OR REPLACE TABLE gold_fact_gl_transactions_light AS
SELECT
    transaction_id as TransactionID,
    transaction_date AS TransactionDate,
    store_code as StoreCode,
    account_number as AccountNumber,
    amount_local as AmountLocal,
    currency AS Currency, 
    document_number as DocumentNumber,
    description AS Description
FROM silver_gl_transactions_light
Order by TransactionID;
""")


con.commit()

print("created gold_fact_gl_transactions_light table")

con.close()

