#!/usr/bin/env python
# coding: utf-8

# ## PYTHON JOURNEY MACHINE & DEEP LEARNING
# ### Trabalho prático usando o Python
# ### Clusters Analysis usando o algoritmo k-means  
# 
# #### Objetivo: Separar um conjunto de objetos/clientes em grupos (clusters) de forma que os membros de qualquer grupo formado sejam os mais homogêneos possíveis com relação a algum critério, como por exemplo a distância euclidiana.
# 
# 
# 
# #### Procedimento:
# 
# #### (1) Selecionar  somente variáveis quantitativas (p).
# #### (2) Análise exploratória dos dados. 
# #### (3) Avaliar a presença de outliers e pontos extremos. 
# #### (4) Padronizar as variáveis antes de se calcular as distâncias, assim, as "p" variáveis serão igualmente importantes. Geralmente, a padronização feita é para que todas as variáveis (quantitativas) tenham média zero e variância 1.
# 
# 
# 
# 

# In[1]:


# Importar as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from collections import Counter


# In[2]:


# Importar a base de dados Recência, Frequência e Valor (RFV)
BaseRFV = pd.read_csv('BaseRFV.csv',sep=',')


# In[3]:


BaseRFV.head()


# In[4]:


BaseRFV.info()


# In[5]:


BaseRFV.count()


# In[6]:


BaseRFV.nunique()


# In[7]:


BaseRFV.isna().sum()


# ## Análise exploratória dos dados
# 
# - Utilize o Box Plot para detecção de outliers e pontos extremos
# - Gráfico de dispersão para identificar correlação entre as variáveis

# In[8]:


BaseRFV.describe()


# In[9]:


dados= BaseRFV.drop(columns=['id_cliente'])


# In[10]:


sns.boxplot(y='valor',data=dados)


# In[11]:


sns.boxplot(y='recencia',data=dados)


# In[12]:


sns.boxplot(y='compras',data=dados)


# In[13]:


sns.heatmap(dados.corr(),cmap='coolwarm',annot=True)
plt.title('dados.corr()')


# In[14]:


sns.pairplot(dados,hue='compras',palette='coolwarm')


# In[15]:


sns.jointplot(x='recencia',y='valor',data=dados)


# In[16]:


sns.clustermap(dados, standard_scale=1)


# In[17]:


rfv = dados.pivot_table(values='compras',index='valor',columns='recencia')
sns.heatmap(rfv)


# ### Normalizar os dados
# 
# ![Figura_Normal_Padrao.png](data:image/png;base64,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)
# 
# 
# 

# In[20]:


dadosnorm = normalize(dados)


# In[21]:


dados_normalizados= pd.DataFrame(data=dadosnorm )
dados_normalizados.head()


# In[22]:


dados_normalizados.describe()


# ### Análise de cluster
# 
# ![Figura_Dist_Euclidiana.png](data:image/png;base64,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)

# In[23]:


model = KMeans(n_clusters = 2)
clusters = model.fit_predict(dados_normalizados)


# In[24]:


Counter(clusters.tolist())


# In[25]:


model.cluster_centers_


# In[ ]:




