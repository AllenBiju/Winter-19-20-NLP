#!/usr/bin/env python
# coding: utf-8

# In[11]:



# 1. Lexical Source

# 1.1 Stopwords in english and one other laguage
from nltk.corpus import stopwords
eng = stopwords.words('english')
print(len(eng))
stopwords.words('german')


# In[55]:


# 1.2 CMU wordlist
import nltk
entries = nltk.corpus.cmudict.entries()
print(len(x))

for entry in entries[:50]:
    print(entry)
    


# In[43]:


# 1.3 Wordnet (for synonyms) 
from nltk.corpus import wordnet as wn
print(wn.synsets('elegant'))
wn.synset('elegant.s.02').lemma_names()


# In[93]:


# 1.4 part of speech tagging
import nltk
texts = ["""Adrien Nicholas Brody was born in Woodhaven, Queens, New York, the only child of retired history professor 
Elliot Brody and Hungarian-born photographer Sylvia Plachy. He accompanied his mother on assignments for the Village Voice, 
and credits her with making him feel comfortable in front of the camera. Adrien attended the American Academy of Dramatic Arts 
and LaGuardia High School for the Performing Arts in New York."""]

for t in texts:
    sentences = nltk.sent_tokenize(t)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        print(tagged_words)


# In[54]:


# 1.5 Tweet Tokenizer
import nltk
from nltk.tokenize import TweetTokenizer
text = """The TRASH 
@TheQuint
 has labelled A PATRIOTIC MOVIE of UNSUNG WARRIORS Of India as isIamophobic. Teach them a LESSON

WATCH #Tanhaji  AGAIN & AGAIN 🇮🇳🇮🇳 
JAI BHAVANI JAI SHIVAJI🚩🚩🚩🚩
I AM INDIAN , I AM NATIONALIST 🇮🇳🇮🇳
:D:D

#TanajiTheUnsungWarrior
#bycott #blockbusterTanhajiReviews"""
twtkn = TweetTokenizer()
wordstwtkn = twtkn.tokenize(text)
words = nltk.word_tokenize(text)
print(words)
print(wordstwtkn)


# In[31]:




# extra 
# tired to change the verbs, adjectives, adn adverbs of a given text into its synonyms


to_change = ["JJ","VB","RB"]
texts = ["""Standing on his hind legs, this rare andalucian stallion is fearless. 
His ears are turned back while his noble looking head is held high. His all black coat 
glistens in the late afternoon sun. His face displays a strong confidence with his 
nostrils flared, his veins bulging from his cheek bones, and his fiery black eyes burning holes 
into the souls of those who stare into them. His neck muscles are tensed and thickened with adrenalin. 
His black main is thrown into the wind like a flag rippling in the winds of a tornado. His muscular front legs are 
brought up to his chest displaying his flashing gray hooves that could crush a man's scull with one blow. His backbone and 
underbelly are held almost straight up and his hind quarters are tensed. His back legs are spread apart for balance. His 
back hooves are pressed into the earth; therefore, his hooves cause deep gouges from the weight of his body on the soil. 
His black tail is held straight down and every once in a while a burst of wind catches it and then it floats down back into
place like an elegant piece of silk falling from the sky. His bravery and strength are what made his breed prized as a warhorse."""]

import nltk
tagged_words =[]
for t in texts:
    sentences = nltk.sent_tokenize(t)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in list(nltk.pos_tag(words)):
            tagged_words.append(word) 


        


from nltk.corpus import wordnet as wn

new_s = []
for tagged_word in tagged_words:
#     print(tagged_word[1])
    if(tagged_word[1] in to_change):
        try:
            id = wn.synsets(tagged_word[0])[-1].name()
            new_s.append("  !!!" + str(wn.synset(id).lemma_names()[0])+"!!!   ")
        except:
            new_s.append(str(tagged_word[0]))
    else:
        new_s.append(str(tagged_word[0]))
    

print(texts)
print("\n\n")

print(" ".join(new_s))


# In[ ]:




