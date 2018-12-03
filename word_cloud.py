def text_mining(city):
    import pandas as pd
    import numpy as np
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    import nltk
    from nltk.corpus import stopwords
    stopwords = list(stopwords.words('english'))
    from collections import Counter 

    
    path = './raw_data/'
    try:
        path_all = path + 'business analyst-' + str(city) + '-job-results-desc.csv'
        data = pd.read_csv(path_all)
    except:
        try:
            city = str(city).lower()
            data = pd.read_csv(path_all)
        except:
            return "please input city names beginning with an Uppercase character"
        
    data.head()
    desc = data['Description']
    text_list = []
    text_str = ''

    for i in range(len(desc)):
        text_str += str(desc[i])
    
    #texts = text_str
    
#     def remove_words(text_string,DELETE_WORDS=stopwords):
#         for word in text_string.split():
#             for stop in stopwords:
#                 if word in stop:                
#                     text_string = text_string.replace(word,' ')
#         return text_string
    
#    text_string = remove_words(text_str)
    
    unsign_words=['experience', 'work','support','ability','project','information','·','skills','years','including',
             'new','process','working','systems','requirements','related','provide','knowledge','reporting',
             '&','position','key','strong','solutions','degree','development','role','opportunity','projects',
             'job','across','system','develop','internal','processes','drive','complex','ensure','uw','required',
             'required','well','multiple','and/or','within','help','application','company','understanding',
             'operations','may','equal','environment','best','using','senior','-','tools','design','use','user',
             'identify','sales','must','manege','quality','skills','office','/','responsible','program',
             'responsibilities','based','functional','candidate','employment','time','performance','effectively','looking',
             'also','needs','*','opportunities','build','+','written','maintain','one',
             'provides','various','professional','make','•','operational','include','able','high','understand','us','insights',
             'people','building','meet','issues','create','duties','providing','status','large','employees','excellent','deliver',
             'successful','planning','problem','implementation','part','compliance','problems','equivalent',
             'critical','improvement','advanced','perform','effective','industry','benefits','variety','level',
             'verbal','existing','external','change','impact','highly','join','department','diverse','access','supporting',
             'growth','organization','staff','appropriate','health']
#    text_string = remove_words(text_str,unsign_words )
    del_word =unsign_words + stopwords
    


#     data_set = text_string
#     split_it = data_set.lower().split() 
#     Counter = Counter(split_it) 
#     most_occur = Counter.most_common(200)
    text = text_str
    wordcloud = WordCloud(stopwords=del_word,background_color='white',width=6000,height=6000).generate(text)

    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
     