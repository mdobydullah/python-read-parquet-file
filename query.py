import config

# Read from engine
data = config.pd.read_sql(f"SELECT * FROM {config.table_name} LIMIT 5", config.engine)
print(data)
