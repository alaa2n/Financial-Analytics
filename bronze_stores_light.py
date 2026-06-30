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
CREATE OR REPLACE TABLE bronze_stores_light AS
SELECT
    store_code,
    store_name,
    store_type
FROM raw__stores_light;
""")

con.commit()

print("created bronze_stores_light table")

con.close()

