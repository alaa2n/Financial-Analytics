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
CREATE OR REPLACE TABLE bronze_geography_light AS
SELECT
    store_code,
    country,
    region
FROM raw__geography_light;
""")

con.commit()

print("created bronze_geography_light table")

con.close()

