import pandas as pd
from sqlalchemy import create_engine

filename = "data/admins.gz.parquet"
table_name = 'test'

# Read data
df = pd.read_parquet(filename)

# Database engines
# engine = create_engine("mysql+pymysql://user:password@host/database")
engine = create_engine("sqlite:///test.sqlite")
