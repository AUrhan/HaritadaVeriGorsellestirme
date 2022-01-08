#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Gerekli Kütüphanenin Yüklenmesi
get_ipython().system('pip install matplotlib ')


# In[7]:


# Kütüphaneden Gerekli Araçların Çağırılması
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Değişkenler ile Grafiğin Boyutu ve Türünün Ayarlanması
fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, projection='3d')

# X / Y / Z Değerlerinin Girilmesi
X=[95821, 5568, 3106, 2148, 5114, 1036, 6866, 17506, 4139, 1717 ,21883, 2056, 35811]
Y=[100064, 5814, 3244, 2244, 5341, 1081, 7170, 18281, 4323, 1793, 22853, 2148, 37397]
Z=[71523, 4156, 2319, 1604, 3817, 773, 5125, 13067, 3090, 1282, 16335, 1535, 26731]


# Scatter Formatında 3D Modelin Oluşturulup Her Değer İçin Ayrı Renk Tanımlaması Yapılması
surf = ax.scatter(X,Y,Z, 
           c=["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"],
           marker='*')
# Düzlemlere İstenen Başlığın Verilmesi Ve Grafiğin Başlıklandırılması / Başlıkların Renklendirilmesi
ax.set_xlabel('ERKEK NÜFUS', size = 15, c='b')
ax.set_ylabel('KADIN NÜFUS', size = 15, c='b')
ax.set_zlabel('ÇOCUK NÜFUS', size = 15, c='b')

plt.title("NÜFUS DAĞLIMI", size = 25, c='black')

# X / Y / Z Düzlemlerinin Arkaplan Renginin Değiştirilmesi 
# (Veri Dağınık Olmadığı İçin Renk Farklılıkları ve Değişimleri Net Görülememektedir)
ax.w_xaxis.set_pane_color((0.7, 0.7, 0.7, 0.7))
ax.w_yaxis.set_pane_color((0.7, 0.7, 0.7, 0.7))
ax.w_zaxis.set_pane_color((0.7, 0.7, 0.7, 0.7))

# Color Bar eklenmesi / Tablonun "Grafik" adıyla".png" formatında kaydedilmesi (Binder Kısmında Olacaktır)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("Grafik.png")
plt.show()


# In[ ]:




