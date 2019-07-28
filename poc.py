# %%
from bs4 import BeautifulSoup
import requests

# https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

link = 'https://cdn.aws.singtel.com/annualreport/2019/pages/gceo-review.html'
the_page = requests.get(link).content
html_tags = BeautifulSoup(the_page, features="html.parser")

paragraphs = html_tags.findAll('p', {'class': ''})

p2_text = paragraphs[1].text

# %%
# import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

tokens = word_tokenize(p2_text)
print(tokens)
