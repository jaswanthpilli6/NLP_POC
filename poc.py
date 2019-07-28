# Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
# import nltk
# nltk.download()


# %%
from bs4 import BeautifulSoup
import requests
import re

# https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

link = 'https://cdn.aws.singtel.com/annualreport/2019/pages/gceo-review.html'
the_page = requests.get(link).content
html_tags = BeautifulSoup(the_page, features="html.parser")

paragraphs = html_tags.findAll('p', {'class': ''})

article_text = ''
for p in paragraphs:
    article_text += ' ' + p.text

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# %%
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
import nltk

sentence_list = sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

# %%
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)
