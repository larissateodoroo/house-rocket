#!/usr/bin/env python
# coding: utf-8

# # 0.0 Imports

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import datetime

from matplotlib import pyplot as plt
import plotly.express as px


# ## 0.1 LOAD DATASET

# In[2]:


data = pd.read_csv('kc_house_data.csv')


# In[3]:


data.head()


# # 1.0 RESPONDENDO AS PERGUNTAS DO CEO

# ### 1. Quantas casas estão disponíveis para compra?

# In[4]:


houses = len( data['id'].unique() )
print('o numero de casas disponiveis é de {}' .format(houses))


# ### 2. Quantos atributos as casas possuem?

# In[5]:


atributos = len( data.drop( (['id','date']), axis=1 ).columns)
print('o numero de atributos é de {}' .format(atributos))


# ### 3. Quais são os atributos das casas?

# In[6]:


df = data.drop( (['id','date']), axis=1 ).columns
df


# ### 4. Qual a casa mais cara ( casa com o maior valor de venda )?

# In[7]:


house_expensive = data[['id','price']].sort_values('price', ascending = False). loc[0, 'id']
house_expensive


# ### 5. Qual a casa com o maior número de quartos?

# In[8]:


df= data[['id', 'bedrooms']].sort_values('bedrooms', ascending = False)
df


# ### 6. Qual a soma total de quartos do conjunto de dados?

# In[9]:


data['bedrooms'].sum()


# ### 7. Quantas casas possuem 2 banheiros?
# 

# In[10]:


df = data.loc[data ['bathrooms'] == 2, :]
num_houses = len (df)
num_houses


# ### 8. Qual o preço médio de todas as casas no conjunto de dados?

# In[11]:


avg_price = np.round ( data ['price'].mean(), 2)
avg_price


# ### 9. Qual o preço médio de casas com 2 banheiros?

# In[12]:


avg_price = np.round( data.loc[data ['bathrooms'] == 2, 'price'].mean(), 2)
avg_price


# ### 10. Qual o preço mínimo entre as casas com 3 quartos?

# In[13]:


min_price = np.round( data.loc[data ['bedrooms'] == 3, 'price'].min(), 2)
min_price


# ### 11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?

# In[14]:


houses = data.loc[data ['sqft_living'] > 300, 'id'].shape [0]
houses


# ### 12. Quantas casas tem mais de 2 andares?

# In[15]:


houses = data.loc[data ['floors'] > 2, 'id'].shape [0]
houses


# ### 13. Quantas casas tem vista para o mar?
# 

# In[16]:


houses = data.loc[data ['floors'] ==1, 'id'].shape [0]
houses


# ### 14. Das casas com vista para o mar, quantas tem 3 quartos?

# In[17]:


houses = data.loc[(data['waterfront'] == 1) & (data['bedrooms'] > 2), 'id'].shape[0]
houses


# ### 15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
# 

# In[18]:


houses = data.loc[(data['sqft_living'] > 300) & (data['bathrooms'] > 2), 'id'].shape[0]
houses


# In[19]:


data.dtypes


# In[20]:


data['date'] = pd.to_datetime( data['date'], format='%Y-%m-%d')


# In[21]:


data.dtypes


# In[ ]:




