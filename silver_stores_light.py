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
CREATE OR REPLACE TABLE silver_stores_light AS
SELECT
    s.store_code,
    TRIM(s.store_name) as store_name,
    UPPER(TRIM(s.store_type)) as store_type,
    g.country,
    g.region
FROM bronze_stores_light s
left JOIN bronze_geography_light g
on s.store_code = g.store_code;
""")

con.commit()

print("created silver_stores_light table")

con.close()

