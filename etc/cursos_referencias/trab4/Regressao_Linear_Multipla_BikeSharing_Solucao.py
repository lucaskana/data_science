#!/usr/bin/env python
# coding: utf-8

# ## PYTHON JOURNEY MACHINE & DEEP LEARNING
# ### Trabalho prático usando Python
#  
# ### Modelo de regressão linear múltipla

# Dataset Bike Sharing
# 
# Descrição: Os sistemas de compartilhamento de bicicletas são uma nova geração de aluguel de bicicletas tradicional, onde todo o processo de associação, locação e devolução tornou-se automático. Através destes sistemas, o usuário pode facilmente alugar uma bicicleta a partir de uma determinada posição e retornar em outra posição. Atualmente, existem cerca de 500 programas de compartilhamento de bicicletas em todo o mundo, compostos por mais de 500 mil bicicletas. Hoje, existe um grande interesse nesses sistemas devido ao seu importante papel no trânsito, questões ambientais e de saúde.
# 
# Fonte de dados: https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# 

# Dicionário de variáveis:
# - instant: ID
# - dteday: ID
# - season: (1:winter, 2=springer, 3:summer, 4:fall)
# - yr: year (0: 2011, 1:2012)
# - mnth: ( 1 to 12)
# - holiday (0=no;1=yes)
# - weekday (day of the week)
# - workingday (0=no;1=yes) 
# - weathersit (1: Clear, Few clouds , Partly cloudy, Partly cloudy; 2: Mist + Cloudy, Mist + Broken clouds, 
#               Mist + Few clouds, Mist;3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + 
#               Scattered clouds;4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) 
# - temp (Normalized temperature in Celsius). The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, 
#         t_max=+39 (only in hourly scale)
# - atemp (Normalized feeling temperature in Celsius). The values are derived via (t-t_min)/(t_max-t_min),
#    t_min=-16, t_max=+50 (only in hourly scale)
# - hum (Normalized humidity_. The values are divided to 100 (max)
# - windspeed	Normalized wind speed. The values are divided to 67 (max)
# - casual (count of casual users)
# - registered (count of registered users) 
# - cnt (count of total rental bikes including both casual and registered)
# 
# 
# ![dic_bike.png](attachment:dic_bike.png)
# 
# 

# In[ ]:


# Importar as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy.stats import pearsonr
import statsmodels.api as sm


# In[ ]:


# Importar a base de dados 
df=pd.read_csv('Bike_Sharing.csv')


# In[ ]:


# Visualizar os dados
df.head(10)


# In[ ]:


# Verificar os formatos das variáveis
df.info()


# In[ ]:


# Análise descritiva
df.describe().round(2)


# In[ ]:


# Pre-processing
# Mudar o formato da variável quantitativa em qualitativa
df['season']= df['season'].astype(str)
df['yr']= df['yr'].astype(str)
df['holiday']= df['holiday'].astype(str)
df['weekday']= df['weekday'].astype(str)
df['workingday']= df['workingday'].astype(str)
df['weathersit']= df['weathersit'].astype(str)
df['mnth']= df['mnth'].astype(str)


# In[ ]:


df.info()


# In[ ]:


df.describe().round(2)


# In[ ]:


# modificando os nomes das colunas
df.columns = ['ID', 'data', 'estacao','ano','mes', 'feriado','dia_semana','dia_util','clima', 'temperatura','sensacao_termica',
             'umidade','vel_vento','casual', 'registrada', 'total']


# In[ ]:


# Verificar os nomes das variáveis
# informações dos dados
df.info()


# In[ ]:


# Selecionar as variáveis quantitativas
var_num = ['temperatura','sensacao_termica','umidade','vel_vento', 'total']


# In[ ]:


# Selecionar as variáveis qualitativas
var_cat =['estacao','ano','mes', 'feriado','dia_semana','dia_util','clima']


# In[ ]:


# Análise descritiva: medidas resumo
df[var_num].describe().round(2)


# In[ ]:


# Análise exploratória dos dados usando o gráfico histograma
# Análise exploratória dos dados
features = var_num
fig,axs=plt.subplots(nrows=2, ncols=3, figsize=(18,10))
for col, ax in zip(features[0:], axs.ravel()):
    x=df.loc[:, col]
    sns.distplot(x, ax=ax, color="blue", kde=False)
    plt.subplots_adjust(top=0.92,bottom=0.08, left=0.10,right=0.95,hspace=0.25,wspace=0.4)


# In[ ]:


# Análise exploratória dos dados usando o gráfico Box Plot
# Análise exploratória dos dados
features = var_num
fig,axs=plt.subplots(nrows=2, ncols=3, figsize=(18,10))
for col, ax in zip(features[0:], axs.ravel()):
    x=df.loc[:, col]
    sns.distplot(x, ax=ax, color="blue", kde=False)
    plt.subplots_adjust(top=0.92,bottom=0.08, left=0.10,right=0.95,hspace=0.25,wspace=0.4)


# In[ ]:


# Análise das variáveis qualitativas

features = var_cat
fig,axs=plt.subplots(nrows=2, ncols=3, figsize=(18,10))
for col, ax in zip(features[1:], axs.ravel()):
    x=df.loc[:, col]
    sns.countplot(x, ax=ax, orient='v')
    plt.subplots_adjust(top=0.92,bottom=0.08, left=0.10,right=0.95,hspace=0.25,wspace=0.4)


# In[ ]:


# Análise exploratória dos dados
#sns.pairplot()
sns.pairplot(df[var_num])


# In[ ]:


# Gráfico de dispersão 


# ### Correlação de Pearson
# 
# ### Teste de hipótese
# ### H0: cprrelação = 0
# ### H1: correlação <> 0
# 
# ### erro decisão: 0,05 ou 5% --> nível de significância do teste de hipótese
# ### Critério de decisão:
# ### p-valor < critério de decisão --> rejeito H0
# ### p-valor < critério de decisão --> não rejeito H0
# 
# ### conclusão: p-valor < 0,05 --> logo existe correlação entre as duas variáveis

# In[ ]:


# Correlação entre CNT e Temperatura
sns.jointplot(x='temperatura', y='total', data=df, kind='reg')


# In[ ]:


# Correlação entre CNT e Sensação térmica


# In[ ]:


# Correlação entre CNT e Umidade
sns.jointplot(x='umidade', y='total', data=df, kind='reg')


# In[ ]:


#  Correlação entre CNT e Velocidade do vento


# In[ ]:


print('Correlação de Pearson entre o total de bikes alugadas e temperatura')
pearsonr(df['temperatura'], df['total'])


# In[ ]:


forca_corr = -0.10065856213715525*-0.10065856213715525
print(forca_corr)


# In[ ]:


# Matriz de correlação

sns.heatmap(df[var_num].corr(), cmap='coolwarm', annot = True)


# In[ ]:





# ## Análise bivariada

# In[ ]:


# Análise qiantitativa versus qualitativa
# Variáveis qualitativas
# Identificar se há associação entre CNT ( variável quantitativa) e Estação do ano (variável qualitativa)
# Box Plot
sns.boxplot(x='estacao', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Teste qui-quadrado é utilizado para descobrir associação entre duas variáveis qualitativas
# transformar a variável total de bikes alugadas em qualitativa --> faixa cnt (qualitativa ordinal) vs estação do ano (qualitativa ordinal)
# criar a faixa_cnt você usar os quartis 


# In[ ]:


# Box Plot
sns.boxplot(x='mes', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Box Plot
sns.boxplot(x='clima', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Box Plot
sns.boxplot(x='dia_semana', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Box Plot
sns.boxplot(x='feriado', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Box Plot
sns.boxplot(x='dia_util', y='total', data=df, palette = 'rainbow')


# In[ ]:


# Criar variáveis dummies para cada variável qualitativa e excluir a primeira categoria de cada variável
var_dummies = pd.get_dummies(df[var_cat], drop_first = True)
print(var_dummies)


# In[ ]:


df = pd.concat([df, var_dummies], axis=1)

print(df.head())


# In[ ]:


df.info()


# In[ ]:


df_copy  = df.copy()

df_copy= df_copy.drop(['ID', 'data','ano','mes', 'feriado', 'dia_util','estacao', 'dia_semana','clima', 
                       'casual', 'registrada'], axis=1)


# In[ ]:


df.head()


# ### Modelo de Regressão Linear Múltipla
# 
# ![regressao_multipla.png](attachment:regressao_multipla.png)

# In[ ]:


# Selecionar as variáveis preditoras e a resposta do modelo
# Selecionar as variáveis preditoras e a resposta do modelo
X = df[['estacao_2', 'estacao_3', 'estacao_4']]
y = df['total']


# ### Dividir a amostra em treino e validação

# In[ ]:


# Importar as bibliotecas
from sklearn.model_selection import train_test_split


# In[ ]:


# random_state é o número aleatório usado para sortear as amostras. O seu uso é opcional.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 101)


# In[ ]:


# Regressão linear múltipla
lm = LinearRegression()
lm.fit(X_train, y_train)


# In[ ]:


# Intercepto do modelo (b0)

print(lm.intercept_)


# In[ ]:


# Os coeficientes do modelo (b1,b2,b3)
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
coeff_df.round(3)


# In[ ]:


# Modelo Regressão Linear Múltipla
# Total = 2603.92 + 2318.023 * estacao_2 + 3079.203*estacao_3 + 2161.986* estacao_4


# In[ ]:


# Selecionar as variáveis preditoras e a resposta do modelo
X = df[['estacao_1', 'estacao_2', 'estacao_3']]
y = df['total']


# In[ ]:


# random_state é o número aleatório usado para sortear as amostras. O seu uso é opcional.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 101)


# In[ ]:


# Os coeficientes do modelo (b1,b2,b3)
lm = LinearRegression()
lm.fit(X_train, y_train)


# In[ ]:


# Intercepto do modelo (b0)

print(lm.intercept_)


# In[ ]:


# Os coeficientes do modelo (b1,b2,b3)
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
coeff_df.round(3)


# In[ ]:


# Selecionar as variáveis preditoras e a resposta do modelo
X = df[['estacao_1', 'estacao_2', 'estacao_3']]
y = df['total']


# ### Selecionar todas as variáveis preditoras no modelo

# In[ ]:


df_copy.info()


# In[ ]:


# Selecionar as variáveis preditoras e a resposta
X = df_copy.drop('total', axis=1)
y = df_copy['total']


# In[ ]:


# random_state é o número aleatório usado para sortear as amostras. O seu uso é opcional.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 101)


# In[ ]:


# importar bibliiotecas
import statsmodels.api as sm
from scipy import stats


# In[ ]:


#Modelo de regressão linear múltipla
X_ = sm.add_constant(X_train)
model = sm.OLS(y_train, X_).fit()
#results = model.fit()
print(model.summary())


# In[ ]:


# Importar a biblioteca
# Medidas de erro
from sklearn.metrics import mean_absolute_error, mean_squared_error


# In[ ]:


X_t = sm.add_constant(X_test)


# In[ ]:


# Calculando o valor predito da variável resposta na amostra treino e teste
y_train_pred = model.predict(X_)
y_test_pred  = model.predict(X_t)


# In[ ]:


y_train_pred


# In[ ]:


y_test_pred


# ### Medidas de erro
# 
# ![medidas_erros.png](attachment:medidas_erros.png)

# In[ ]:


# Medidas de erro na amostra treino
me1   = round((y_train-y_train_pred).mean(),2)
mae1  = (mean_absolute_error(y_train, y_train_pred)).round(2)
mse1  = (mean_squared_error(y_train, y_train_pred)).round(2)
rmse1  = (np.sqrt(mean_squared_error(y_train, y_train_pred))).round(2)
mpe1  = round(((y_train - y_train_pred)/y_train).mean(),2)
mape1  =  round((mae1/y_train).mean(),2) 


# In[ ]:


# Medidas de erro na amostra teste
me2   = round((y_test-y_test_pred).mean(),2)
mae2  = (mean_absolute_error(y_test, y_test_pred)).round(2)
mse2  = (mean_squared_error(y_test, y_test_pred)).round(2)
rmse2  = (np.sqrt(mean_squared_error(y_test, y_test_pred))).round(2)
mpe2  = round(((y_test - y_test_pred)/y_test).mean(),2)
mape2  =  round((mae2/y_test).mean(),2) 


# In[ ]:


list1 = [me1, mae1,mse1,rmse1,mpe1, mape1]
list2 = [me2, mae2,mse2,rmse2,mpe2, mape2]
pd.DataFrame({"treino":list1, "teste": list2})


# In[ ]:


## Conclusão dos resultados da amostra treino e teste
## (1) Note que o rmse1 e rmse2 estão próximos, esse resultado mostra que o modelo ajustado na amostra treino tem desempenho
## semlhante na amostra teste. Ou seja, não tem problema de overfitting ou underfitting.
## (2) o mape1 e mape2 estão próximos, ou seja, o erro da  modelo é 22% na amostra treino e 17% na amostra teste. O mape informa
## o erro percentual da quantidade de bikes alugadas.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




