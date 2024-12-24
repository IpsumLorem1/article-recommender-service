#!/usr/bin/env python
# coding: utf-8

# In[56]:


import kagglehub
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

# In[ ]:


path = kagglehub.dataset_download("fabiochiusano/medium-articles")

# In[23]:


df = pd.read_csv('/kaggle/input/medium-articles/medium_articles.csv')

# In[50]:


df.head()

# In[25]:


df.info()

# #### Очистка и подготовка текста

# In[26]:


df['full_text'] = df['title'] + " " + df['text']

# In[27]:


df['full_text'] = df['full_text'].fillna("")

# In[28]:


df['full_text'] = df['full_text'].str.strip()

# #### Генерация эмбедингов

# In[55]:


!pip install sentence-transformers

# In[30]:


from sentence_transformers import SentenceTransformer

# In[34]:


model = SentenceTransformer('all-MiniLM-L6-v2')

# In[37]:


batch_size = 64

texts = df['full_text'].tolist()
embeddings = []

for i in range(0, len(texts), batch_size):
    batch = texts[i:i + batch_size]
    batch_embeddings = model.encode(batch)
    embeddings.extend(batch_embeddings)

# In[51]:


article_embeddings = np.vstack(embeddings)

# In[ ]:


np.save("article_embeddings.npy", article_embeddings)

# In[53]:


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

embeddings_matrix = article_embeddings
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings_matrix)

plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], alpha=0.5)
plt.title("PCA для эмбедингов статей")
plt.show()
