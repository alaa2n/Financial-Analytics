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
CREATE OR REPLACE TABLE bronze_gl_transactions_light AS
SELECT
    transaction_id,
    transaction_date,
    store_code,
    account_number,
    amount_local,
    currency, 
    document_number,
    description
FROM raw__gl_transactions_light;
""")

con.commit()

print("created bronze_gl_transactions_light table")

con.close()

