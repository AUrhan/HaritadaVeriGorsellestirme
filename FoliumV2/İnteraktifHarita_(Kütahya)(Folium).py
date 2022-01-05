#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Gerekli kütüphanelerin Jupyter Sistemine yüklenmesi
get_ipython().system('pip install folium')
get_ipython().system('pip install requests')
get_ipython().system('pip install branca')
get_ipython().system('pip install pandas')


# In[2]:


# Yüklenen kütüphanelerin kullanılan 'Notebook'ta' aktif edilmesi
import folium
import requests
import pandas
import branca
import branca.colormap as cm


# In[3]:


# M değişkenine tanımlanarak Folium ile belirtilen koordinata haritalama yapılması.
m = folium.Map(location=[39.2149, 29.8703],
        zoom_start=8,
        tiles='OpenStreetMap',
        attr='KÜTAHYA VE İLÇELERİ NÜFUS HARİTASI')
# geojson değişkeniyle Haritası çizilen şehrin github üzerinden 'GeoJson' dosyasının okutulması.
geojson = r"https://raw.githubusercontent.com/AUrhan/kth-hrt-python/main/kut.geojson"
# Çizilen haritanın folium haritasına entegrasyonu ve gerekli sütünlardan verilerin okutulması
g = folium.GeoJson(
    geojson,
    name = 'geojson',
).add_to(m)

folium.GeoJsonTooltip(fields=["YER","TOPLAM","ERKEK","KADIN","ÇOCUK"]).add_to(g)

# Colormap, Minimap eklenmesi
colormap = cm.LinearColormap(colors=['black','darkblue', 'blue', 'lightblue', 'cyan', 'lightgreen', 'green', 'yellow', 'orange', 'red'],
                             index=[3, 5, 7, 10, 15, 20, 50, 60, 100, 200 ], vmin=0, vmax=100,
                             caption='Toplam Popülasyon  (x1000)')

from folium import plugins

minimap = plugins.MiniMap()
m.add_child(minimap)
m.add_child(colormap)
m


# In[ ]:




