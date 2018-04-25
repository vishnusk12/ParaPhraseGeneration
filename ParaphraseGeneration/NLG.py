# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:39:04 2018

@author: Vishnu
"""

from textblob import Word, TextBlob
from textblob.wordnet import NOUN, VERB, ADV, ADJ
import spacy

nlp = spacy.load('en')

# langs = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 
#          'ca', 'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'nl', 'eo', 
#          'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 
#          'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 
#          'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 
#          'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 
#          'no', 'ny', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 
#          'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 
#          'sv', 'tl', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 
#          'cy', 'xh', 'yi', 'yo', 'zu']

# def paraphrases(text):
#     txt = TextBlob(text)
#     paraphrase = []
#     for i in langs:
#         try:
#             tran = txt.translate(to=i)
#             para = tran.translate(to="en")
#             paraphrase.append(str(para).lower())
#         except:
#             pass
#     paraphrase = list(set(paraphrase))
#     final = []    
#     for i in paraphrase:
#         if nlp(text).similarity(nlp(i)) > .75 and not nlp(text).similarity(nlp(i)) >= .999:
#             final.append(i)
#     return final

def textgen(text):
    txt = nlp(text)
    nouns = [token.text for token in txt if token.pos_ == 'NOUN']
    verbs = [token.text for token in txt if token.pos_ == 'VERB']
    adverbs = [token.text for token in txt if token.pos_ == 'ADV']
    adjectives = [token.text for token in txt if token.pos_ == 'ADJ']
    synonyms_noun_list = []
    for i in nouns:
        dict_noun_synonyms = {}
        dict_noun_synonyms['noun'] = i
        dict_noun_synonyms['synonyms'] = list(set([l.replace('_', ' ') for syn in Word(i).get_synsets(pos=NOUN) for l in syn.lemma_names()]))
        if len(dict_noun_synonyms['synonyms']) > 0:
            synonyms_noun_list.append(dict_noun_synonyms)
    
    valid_noun_list = []
    for j in synonyms_noun_list:
        for k in j['synonyms']:
            valid_noun_dict = {}
            valid_noun_dict['noun'] = j['noun']
            valid_noun_dict['syn'] = k
            if nlp(j['noun']).similarity(nlp(k)) > .45 and not nlp(j['noun']).similarity(nlp(k)) >= .999:
                valid_noun_list.append(valid_noun_dict)
    
    text_noun_generated = []
    for l in valid_noun_list:
        text_noun_generated.append(text.replace(l['noun'], l['syn']))
    synonyms_verb_list = []
    for i in verbs:
        dict_verb_synonyms = {}
        dict_verb_synonyms['verb'] = i
        dict_verb_synonyms['synonyms'] = list(set([l.replace('_', ' ') for syn in Word(i).get_synsets(pos=VERB) for l in syn.lemma_names()]))
        if len(dict_verb_synonyms['synonyms']) > 0:
            synonyms_verb_list.append(dict_verb_synonyms)
    
    valid_verb_list = []
    for j in synonyms_verb_list:
        for k in j['synonyms']:
            valid_verb_dict = {}
            valid_verb_dict['verb'] = j['verb']
            valid_verb_dict['syn'] = k
            if nlp(j['verb']).similarity(nlp(k)) > .45 and not nlp(j['verb']).similarity(nlp(k)) >= .999:
                valid_verb_list.append(valid_verb_dict)
    
    text_verb_generated = []
    for l in valid_verb_list:
        text_verb_generated.append(text.replace(l['verb'], l['syn']))
        
    synonyms_adverb_list = []
    for i in adverbs:
        dict_adverb_synonyms = {}
        dict_adverb_synonyms['adverb'] = i
        dict_adverb_synonyms['synonyms'] = list(set([l.replace('_', ' ') for syn in Word(i).get_synsets(pos=ADV) for l in syn.lemma_names()]))
        if len(dict_adverb_synonyms['synonyms']) > 0:
            synonyms_adverb_list.append(dict_adverb_synonyms)
    
    valid_adverb_list = []
    for j in synonyms_adverb_list:
        for k in j['synonyms']:
            valid_adverb_dict = {}
            valid_adverb_dict['adverb'] = j['adverb']
            valid_adverb_dict['syn'] = k
            if nlp(j['adverb']).similarity(nlp(k)) > .45 and not nlp(j['adverb']).similarity(nlp(k)) >= .999:
                valid_adverb_list.append(valid_adverb_dict)
    
    text_adverb_generated = []
    for l in valid_adverb_list:
        text_adverb_generated.append(text.replace(l['adverb'], l['syn']))
        
    synonyms_adjective_list = []
    for i in adjectives:
        dict_adjective_synonyms = {}
        dict_adjective_synonyms['adjective'] = i
        dict_adjective_synonyms['synonyms'] = list(set([l.replace('_', ' ') for syn in Word(i).get_synsets(pos=ADJ) for l in syn.lemma_names()]))
        if len(dict_adjective_synonyms['synonyms']) > 0:
            synonyms_adjective_list.append(dict_adjective_synonyms)
    
    valid_adjective_list = []
    for j in synonyms_adjective_list:
        for k in j['synonyms']:
            valid_adjective_dict = {}
            valid_adjective_dict['adjective'] = j['adjective']
            valid_adjective_dict['syn'] = k
            if nlp(j['adjective']).similarity(nlp(k)) > .45 and not nlp(j['adjective']).similarity(nlp(k)) >= .999:
                valid_adjective_list.append(valid_adjective_dict)
    
    text_adjective_generated = []
    for l in valid_adjective_list:
        text_adjective_generated.append(text.replace(l['adjective'], l['syn']))
    
    text_generated = text_noun_generated + text_verb_generated + text_adverb_generated + text_adjective_generated
    paraphrases = []
    for i in text_generated:
        if nlp(text).similarity(nlp(i)) > .90 and not nlp(text).similarity(nlp(i)) >= .999:
            paraphrases.append(i)
    return paraphrases
    
# def result(text):
#     paraphrases1 = textgen(text)
#     paraphrases2 = paraphrases(text)
#     paraphrase = paraphrases1 + paraphrases2
#     paraphrase = list(set(paraphrase))
#     return paraphrase
