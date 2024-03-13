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

# Command-line interface setup
cl = clfilter("mn", doc=__doc__)

def tokeniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:!?—]+', texto)
    return palavras

def imprime(lista, numeric=False):
    if numeric:
        # Sort by number of occurrences (descending) then alphabetically
        lista.sort(key=lambda x: (-x[1], x[0]))
    else:
        # Sort alphabetically
        lista.sort()
    for palavra, n_ocorr in lista:
        print(f"{palavra}   {n_ocorr}")

for txt in cl.text():  # Process one file at a time
    lista_palavras = tokeniza(txt)
    ocorr = Counter(lista_palavras)
    lista_items = list(ocorr.items())

    if "-n" in cl.opt:
        # Order by number of appearances if -n option is present
        imprime(lista_items, numeric=True)
    else:
        # Default to alphabetical order
        imprime(lista_items)
