import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pour panda une matrice est un dataframe
dataframe = pd.read_csv("data/house/house.csv")
# print(dataframe)
#print(dataframe.loyer)
# ou de facon equivalente
#print(dataframe["loyer"])
res = dataframe.loyer / dataframe.surface
#print(dataframe.loyer / dataframe.surface)
# print(np.mean(res), np.std(res))

import sqlite3
with sqlite3.connect("data/house/house.db3") as conn:
    dataframeSql = pd.read_sql("select * from house", conn)

resSql = dataframeSql.loyer / dataframeSql.surface
print(type(resSql))
# ajout d'une colonne au dataframe
dataframe.insert(2,'loyerParm2',resSql)
# print(dataframe)

print(np.mean(resSql), np.std(resSql))
std = np.std(resSql)
mean = np.mean(resSql)

# filtrage des donnees (data mining)
print("Before filtering : " + str(dataframe.shape))
filteredDataframe = dataframe[dataframe.surface < 300]
print("Filtering <300 : " + str(filteredDataframe.shape))

res = filteredDataframe.loyer / filteredDataframe.surface
std = np.std(res)
mean = np.mean(res)
filteredDataframe2 = filteredDataframe[abs(filteredDataframe.loyer/filteredDataframe.surface-mean) < 3 * std]
# solution alternative apres ajout de la colonne 'loyerParm2'
filteredDataframe2 = filteredDataframe[abs(filteredDataframe.loyerParm2-mean) < 3 * std]
print([abs(filteredDataframe.loyerParm2-mean) < 3 * std])
print("Filtering  <3sig : " + str(filteredDataframe2.shape))

import scipy.stats as stats

f, axarr = plt.subplots(3, sharex=True, sharey=True)
axarr[0].scatter(dataframe.surface,dataframe.loyer)
slope, intercept, rvalue, pvalue, stdErr = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, stdErr)
axarr[0].plot(dataframe.surface, slope * dataframe.surface + intercept, color="red")

axarr[1].scatter(filteredDataframe.surface,filteredDataframe.loyer)
slope, intercept, rvalue, pvalue, stdErr = stats.linregress(filteredDataframe.surface, filteredDataframe.loyer)
print(slope, intercept, rvalue, pvalue, stdErr)
axarr[1].plot(filteredDataframe.surface, slope * filteredDataframe.surface + intercept, color="red")

axarr[2].scatter(filteredDataframe2.surface,filteredDataframe2.loyer)
slope, intercept, rvalue, pvalue, stdErr = stats.linregress(filteredDataframe2.surface, filteredDataframe2.loyer)
print(slope, intercept, rvalue, pvalue, stdErr)
axarr[2].plot(filteredDataframe2.surface, slope * filteredDataframe2.surface + intercept, color="red")

f.subplots_adjust(hspace=0)
plt.show()