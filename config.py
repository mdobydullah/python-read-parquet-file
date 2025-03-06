import pandas as pd
from sqlalchemy import create_engine

filename = "data/tickets.parquet"
table_name = 'tickets'

# Read data
df = pd.read_parquet(filename)

# Database engines
engine = create_engine("mysql+pymysql://root@localhost/test")  # root:password@host/database
# engine = create_engine("sqlite:///test.sqlite")
