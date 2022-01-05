#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Kütüphanelerin yüklenmesi
get_ipython().system('pip install geopandas')
get_ipython().system('pip install folium')


# In[6]:


# Yüklenen kütüphanelerin kullanılan 'Notebook'ta' aktif edilmesi
import pandas as pd
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import numpy as np


# In[7]:


# data değişkeni ile verilerimizin olduğu CSV doyasının Okunması
data = pd.read_csv('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kth.csv')
data.head()


# In[8]:


# kut adlı değişkenle Kütahya Haritasının Yazdırılması
kut = gpd.read_file('https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kut.geojson')
kut.plot()


# In[56]:


# Haritanın Toplam Nüfus Verisi İle Renklendirilmesi ve Colorbar eklenmesi
ax=kut.plot(
    column="TOPLAM",
    legend=True,
    legend_kwds={'label': "İLÇELER TOPLAM NUFÜS DAĞILIMI",'orientation': "vertical"},
    figsize=(15, 10),
    missing_kwds={
        "color": "lightgrey",
        "edgecolor": "red",
        "hatch": "///",
        "label": "Missing values",
    },
);

# Oluşturulan Haritaya Başlık eklenmesi
ax.set_title('Kütahya Nüfus Haritası', fontdict={'fontsize':20}, pad=12.5,)


# In[ ]:




