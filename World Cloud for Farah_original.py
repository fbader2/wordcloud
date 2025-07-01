#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
from scipy.stats import stats
import plotly.graph_objects as go
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

get_ipython().run_line_magic('matplotlib', 'inline')

#file here
df = pd.read_csv(r"C:/Users/baderf/OneDrive - National Institutes of Health/WordCloudPythoniSearch/WordCloudsall11.25.24.csv")
#.csv file generated from running RePORTER search of all competing BRAIN Brain Circuit Program awards from 2014-2023


# In[ ]:


# Word cloud documentation is here; https://amueller.github.io/word_cloud/
# Select the data you want to use here, and filter as needed
df['test2']=df['Title']+" "+df['Abstract']
# df['test2']=df['PubMed Keywords']
# data=df.loc[df['Pub Year']==2022]

data=df

comment_words = ''
stopwords = set(STOPWORDS)

#Add any stop words you want
stopwords.update(["description", "narrative","result","propose",'aim','hypothesis',
                 'determine','contribute','system','proposed research','within','will','test','hypothesize','use','using',
                  'first','based','many','will provide','used','including','research','study','may','impact','cause',
                 'novel','due','important','relevant','find','results','lead','current','ad','goal','different','technique',
                 'well','area','proposed','allow','analysis','approach','approaches','target','identify','characterize',
                 'thus','address','work','finding','design','whether','change','role','spectific','work','novel','one','two',
                 'multipe','examine','investigate','application','enable','common','project','studie','proposal','establish',
                 'innovative','time','assess','second','first','innovative','major','image','currently','testing',
                  'understanding','across','measure','increased','complex','aims','although','increased','support',
                 'afect','effect','objectives','without','include','provide','level','developed','specific','studies',
                 'data','changes','disease','development','disorder','findings','state','related','significant','new',
                 'known','experiment','preliminary','three','third','control','effects','following','shown','associated',
                 'condition','show','overall','characterized','reduced','critical','number','evaluate','addition',
                 'use','method','using','within','demonstrate','any','apply','applying','reapplying','given','papers',
                  'paper','about','results','result','real','world','page','article','present','takes','account', 
                  'previous','work','propose','proposes','proposed','simply','simple','demonstrate','demonstrated',
                  'demonstrates','realworld','datasets','dataset','provide','important','research','researchers',
                  'experiments','experiment','unexpected','discovering','using','recent','collected','solve','columns',
                  'existing','traditional','final','consider','presented','provides','automatically','extracting',
                  'including','help','helps','explore','illustrate','achieve','better','data','nan','male','female', 'methods','suggests','human'])
 
# iterate through the csv file
for val in data.test2:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "

# Import image to np.array

#Set unique color pallet for your image
cmap = ListedColormap(["#0D3B66", "#457B9D", "#A8DADC","#0D3B66"])

#Set properties of the word cloud
wordcloud = WordCloud(width = 680, height = 300,
                colormap=cmap,
                background_color = "white",
                stopwords = stopwords,
                min_word_length =3,
                min_font_size = 10).generate(comment_words)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

#save here
plt.savefig('Users/baderf/OneDrive - National Institutes of Health/WordCloudPythoniSearch/WordCloudPythoisearch.png')
plt.show()

