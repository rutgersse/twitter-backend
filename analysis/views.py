from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.dispatch import receiver
from django.db import models
from django.db.models import F, Q
from django.core.files.storage import default_storage as storage

from fetchdata.models import Tweet

from fetchdata.forms import keyword

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams 


import re

import operator 
import json
from collections import Counter

import string
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]


tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

def tokenize_ind( tweet ):
    return word_tokenize(tweet)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def remove_stop( tweet ):
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

    # Count terms only once, equivalent to Document Frequency
    terms_single = set(terms_all)
    # Count hashtags only
    terms_hash = [term for term in preprocess(tweet['text']) 
                  if term.startswith('#')]
    # Count terms only (no hashtags, no mentions)
    terms_only = [term for term in preprocess(tweet['text']) 
                    if term not in stop and
                    not term.startswith(('#', '@'))] 


    terms_bigram = bigrams(terms_stop)

def analyze_bigrams( twweet ):
    for line in f: 
    terms_only = [term for term in preprocess(tweet['text']) 
                  if term not in stop 
                  and not term.startswith(('#', '@'))]
 
    # Build co-occurrence matrix
    for i in range(len(terms_only)-1):            
        for j in range(i+1, len(terms_only)):
            w1, w2 = sorted([terms_only[i], terms_only[j]])                
            if w1 != w2:
                com[w1][w2] += 1

    com_max = []
    # For each term, look for the most common co-occurrent terms
    for t1 in com:
        t1_max_terms = max(com[t1].items(), key=operator.itemgetter(1))[:5]
        for t2 in t1_max_terms:
            com_max.append(((t1, t2), com[t1][t2]))
    # Get the most frequent co-occurrences
    terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
    return (terms_max[:5])

def semantic_analysis():
    # Computing probability
    p_t = {}
    p_t_com = defaultdict(lambda : defaultdict(int))
     
    for term, n in count_stop_single.items():
        p_t[term] = n / n_docs
        for t2 in com[term]:
            p_t_com[term][t2] = com[term][t2] / n_docs

    
def analysis_main( data ):
    for tweet in data:
        s = preprocess( tweet )

