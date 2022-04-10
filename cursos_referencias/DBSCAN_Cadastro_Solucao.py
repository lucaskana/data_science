#!/usr/bin/env python
# coding: utf-8

# ## PYTHON JOURNEY MACHINE & DEEP LEARNING
# ### Trabalho prático usando o Python
# ### Clusters Analysis usando o algoritmo Density-Based Spatial Clustering (DBSCAN)  
# 
# link: ttps://www.youtube.com/watch?v=eq1zKgCFwkk
# Case: Implement DBSCAN Clustering and detecting OUTLIERS with Python

# In[ ]:


# Importar as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
from pylab import rcParams
rcParams['figure.figsize'] = 14,6
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Importar a base de dados
df = pd.read_csv('C:/Users/regin/FIAP/Shift/Imersao_Python/Turma3/trab1/cadastro.csv')
df.head()


# In[ ]:


# Ver os tipos de variáveis
df.info()


# In[ ]:


# Quantificar os missing 
df.isna().sum()


# In[ ]:


# Recode os missing
df.replace('nan', np.NaN, inplace=True)


# In[ ]:


# Apagar as linhas com missing
df = df[df['LONGITUDE'].notna()]


# In[ ]:


df.info()


# In[ ]:


# Gráfico da longitude e latitude
_=plt.plot(df['LONGITUDE'], df['LATITUDE'], marker='.', linewidth=0, color='#128128')
_=plt.grid(which='major', color='#cccccc', alpha=0.45)
_=plt.title('Distribuição geográfica de GPS', family ='Arial', fontsize=12)
_=plt.xlabel('Longitude')
_=plt.ylabel('Latitude')
_=plt.show()


# In[ ]:


# Preparar os dados para o modelo
dbscan_df = df[['LONGITUDE', 'LATITUDE']]
dbscan_df = dbscan_df.values.astype('float32', copy=False) 
dbscan_df


# In[ ]:


# Padronizar os dados usando a Distribuição Normal Padrão
dbscan_df_scaler = StandardScaler().fit(dbscan_df)
dbscan_df = dbscan_df_scaler.transform(dbscan_df)
dbscan_df


# In[ ]:


# Parâmetros do modelo DBSCAN
'''
-- min_samples :: requires a minimum 20 data points in a neighboardhood
-- eps :: in radius 0.02
'''
modelo = DBSCAN(eps=0.02, min_samples=5, metric='euclidean').         fit(dbscan_df)
modelo


# In[ ]:


# Identificar os outliers 
outliers_df = df[modelo.labels_ == -1]
clusters_df = df[modelo.labels_ != -1]

colors = modelo.labels_
colors_clusters = colors[colors != -1]
colors_outliers = 'black'

clusters = Counter(modelo.labels_)
print(clusters)
print(df[modelo.labels_ == -1].head())
print('Número de clusters = {}'.format(len(clusters)-1))


# In[ ]:


# Visualizar os clusters

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])
ax.scatter(clusters_df['LONGITUDE'], clusters_df['LATITUDE'], c=colors_clusters, edgecolors='black', s=50)
ax.scatter(outliers_df['LONGITUDE'], outliers_df['LATITUDE'], c=colors_outliers, edgecolors='black', s=50)
ax.set_xlabel('Longitude', family = 'Arial', fontsize = 9)
ax.set_ylabel('Latitude', family = 'Arial', fontsize = 9)

plt.title('Clusters')
plt.grid(which='major', color='#cccccc', alpha=0.45)


# ![figura_clusters.png](attachment:figura_clusters.png)

# In[ ]:





# In[ ]:




