import pandas as pd
import pyarrow.parquet as pq
# Definir o caminho para o arquivo JSON
JSON_FILE = "product.json"

# Ler os dados do arquivo JSON
df = pd.read_json(JSON_FILE)
#df = pd.DataFrame(JSON_FILE)

# Exibir o DataFrame
print(df)

PARQUET_FILE = "product.parquet"

# Salvar o DataFrame em um arquivo Parquet
#pq.write_table(pq.Table.from_pandas(df), PARQUET_FILE)
df.to_parquet(PARQUET_FILE)
print(f"Dados salvos no arquivo {PARQUET_FILE}")