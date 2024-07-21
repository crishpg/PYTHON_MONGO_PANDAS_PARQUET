import pandas as pd

# Ler o arquivo Parquet em um dataframe
df = pd.read_parquet('product.parquet')

# Exibir o dataframe
print(df.head())