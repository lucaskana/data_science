#!/usr/bin/env python
# coding: utf-8

# ## PYTHON JOURNEY MACHINE & DEEP LEARNING
# ### Trabalho prático usando o Python
# ### Noções de probabilidade

# ### Definição 1
# 
# “A probabilidade simplesmente determina qual é a chance de algo acontecer.”
# 
# “Toda vez que não temos certeza sobre o resultado de algum evento, estamos tratando da probabilidade de certos resultados acontecerem—ou quais as chances de eles acontecerem.”
# 
# Fonte:https://pt.khanacademy.org/math/probability/probability-geometry/probability-basics/a/probability-the-basics
# 
# 
# ### Definição 2
# 
# “As frequências relativas são estimativas de probabilidade de ocorrência de certos eventos de interesse. 
# Com suposições adequadas, e sem observamos diretamente o fenômeno aleatório de interesse, podemos criar 
# um modelo teórico que reproduza de maneira razoável a distribuição das frequências, quando o fenômeno é 
# observado diretamente. Tais modelos são chamados de modelos probabilísticos.”
# 
# (Bussab, WO e Morettin, PA, Estatística Básica. 5 ed. São Paulo: Saraiva, 2002, página 103).
# 
# 
# ![exemplo2_prob_freq.png](attachment:exemplo2_prob_freq.png)

# ### Propriedades
# 
# (1) Para cada experiência define-se um espaço amostral
# (2) Probabilidade de um evento E:  0 ≤ P(E) ≤ 1
# (3) P(S) = Soma das probabilidades dos eventos simples = 1
# 

# ### Exemplo 1: Qual a probabilidade de ganhar o prêmio máximo da Mega Sena com um único jogo de seis dezenas?
# 
# ![megasena.png](attachment:megasena.png)
# 

# In[ ]:


# Espaço amostral

omega = {(1,2,3,4,5,6), (1,2,3,4,5,7), (1,2,3,4,5,8) .... (????)}


# ### Método para resolver problema relacionado a contagem
# 
# ![analise_combinatoria.png](attachment:analise_combinatoria.png)

# In[3]:


# Importar numpy
import numpy as np


# In[ ]:


# Fatorial
0! = 1
1! = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6


# In[8]:


# Solução
print('0!=',np.math.factorial(3))


# In[11]:


n = 60
p= 6
difnp = n - p
print('n!=',np.math.factorial(n))
print('p!=',np.math.factorial(p))      
print('difnp!=',np.math.factorial(difnp))
print('combinacoes=',np.math.factorial(n)/(np.math.factorial(difnp)*np.math.factorial(p)))


# In[13]:


# Cálculo da probabilidade de ganhar com um único jogo da Mega Sena

prob = 1/np.math.factorial(n)/(np.math.factorial(difnp)*np.math.factorial(p))
print(prob)


# In[ ]:





# ## Distribuição de probabilidade
# ### Variável discreta

# ### Exemplo
# 
# Construir o modelo preditivo a fim de prever o resultado de partidas do campeonato brasileiro.
# 
# Considerando que a quantidade de gols marcados (K) em uma partida de futebol do Campeonato Brasileiro de Futebol (Brasileirão) em 2018 seja uma variável aleatória que segue a distribuição de Poisson com média de gols igual a 𝜆. 
# 
# Calcule a probabilidade de ocorrer k = 0, 1, 2, 3, 4, 5, 6 e 7.
# 
# 
# ![distr_poisson.png](attachment:distr_poisson.png)

# In[1]:


# importar as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# In[15]:


# Importar os dados do Cartola FC de 2018 para estimar a média de gols.

cartolafc = pd.read_excel(r'C:\Users\regin\FIAP\Shift\Imersao_Python\Turma3\trab2\cartola_fc_2018.xlsx')


# In[16]:


cartolafc.head()


# In[17]:


cartolafc.info()


# In[18]:


cartolafc.describe().round(2)


# In[19]:


media_gols = cartolafc['gols'].mean()
print(media_gols)


# In[20]:


# Gráfico da variável gols
sn.countplot(x='gols', data=cartolafc)


# In[21]:


# Calcular a média de gols

media_gols = cartolafc['gols'].mean()
print(media_gols)


# In[22]:


# Qual a probabilidade de ocorrer 0 gol?
# P(K=0) = 0.113413528037031
lamb = media_gols
euler = 2.71828
k=0
numerador = (euler**(-lamb))*lamb**k
denominador = np.math.factorial(k)
prob_k = numerador/denominador
print('prob=', prob_k)


# In[23]:


# Qual a probabilidade de ocorrer 1 gol?
# P(K=1) = 0.24682365180690696
lamb = media_gols
euler = 2.71828
k=1
numerador = (euler**(-lamb))*lamb**k
denominador = np.math.factorial(k)
prob_k = numerador/denominador
print('prob=', prob_k)


# In[24]:


# Qual a probabilidade de ocorrer 2 gol?
# P(K=2) = 0.26858310532146323
lamb = media_gols
euler = 2.71828
k=2
numerador = (euler**(-lamb))*lamb**k
denominador = np.math.factorial(k)
prob_k = numerador/denominador
print('prob=', prob_k)


# In[25]:


# Qual a probabilidade de ocorrer 3 gol?
# P(K=3) = 0.19484055096565803
lamb = media_gols
euler = 2.71828
k=3
numerador = (euler**(-lamb))*lamb**k
denominador = np.math.factorial(k)
prob_k = numerador/denominador
print('prob=', prob_k)


# In[28]:


#instalar: pip install empiricaldist
get_ipython().system('pip install empiricaldist')
from empiricaldist import Pmf

def poisson_pmf (lam,qs):
    ps = poisson(lam).pmf(qs)
    pmf = Pmf(ps,qs)
    return pmf
    


# In[31]:


from scipy.stats import poisson

# Probanility Mass Function
from empiricaldist import Pmf
def poisson_pmf(lam, qs):
    ps=poisson(lam).pmf(qs)
    pmf=Pmf(ps,qs)
    return pmf


# In[33]:


lam = media_gols
goals=np.arange(10)
pmf_goals = poisson_pmf(lam,goals)
print(pmf_goals)


# In[34]:


# Probanility Mass Function
lam = 2
goals=np.arange(10)
pmf_goals = poisson_pmf(lam,goals)
print(pmf_goals)


# In[ ]:





# ## Distribuição de probabilidade
# ### Variável contínua
# 
# ![distr_normal.png](attachment:distr_normal.png)

# ## Distribuição Normal Padrão ou Normal Reduzida
# 
# ![dist_norm_padr.png](attachment:dist_norm_padr.png)

# In[ ]:


# Use a Tabela Normal Padrão para encontrar a probabilidade:

1) P(Z > 0) = 0.50

2) P(Z < 0) = 0.50

3) P(Z > 1.96) = 0.50 -0.475 = 0.025

4) P(Z < -1.96) = 0.50 - 0.475 = 0.025

5) P(-1.96 < Z < +1.96) = 0.475 + 0.475 = 0.95


# In[ ]:





# ## Normalização dos dados
# 
# ![padr_variaveis.png](attachment:padr_variaveis.png)
# 

# In[3]:


# Importar os dados de ingestão de sal da Pesquisa Nacional de Saúde (PNS) 2013 do IBGE

sal = pd.read_excel(r'C:\Users\regin\FIAP\Shift\Imersao_Python\Turma3\trab2\sal_lab1.xlsx')


# In[4]:


sal.head()


# In[5]:


sal.info()


# In[6]:


sal.isna().sum()


# In[7]:


sal.describe()


# In[9]:


# Histograma da Ingestão de Sal

plt.hist(sal['Ingestao_Sal'])


# In[ ]:


# Análise descritiva da Ingestão de sal


# In[10]:


# Ingestão de Sal tem média 9,14g/dia e desvio padrão de 2.32g/dia

# Criar a variável z_score_sal com média 0 e variância igual a 1
sal['zscore_sal'] = (sal['Ingestao_Sal'] - 9.14)/2.32


# In[11]:


sal.head()


# In[12]:


sal.describe().round(2)


# In[13]:


# Gráfico histograma da Ingestão de Sal e Z_score_sal
plt.subplot(1,2,1)
plt.hist(sal['Ingestao_Sal'], bins=10)
plt.subplot(1,2,2)
plt.hist(sal['zscore_sal'], bins=10)


# In[ ]:





# In[14]:


# Criar a variável padronizada da Ingestão de Sal usando o critério do Máximo e Mínimo

sal['sal_normalizado'] = (sal['Ingestao_Sal'] -  1.13)/(28.28 - 1.13)


# In[15]:


sal.describe().round(2)


# In[17]:


# Fazer o gráfico histograma da Ingestão de Sal e sal_normalizada
plt.subplot(1,3,1)
plt.hist(sal['Ingestao_Sal'], bins=10)
plt.subplot(1,3,2)
plt.hist(sal['zscore_sal'], bins=10)
plt.subplot(1,3,3)
plt.hist(sal['sal_normalizado'], bins=10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




