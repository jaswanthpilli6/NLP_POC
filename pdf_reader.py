import PyPDF2
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag

import heapq

import json
import pkg_resources

from symspellpy.symspellpy import SymSpell

KEY_RATIOS = ['sales', 'revenue', 'operating expense', 'gross margin', 'operating margin', 'gearing', 'ebitda', 'net profit']

KEY_PHRASE = ['due to', 'because', 'as a result', 'impacted by']

def read_full_pdf(fname):
    pdfFileObj = open(fname, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("Total pages in file", pdfReader.numPages)
    full_text = ''
    for i in range(pdfReader.numPages):
        text = pdfReader.getPage(i).extractText()
        tmp = ' '.join(text.split())


# print(text)
