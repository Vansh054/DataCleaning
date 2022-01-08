import pandas as pd

df = pd.read_csv("final_data.csv")
print(df.shape)
del df['sy_gaiamagerr2']
del df['sy_gaiamagerr1']
del df['sy_gaiamag']
print(df.shape)

