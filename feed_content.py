#!/usr/bin/env python2
"""
Extract words,phrases from description and feed into my content.
"""
import task_settings
import shelve

d = shelve.open(task_settings.get_path()+"database")
data = []
for k in d.keys():
    data.append(d[k]['description'])
d.close()

da = open(task_settings.get_path()+"words_list.txt")
common_words = da.read().split('\n')
da.close()

    
def extract_words(text):
    #remove commonly used words
    mywords = text.split(' ')
    words = [w for w in mywords if(w not in common_words)]
    print words

for text in data:
    words = extract_words(text)
    #a list of words
#    generate_feed(words)

