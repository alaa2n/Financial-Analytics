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
CREATE OR REPLACE TABLE gold_fact_gl_transactions_monthly_light AS
WITH BASE AS (
    SELECT
        DATE(STRPTIME(TransactionDate, '%d.%m.%y')) AS transaction_date,
        StoreCode,
        AccountNumber,
        AmountLocal
    FROM gold_fact_gl_transactions_light
)
SELECT
    DATE_TRUNC('month', transaction_date) AS TransactionMonth,
    StoreCode,
    AccountNumber,
    SUM(AmountLocal) AS AmountLocal
FROM BASE
GROUP BY TransactionMonth, StoreCode, AccountNumber
Order by TransactionMonth, StoreCode, AccountNumber;
""")


con.commit()

print("created gold_fact_gl_transactions_monthly_light table")

con.close()

