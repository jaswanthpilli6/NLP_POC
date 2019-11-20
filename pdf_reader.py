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

KEY_RATIOS = ['sales', 'revenue', 'operating expense', 'gross margin', 'operating margin', 'gearing', 'ebitda',
              'net profit']

KEY_PHRASE = ['due to', 'because', 'as a result', 'impacted by']

non_ascii_char = {''}
non_ascii_context = {''}

def remove_non_ascii(text):
    result = ''.join([i if ord(i) < 128 else ' ' for i in text])

    non_ascii_char_list = [i if not ord(i) < 128 else '' for i in text]
    non_ascii_char.update(non_ascii_char_list)

    return result


def read_full_pdf(fname):
    pdfFileObj = open(fname, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("Total pages in file", pdfReader.numPages)


    full_text = ''
    for i in range(pdfReader.numPages):
        text = pdfReader.getPage(i).extractText()
        text = remove_non_ascii(text)
        tmp = ' '.join(text.split())
        full_text = full_text + tmp + ' '

    return full_text


full_text = read_full_pdf('AR_2017.pdf')
print(non_ascii_char)

sentences = sent_tokenize(full_text)

def find_sentences_with_key_word(sentences):
    result = {}
    for key in KEY_RATIOS:
        filtered = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if sentence_lower.find(key) > -1:
                filtered.append(sentence)
        result[key] = filtered

    return result


result = find_sentences_with_key_word(sentences)

print(result)



