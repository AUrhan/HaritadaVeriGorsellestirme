#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Gerekli Kütüphanelerin Yüklenmesi
get_ipython().system('pip install folium')
get_ipython().system('pip install requests')
get_ipython().system('pip install branca')
get_ipython().system('pip install pandas')


# In[2]:


# Kütüphanelerim çalıştırılması
import folium
import requests
import pandas
import branca
import branca.colormap as cm


# In[18]:


# M değişkenine haritanın koordinatını atayıp üzerine verileri gösterecek noktaları ve çevresindeki çemberi ekleme
m = folium.Map(location=[39.4200, 29.9857])
folium.Marker(location=[39.4200, 29.9857], tooltip=" Kütahya-Toplam Nufüs: 572500", popup = 'Kişi Başına Gelir: 11.661.200').add_to(m)
folium.Marker(location=[39.5470, 29.4914], tooltip=" Tavşanlı-Toplam Nufüs: 101848", popup = 'Kişi Başına Gelir: 870.660').add_to(m)
folium.Marker(location=[39.0580, 30.1086], tooltip=" Altıntaş-Toplam Nufüs: 15835", popup = 'Kişi Başına Gelir: 563.811').add_to(m)
folium.Marker(location=[39.2149, 29.8703], tooltip=" Aslanapa-Toplam Nufüs: 8834", popup = 'Kişi Başına Gelir: 110.635').add_to(m)
folium.Marker(location=[39.1969, 29.6172], tooltip=" Çavdarhisar-Toplam Nufüs: 6110", popup = 'Kişi Başına Gelir: 161.203').add_to(m)
folium.Marker(location=[39.8010, 29.6127], tooltip=" Domaniç-Toplam Nufüs: 14545", popup = 'Kişi Başına Gelir: 613.816').add_to(m)
folium.Marker(location=[38.8552, 29.9762], tooltip=" Dumlupınar-Toplam Nufüs: 2945", popup = 'Kişi Başına Gelir: 331.563').add_to(m)
folium.Marker(location=[39.3444, 29.2579], tooltip=" Emet-Toplam Nufüs: 19528", popup = 'Kişi Başına Gelir: 457.187').add_to(m)
folium.Marker(location=[38.9929, 29.4012], tooltip=" Gediz-Toplam Nufüs: 49787", popup = 'Kişi Başına Gelir: 179.323').add_to(m)
folium.Marker(location=[39.2465, 29.2359], tooltip=" Hisarcık-Toplam Nufüs: 11772", popup = 'Kişi Başına Gelir: 358.406').add_to(m)
folium.Marker(location=[38.9953, 29.1215], tooltip=" Pazarlar-Toplam Nufüs: 4884", popup = 'Kişi Başına Gelir: 182.800').add_to(m)
folium.Marker(location=[39.0896, 28.9787], tooltip=" Simav-Toplam Nufüs: 62237", popup = 'Kişi Başına Gelir: 143.451').add_to(m)
folium.Marker(location=[39.0249, 29.2201], tooltip=" Şaphane-Toplam Nufüs: 5850", popup = 'Kişi Başına Gelir: 152.614').add_to(m)


folium.CircleMarker(location=(39.4200, 29.9857),radius=100, fill_color='red').add_to(m)
folium.CircleMarker(location=(39.5470, 29.4914),radius=80, fill_color='red').add_to(m)
folium.CircleMarker(location=(39.0580, 30.1086),radius=80, fill_color='yellow').add_to(m)
folium.CircleMarker(location=(39.2149, 29.8703),radius=75, fill_color='black').add_to(m)
folium.CircleMarker(location=(39.1969, 29.6172),radius=75, fill_color='blue').add_to(m)
folium.CircleMarker(location=(39.8010, 29.6127),radius=50, fill_color='orange').add_to(m)
folium.CircleMarker(location=(38.8552, 29.9762),radius=50, fill_color='lightgreen').add_to(m)
folium.CircleMarker(location=(39.3444, 29.2579),radius=50, fill_color='green').add_to(m)
folium.CircleMarker(location=(38.9929, 29.4012),radius=70, fill_color='lightblue').add_to(m)
folium.CircleMarker(location=(39.2465, 29.2359),radius=50, fill_color='lightgreen').add_to(m)
folium.CircleMarker(location=(38.9953, 29.1215),radius=40, fill_color='cyan').add_to(m)
folium.CircleMarker(location=(39.0896, 28.9787),radius=80, fill_color='darkblue').add_to(m)
folium.CircleMarker(location=(39.0249, 29.2201),radius=40, fill_color='blue').add_to(m)

# Colorbar ekleme
colormap = cm.LinearColormap(colors=['black','darkblue', 'blue', 'lightblue', 'cyan', 'lightgreen', 'green', 'yellow', 'orange', 'red'],
                             index=[10, 12, 15, 18, 20, 30, 40, 50, 60,70 ], vmin=10, vmax=75,
                             caption='Kişi Başına Gelir x10000')
# Minimap ekleme ve Colorbarı görselleştirme
from folium import plugins

minimap = plugins.MiniMap()
m.add_child(minimap)
m.add_child(colormap)
m


# In[ ]:




