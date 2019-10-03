#!/usr/bin/env python
# coding: utf-8

# # Домашнее задание hw_3

# #### Вебер Анастасия, БКЛ182

# Делалось совместно с Ликой Джиоевой и Машей Козловой из бкл182

# In[180]:


import json 
import collections
from collections import Counter
import re


# In[88]:


twitter = [] 
for line in open('hw_3_twitter.json'):
    twitter.append(json.loads(line)) # создание списка из строки json


# ### №1. Всего твитов в наборе:

# In[90]:


print(len(twitter)) 


# ### №2. Процент твитов, которые составляют удаленные записи

# In[170]:


pr = (sum('delete' in t for t in twitter)/len(twitter)) #отношение твитов с пометкой delete к общему числу твитов
print('Процент твитов, которые составляют удаленные записи -', round(pr*100, 2))


# ### №3. Самые популярные языки твитов:

# In[175]:


list1 = []
for i in range(len(twitter)):
    if 'user' in twitter[i]:
        list1.append(twitter[i]['lang'])
c = collections.Counter(list1)
d = c.most_common()
print('Самые популярные языки твитов:')
for i in range(5):
    print(i+1, '.' ,d[i][0])


# ### №4. Твиты от одного и того же пользователя, и их количество таких пользователей

# In[103]:


list2 = []
a = 0
for i in range(len(twitter)):
    if 'user' in twitter[i]:
        list2.append(twitter[i]['user']['id'])
for i in Counter(list2).most_common():
    if i[1] > 1:
        a += 1
if a == 0:
    print('Нет твитов от одного и того же пользователя')
else:
    print('Есть твиты от одного и того же пользователя, всего таких пользователей', a)


# ### №5. Топ-20 хэштегов

# In[121]:


list3 = []
for i in range(len(twitter)):
    if 'entities' in twitter[i]:
        if 'hashtags' in twitter[i]['entities']:
            for hash in twitter[i]['entities']['hashtags']:
                list3.append(hash['text'])
c3 = collections.Counter(list3)
d3 = c3.most_common()
print('Самые популярные хэштэги:')
for i in range(20):
    print(i+1,'.',d3[i][0])


# ### №6. Частотный словарь

# In[243]:


list = []
for i in twitter:
    if 'text' in i:
        if not 'retweeted_status' in i and i['lang'] == 'en':
            list.append(i['text'])
list = ' '.join(nr)
list = re.sub(r'[^\w\s]', '', list)
list = list.lower()
list = list.split()
c = collections.Counter(list)
d = c.most_common()
print('Самые частотные слова и количество их упоминаний')
for i in range(10):
    print(i+1,'.',d[i][0],'-', d[i][1])
print('Частотный словарь:')
print(d)


# ### №7. Количество подписчиков (фолловеров) у авторов твитов, топ-10

# In[169]:


dict = {}
for i in range(len(twitter)):
    if 'user' in twitter[i]:
        dict[twitter[i]['user']['name']] = twitter[i]['user']['followers_count'] 
c4 = collections.Counter(dict)
d4 = c4.most_common()
print('Самые популярные авторы и количество их подписчиков:')
for i in range(10):
    print(i+1,'.',d4[i][0],'-' ,d4[i][1])



# ### №8. Топ-10 источников твита

# In[230]:


list6 = []
for i in range(len(twitter)):
    if 'source' in twitter[i]:
        a = re.findall(r'>(.*?)<', twitter[i]['source'])
        list6.extend(a)
c5 = collections.Counter(list6)
d5 = c5.most_common()
print('Самые популярные источники твитов:')
for i in range(10):
    print (i+1,'.', d5[i][0])


# In[ ]:




