#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('apt-get install libproj-dev proj-data proj-bin')
get_ipython().system('apt-get install libgeos-dev')
get_ipython().system('pip install cython')
get_ipython().system('pip install cartopy')

get_ipython().system('apt-get -qq install python-cartopy python3-cartopy')
get_ipython().system("pip uninstall -y shapely    # cartopy and shapely aren't friends (early 2020)")
get_ipython().system('pip install shapely --no-binary shapely')


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from matplotlib import cm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs                   # for projections
import cartopy.feature as cfeature           # for features
import cartopy.io.shapereader as shapereader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.feature.nightshade import Nightshade


# In[11]:


DataTran = pd.read_csv('../content/datatran2020.csv',sep = ';',encoding='latin-1',decimal=',')





# In[15]:


print(DataTran.latitude[2]+DataTran.longitude[2])
x = DataTran.longitude[:100]
y = DataTran.latitude[:100]
plt.scatter(x, y, marker='.',picker=True)
plt.show()


# In[19]:


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.set_extent([-90, -10, -60, 15], ccrs.PlateCarree())
ax.scatter(x, y)

ax.coastlines()


# In[26]:


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.set_extent([-82, -30, -55, 15], ccrs.PlateCarree())
ax.scatter(x, y)

ax.coastlines()

