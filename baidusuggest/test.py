# -*- coding: utf-8 -*-
import baidusuggest
import sys

def msg_list(lst):
    return repr([x.encode('utf8') for x in lst]).decode('string-escape')

query_input=u'共產黨'
suggestions_list=[]

query_output, suggestions_list=baidusuggest.get(query_input)
print "Input\tOutput"
print "%s\t%s" % (query_input, query_output)
print "Output suggestions"
print msg_list(suggestions_list)
