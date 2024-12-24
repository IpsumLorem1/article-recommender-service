#!/usr/bin/env python
# coding: utf-8

# In[2]:


!pip install faiss-cpu

# In[3]:


import faiss
import numpy as np

# Загрузка эмбеддингов статей
article_embeddings = np.load("article_embeddings.npy")
d = article_embeddings.shape[1]

# Нормализуем эмбеддинги (для косинусного сходства)
faiss.normalize_L2(article_embeddings)

# Создаем индекс для косинусного расстояния
index = faiss.IndexFlatIP(d)
index.add(article_embeddings)

faiss.write_index(index, "faiss_index.idx")
