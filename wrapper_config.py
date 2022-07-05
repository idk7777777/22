#coding: utf-8

# proxy types: http|https|socks4|socks5


DEBUG = True # False - without logs
#DEBUG = False # False - without logs

URLS_FILE = 'site.txt'
SQLi_SAVE_FILE = 'goodsqli.txt'
BRUTE_SAVE_FILE = 'goodbrute.txt'

LOG_FILE = 'wrapper_session.log'

DUMP = True
STRUCT = False
DUMP_ALL = False
Check_SQLi = False

start = 1
stop = 1000000000

Robots = True
ROBOTS_SAVE = 'goodrobots.txt'

Check_List = True

# Брут CMS - не используется
BRUTE_CMS = False
THREADS_BRUTE = 100
# Пробив эксплоитами
EXPLOITS_CMS = True

ADMIN_FIND = False
FILES_FIND = False
FILES_SAVE = 'filesave.txt'
FILES_PAGE = 'files.txt'

ADMIN_PAGE = 'adminpage.txt'
ADMIN_SAVE = 'adminsave.txt'
PASSW_FILE = 'passw.txt'

ADMIN_FOLDER = 'admdump'

ADMIN_HACK_SAVE = 'adminhacksave.txt'

COLUMN_DUMP = 'user,clave,correo,hash,heslo,jelszo,mail,parola,pass,posta,psw,pw,senha,salt,md5,sha1,mobile,phone,number'

SPIDER = True
SPIDER_LINKS = '10'

SQLMAP_DUMPS = 'dumps'
WRAPPER_TXT_DUMPS = 'txt_dumps'
DUMP_FORMAT='CSV'

time_sec = 30
TIMEOUT = 180 # sec

ALEXA_CHECK = False
ALEXA = 1000000

TAMPER = 'safedog,randomcase' # safedog,doubleurlencode,doublekeywords   space2comment,space2plus,randomcase,unmagicquotes

PROXY = False # False if work without it
# PROXY = True
PROXY_TYPE = 'socks5'
PROXY_URL = '' # first#
PROXY_FILE = 'proxy.txt' # second if not first
PROXY_USERNAME = ''
PROXY_PASSWORD = ''
URLS_LIMIT = 10000000
DUMP_FOLDER = 'dumps_folder'
DUMP_COLUMN_LIMIT = 20 # 91 - 100 ...
THREADS = 300

DELETE = False

RISK = 3
LEVEL = 5
RETRIES = '5'
