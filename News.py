#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:47:26 2022

@author: hunchoahmad
"""

import pprint
import requests

from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import wordcloud
import pandas as pd


from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import tkinter as tk

import requests


secret = '4da3193c36db4a0a944a6585cxxxxxx'

url = 'https://newsapi.org/v2/everything?'
parameters = {
    'q': 'Elon Musk', # query phrase
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}
response = requests.get(url, params=parameters)

# Convert the response to JSON format and pretty print it
response_json = response.json()
pprint.pprint(response_json)

output  = response_json['articles']
List_Url = []
for i in range (0 , 5):
    List_Url.append(output[i]['url'])
    i+=1
    
for status in output:
    dict_ = {'Title':[],'Author':[],'Publication_Date':[]}
for status in output:
    dict_["Title"].append(status["content"])
    dict_["Author"].append(status["author"])
    dict_["Publication_Date"].append(status["publishedAt"])

    
df = pd.DataFrame(dict_)
df
    
    
pbb = df["Publication_Date"].to_list()
auth = df["Author"].to_list()

authc = [len(au) for au in auth]



plt.plot(pbb,authc)
plt.xticks(rotation=90)
plt.show()



from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import tkinter as tk
from newspaper import Article

for i in range(0 , len(List_Url)):

    article = Article(List_Url[i])
    article.download()
    article.parse()
    article.nlp()
    print(f'Title:{article.title}')
    print(f'Authors:{article.authors}')
    print(f'Publication Date:{article.publish_date}')
    print(f'Summary:{article.summary}')
    analyse = TextBlob(article.text)
    print(analyse.sentiment)
    i+= 1
    
 from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import tkinter as tk
from newspaper import Article
Text_List=[]
for i in range(0 , len(List_Url)):

    article = Article(List_Url[i])
    article.download()
    article.parse()
    article.nlp()
    Text_List.append(article.text)  
    
import nltk
for i in range(0 , 5):
    Text_List[i]
    sentences = nltk.sent_tokenize(Text_List[i])
    Words= nltk.word_tokenize(Text_List[i])
    j=0
    for sentence in sentences:
        j+=1
    print("Article sentences:",i , j )
    K=0
    for word in Words:
        K+=1
    print("Article Words", i , K)
    i+=0
    
 from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import wordcloud
import pandas as pd
stop_words = set(stopwords.words("english"))

Words =nltk.word_tokenize(Text_List[4])
filtered_words= []
for w in Words:
    if w not in stop_words:
        filtered_words.append(w)

for i in range(0 , len(filtered_words)):
    filtered_words[i] = filtered_words[i].lower()

frequency_dist = nltk.FreqDist(filtered_words)


sorted(frequency_dist, key=frequency_dist.__getitem__, reverse= True)[0:30]
large_words = dict([(k,v) for k , v in frequency_dist.items() if len(k) > 3 ] )

frequency_dist = nltk.FreqDist(large_words)
frequency_dist.plot(30,cumulative=False)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud(max_font_size=50, max_words=100,
background_color="black").generate_from_frequencies(frequency_dist)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
    
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
documents = Text_List[3].splitlines()
count_vectorizer = CountVectorizer()
bag_of_words =count_vectorizer.fit_transform(documents)
feature_names = count_vectorizer.get_feature_names()
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names))


from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
tfidf_vectorizer = TfidfVectorizer()
values = tfidf_vectorizer.fit_transform(documents)
feature_names =tfidf_vectorizer.get_feature_names()
TFIDF_matrix = pd.DataFrame(values.toarray() , columns= feature_names)
print(TFIDF_matrix)


#LSA Modelling

from gensim.models import LsiModel
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt
def load_data(path,file_name):
    documents_list=[]
    titles=[]
    with open(os.path.join(path, file_name),"r", encoding="utf-8") as fin:
       for line in fin.readlines():
           text = line.strip()
           documents_list.append(text)
           print("Total Number of Documents:", len(documents_list))
           titles.append(text[0:min(len(text),100)])
           return documents_list,titles
       
def preprocess_data(doc_set):
    
    
    # intialize regex tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # Create English stop words list
    en_stop=set(stopwords.words('english'))
    # Create p_stemmerof class PorterStemmer
    p_stemmer = PorterStemmer()
    # list for tokenized documents in loop
    texts = []
    # loop through document list
    for i in doc_set:
    # clean and tokenize document string
        raw = i.lower()
        tokens=tokenizer.tokenize(raw)
    # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
    # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    # add tokens to list
        texts.append(stemmed_tokens)
    return texts
    
def prepare_corpus(doc_clean):
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary=corpora.Dictionary
    dictionary=corpora.Dictionary(doc_clean)
    #converting list of documents (corpus) into Document term Matrix using dictionary prepared above.
    doc_term_matrix=[dictionary.doc2bow(doc) for doc in doc_clean]
    # generate LDA model
    return dictionary,doc_term_matrix

def create_gensim_lsa_model(doc_clean,number_of_topics,words):
    dictionary,doc_term_matrix=prepare_corpus(doc_clean)
    # generate LSA model
    lsamodel = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary) # train model
    print(lsamodel.print_topics(num_topics=number_of_topics, num_words=words))
    return lsamodel


    # LSA Model
number_of_topics=3
words=10
document_list,titles=load_data("", "em3.txt")
clean_text=preprocess_data(document_list)
model=create_gensim_lsa_model(clean_text, number_of_topics, words)