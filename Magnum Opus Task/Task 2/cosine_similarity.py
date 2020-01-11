
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pandas as pd
import numpy
import scipy
from nltk.stem.snowball import SnowballStemmer

stop_words = set(stopwords.words('english'))

filtered_words=[]
folder_path = "C:\\Users\\Allen Biju Thomas\\Desktop\\Winter-19-20-NLP\\Magnum Opus Task\\Task 2"
file_list = os.listdir(folder_path)
doc_list = []
for i in file_list:
        if ".txt" in i:
                doc_list.append(i)

for iteration in range(2):
    vectorised_words = {}
    temp_filtered_words = []
    for i in doc_list:
            doc_path = folder_path+"\\"+i
            f=open(doc_path,"r").read()
            word_tokens = word_tokenize(f.lower())
            stemmer = SnowballStemmer("english")
            for word in word_tokens:
                    if word not in stop_words:
                        if iteration == 1:
                            word = stemmer.stem(word)
                        filtered_words.append(word)
                        temp_filtered_words.append(word)
            vectorised_words.update({i :temp_filtered_words})
            temp_filtered_words = []

    temp = set(filtered_words)
    unique_filtered_words = list(temp)


    dict = {}
    dict.update({"Document":doc_list})

    for i in unique_filtered_words:
        dict.update({i:[]})


    dframe = pd.DataFrame

    for i in doc_list:
        for j in unique_filtered_words:
            dict[j].append(vectorised_words[i].count(j))
            

    dframe  = pd.DataFrame(dict)
    dframe.set_index('Document',inplace = True)

#    print(dframe)
    no_stemming_similarity_dict  = {}
    stemming_similarity_dict  = {}
    
    for i in doc_list:
        stemming_similarity_dict.update({i : {}})
        no_stemming_similarity_dict.update({i : {}})

    if(iteration == 1):
        for i in doc_list:
            for j in doc_list:
                stemming_similarity_dict[i].update({j : 100*(1-scipy.spatial.distance.cosine(dframe.loc[i].values,dframe.loc[j].values))})
        
        stemming_similarity_dframe = pd.DataFrame(stemming_similarity_dict)
        print("\nsimilarity between documents with stemming: ")
        print(stemming_similarity_dframe)
        print("\n");
    else:
        for i in doc_list:
            for j in doc_list:
                no_stemming_similarity_dict[i].update({j : 100*(1-scipy.spatial.distance.cosine(dframe.loc[i].values,dframe.loc[j].values))})
        
        no_stemming_similarity_dframe = pd.DataFrame(no_stemming_similarity_dict)
        print("\nsimilarity between documents without stemming: ")
        print(no_stemming_similarity_dframe)
        print("\n");


# print("Difference in similarity with stemming: "+ str(stemming_similarity-no_stemming_similarity))