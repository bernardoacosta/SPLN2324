#!/usr/bin/env python3

'''
NAME
   word_freq - calculates the frequency of words in a text

SYNOPSIS
   word_freq [options] input_file
   options:
        -m: ordered alphabetically (default behavior)
        -n: ordered by number of appearances

DESCRIPTION
   This script calculates and displays the frequency of words in a given text file.
   It supports ordering the output either alphabetically or by number of appearances.
'''

from jjcli import *
from collections import Counter
import re

def tokeniza(texto):
    palavras = re.findall(r'\w+(?:-\w+)?|[,;.:!?—]+', texto)
    return palavras

def imprime(lista, numeric=False):
    if numeric:
        lista.sort(key=lambda x: (-x[1], x[0]))
    else:
        lista.sort()
    for palavra, n_ocorr in lista:
        print(f"{palavra}   {n_ocorr}")

def consolidate_counts(words):
    
    case_insensitive_count = Counter(word.lower() for word in words)
    preferred_forms = {}

    for word, _ in case_insensitive_count.items():
        capitalized_form = word.capitalize()
        lowercase_form = word.lower()
        cap_count = words.get(capitalized_form, 0)
        low_count = words.get(lowercase_form, 0)
        if cap_count >= low_count:
            preferred_forms[word] = capitalized_form
        else:
            preferred_forms[word] = lowercase_form

    consolidated_counts = {}
    for word, count in words.items():
        preferred_form = preferred_forms[word.lower()]
        consolidated_counts[preferred_form] = consolidated_counts.get(preferred_form, 0) + count

    return consolidated_counts

def main():
    cl = clfilter("mn", doc=__doc__)

    for txt in cl.text():
        lista_palavras = tokeniza(txt)
        ocorr = Counter(lista_palavras)
        consolidated_ocorr = consolidate_counts(ocorr)
        lista_items = list(consolidated_ocorr.items())
        if "-n" in cl.opt:
            imprime(lista_items, numeric=True)
        else:
            imprime(lista_items)

if __name__ == "__main__":
    main()


