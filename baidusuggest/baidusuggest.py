# -*- coding: utf-8 -*-
"""
Baidu suggestion
~~~~~~~~~~

Defines the interaction with the Baidu suggestion services.
Since the script interfaces with the Baidu web service, this
module deals with making the suggestion request
on the client side to the the server.
"""

from __future__ import print_function, unicode_literals

import json
import re

from functools import wraps

try:
    #from urllib.request import urlopen, Request
    #from urllib.parse import urlencode
    import requests
except ImportError:
    #from urllib2 import urlopen, Request
    #from urllib import urlencode
    import requests

__all__ = [
    'query_url',
    'results_type'  #json by default
]


def get(query_word):
    query_par= {'wd': query_word, 'json': 1}

    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'
    acceptlang='zh-CN,zh;q=0.8'
    headers = {'User-Agent': agent, 'Accept-Language':acceptlang}
    url_base = 'http://suggestion.baidu.com/su'

    r = requests.get(url_base, params=query_par,headers=headers)

    if r.status_code==200:
        regex_Baidu_autocomp = re.compile("({.*})") # re.match(ur"\((.*)\)", r.text, flags=re.UNICODE)
        r = regex_Baidu_autocomp.search(r.text)
        # if r.groups():
            # print r.groups(0)
        json_extracted=r.groups(1)[0]
        json_data= json.loads(json_extracted)         #simplejson.loads(json_extracted.encode('utf8'), "utf-8")

        Baidu_autocomp_query=json_data['q']
        Baidu_autocomp_results=json_data['s']
    else:
        Baidu_autocomp_query=u"failed:"+query_word
        Baidu_autocomp_results=[]
    return Baidu_autocomp_query, Baidu_autocomp_results

