import config

# Write Data to MySQL, PostgreSQL, or SQLite
config.df.to_sql(config.table_name, config.engine, if_exists="replace", index=False, chunksize=5000)

# Write to ClickHouse
# from clickhouse_connect import get_client
# client = get_client(host="your_clickhouse_host", port=8123, username="default", password="")
# client.insert_dataframe("INSERT INTO table_name VALUES", df)
