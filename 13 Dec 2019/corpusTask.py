#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[8]:


nltk.download()


# In[27]:


from nltk.corpus import brown


# In[33]:

# Categories availabel in brown corpus
cat = brown.categories()
brown.words(categories = "adventure")[:100]


# In[35]:


from nltk.corpus import inaugural


# In[43]:

# American president inaugural speeches
inaugural.fileids()


# In[49]:


" ".join(inaugural.words(fileids = "2017-Trump.txt")[:100])


# In[51]:


from nltk.book import *


# In[66]:


f = FreqDist(inaugural.words(fileids = "1977-Carter.txt"))
f.most_common(20)

