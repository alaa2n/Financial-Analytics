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
CREATE OR REPLACE TABLE gold_dim_stores_light AS
SELECT
    store_code As StoreCode,
    store_name As StoreName,
    store_type As StoreType,
    country As Country,
    region As Region
FROM silver_stores_light 
order by StoreCode;
""")

con.commit()

print("created gold_dim_stores_light table")

con.close()

