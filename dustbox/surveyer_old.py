# coding:utf-8
"""
python surveyer.py [***.html] [key words like (A_B)]

"""
import sys
import os

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        if is_page(data):
            results.append(data)
        if is_wanted_paper(data, key_words):
            results.append(data)

def is_wanted_paper(line, key_words):
    flag = False
    for key_word in key_words:
        if key_word in line:
            flag = True
    return flag

def is_page(data):
    return '-' in data

def parse():
    parser = MyHTMLParser()
    parser.feed(''.join(html_file))
    #for line in open(sys.argv[1]):
    #    key_words = sys.argv[2].split('_')
    #    if is_wanted_paper(line, key_words):
    #        print(line.strip())

if __name__=='__main__':
    html_file = open(sys.argv[1])
    key_words = sys.argv[2].split('_')
    results = list()
    parse()
    for result in results:
        if is_page(result):
            page = result
        if is_wanted_paper(result, key_words):
            print('****')
            print(result, page)
