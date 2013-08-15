#!/usr/bin/env python 
import sys 
import re
from bs4 import BeautifulSoup as bs

documents='/home/dmalik5/docs/'
doc_names=[
        'gunicorn','ngnix','tastypie',
        'south','vim','git','uwsgi',
        'fabric','python','curl'
        ]

def help ():
    return "\n\tSynatx: chelp <document string> <doctype>\n"



def display(document,doctype):
    if document in doc_names:
        with open(documents+document+'.txt') as fh:
            soup=bs(fh)
            try:
                data=getattr(soup,doctype).string
                print data 
            except AttributeError:
                print "%s doctype is not defined for %s"  %(doctype,document)

    else:
        print doc_names




if __name__=="__main__":
    try:
        doc_index=sys.argv[1]
        try:
            doc_type=sys.argv[2] or None
        except IndexError:
            doc_type='help'
        display(doc_index,doc_type)
    except IndexError:
        print  help()
