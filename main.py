import pandas as pd
file_path = 'public/'

df = pd.read_csv(f"{file_path}sesamesim.csv")

print(df.head())