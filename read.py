import config

df = config.pd.read_parquet(config.filename)
print(df.head(10))
