#!/usr/bin/env python
# coding: utf-8

# ## PYTHON JOURNEY MACHINE & DEEP LEARNING
# ### Trabalho prático usando o Python
# 
# ### Sorteio de amostra probabilística e cálculo do Intervalo de confiança de 95%

# In[44]:


# Importar as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import math


# Contexto dos dados
# 
# A gerente da área de Marketing Relacionamento da empresa XYZ tem observado, nas últimas campanhas, 
# um aumento no número de clientes não contatados. Uma das estratégias para melhorar esse quadro é a 
# utilização de outros canais de relacionamento. A gerente deseja testar os canais de relacionamento 
# em uma amostra de tamanho igual a 40.
# 
# Dicionário de variáveis:
# 
# Sexo: 2=Masculino;4=Feminino
# Idade: Idade 
# Cor_pele:0=missing; 2=Branca; 4=Preta; 6=Amarela; 8 = Parda
# Telefone móvel:2=Sim; 4=Não
# Anos_estudo: Anos de estudo

# # Importar o arquivo de dados

# In[22]:


# Importar o arquivo Arq_trab3.csv
df = pd.read_csv(r'C:\Users\lucas\Downloads\trab3\Arq_trab3.csv')


# In[23]:


df.head()


# In[24]:


df.info()


# In[25]:


# mudar o formato da variável number para string
df['Sexo'] = df['Sexo'].astype(str)
df['Cor_pele'] = df['Cor_pele'].astype(str)
df['Telefone_movel'] = df['Telefone_movel'].astype(str)


# In[26]:


df.info()


# # Tabela de Frequência da População

# In[28]:


sexo = pd.pivot_table(df, index='Sexo', values='ID', aggfunc=np.count_nonzero)


# In[30]:


sexo['%'] = (pd.pivot_table(df, index='Sexo', values='ID', aggfunc=np.count_nonzero))/df['ID'].count()*100


# In[31]:


sexo


# # Medidas resumo da Idade e Anos de estudo da População

# In[32]:


df.describe()


# In[ ]:





# # Sorteio da amostra probabilística

# In[33]:


df_sample = df.sample(n=40)


# In[34]:


df_sample.head()


# In[35]:


df_sample.info()


# # Tabela de Frequência da Amostra

# In[ ]:





# # Medidas resumo da Idade e Anos de estudo da Amostra

# In[36]:


sexo_ams = pd.pivot_table(df_sample, index='Sexo', values='ID', aggfunc=np.count_nonzero)


# In[37]:


sexo_ams['%'] = (pd.pivot_table(df_sample, index='Sexo', values='ID', aggfunc=np.count_nonzero))/df_sample['ID'].count()*100


# In[39]:


sexo_ams


# In[40]:


df_sample.describe()


# ### Cálculo do Intervalo de Confiança de 95% para proporção
# 
# #### Limite inferior = p - 1.96*sqrt(p*q)
# #### Limite superior = p + 1.96*sqrt(p*q)
# 
# #### nível de confiança de 95% = 1.96
# #### p=proporção de usuários de telefone móvel
# #### q= 1-p = proporção de usuários sem telefone móvel

# 

# ### Cálculo da proporção de clientes com telefone
# 
# ### Alterar o número de clientes com telefone móvel (k)
# ### prop_tel=k/40
# 

# In[41]:


telefone_ams = pd.pivot_table(df_sample, index='Telefone_movel', values='ID', aggfunc=np.count_nonzero)


# In[42]:


telefone_ams['%'] = (pd.pivot_table(df_sample, index='Telefone_movel', values='ID', aggfunc=np.count_nonzero))/df_sample['ID'].count()*100


# In[43]:


telefone_ams


# In[45]:


# Erro padrão
prop_telefone = 33 / 40
erro_padrao = math.pow(prop_telefone*((1-prop_telefone)/40),1/2)


# In[46]:


erro_padrao


# In[49]:


#Margem de erro
margem_erro = 1.96*erro_padrao


# In[50]:


margem_erro


# In[51]:


#Limite inferior do intercalo de confiança
li = prop_telefone-margem_erro


# In[52]:


li


# In[53]:


#Limite superior do intervalo de confiança
ls = prop_telefone+margem_erro


# In[54]:


ls


# In[ ]:




