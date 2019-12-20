#!/usr/bin/env python
# coding: utf-8

# In[6]:


from nltk.corpus import webtext


# In[7]:


webtext.fileids()


# In[8]:


print(webtext.words(fileids = 'pirates.txt'))


# In[9]:


for file in webtext.fileids():
    print(webtext.words(fileids = file)[:20])

