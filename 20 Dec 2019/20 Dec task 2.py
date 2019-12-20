#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
f = open('C://Users//Allen Biju Thomas//Desktop//MASC-3.0.0//MASC-3.0.0//data//written//twitter//tweets1.txt','r')
text = f.read()     # read from file


# In[9]:


text1 = text.split()
print(text1[:10])
text2 = nltk.Text(text1)    #convert to nltk readble text
print(text2)
text2.concordance("wondering")      #show word in context


# In[20]:


from urllib import request
url = "https://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)     # Web request for the url
raw =  response.read().decode('utf-8')

from nltk.tokenize import  word_tokenize
tokens = word_tokenize(raw)     # split to tokens
print(len(tokens))
print(tokens[:20])

