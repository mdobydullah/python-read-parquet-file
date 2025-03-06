<p align="center">
<strong>Python Read Parquet File</strong>
</p>

> Read Parquet file and write it to an SQL or ClickHouse database.

### Create Python Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# Conda
conda create --name myenv python=3.11
conda activate myenv
```

### Install Required Libraries

```bash
pip install pandas pyarrow sqlalchemy
```

For ClickHouse:

```bash
pip install clickhouse-connect
```

### Config

Update `config.py` file. Keep `parquet` or any `gz.parquet` files in the `data` directory.

### Read Parquet file

```bash
python read.py
```

### Write to Database

```bash
python write.py
```

### Read from Database

```bash
python query.py
```
