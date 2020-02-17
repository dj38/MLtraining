import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pour panda une matrice est un dataframe
dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
#print(dataframe.loyer)
# ou de facon equivalente
#print(dataframe["loyer"])
res = dataframe.loyer / dataframe.surface
#print(dataframe.loyer / dataframe.surface)
print(np.mean(res), np.std(res))

import sqlite3
with sqlite3.connect("data/house/house.db3") as conn:
    dataframeSql = pd.read_sql("select * from house", conn)

resSql = dataframeSql.loyer / dataframeSql.surface

print(np.mean(resSql), np.std(resSql))

# filtrage des donnees (data mining)
filteredDataframe = dataframe[dataframe.surface < 250]
print(filteredDataframe)
# plt.plot(filteredDataframe.surface,filteredDataframe.loyer)
# plt.show()