# coding:utf-8
"""
python surveyer.py [***.html] [key words like (A_B)]

"""
import sys
import os
import re

def is_wanted_paper(line, key_words):
    cnt = 0
    for key_word in key_words:
        if key_word in line:
            cnt += 1
    return cnt == len(key_words)

def yes_no(y_n):
    if y_n == 'y':
        return True
    elif y_n == 'n':
        return False
    else:
        print('invalid! try again[y/n]')
        yes_no(input())

if __name__=='__main__':
    re_paper_id = re.compile("[A-Z][0-9]{1,2}-[0-9]{4}")
    html_file = open(sys.argv[1])
    key_words = sys.argv[2].split('_')
    for line in html_file:
        if is_wanted_paper(line.lower(), key_words):
            page = re_paper_id.search(line).group(0)
            title = line[line.find('</b><br><i>')+11:line.find('</i>')]
            #author = line[line.find('</b><br><i>')+11:line.find('</i>')]
            conference_year = sys.argv[1][:-5].split('../htmls/')[1]
            #year = "20%s" %page[1:3]
            print('\ntitle:',title, conference_year, page)
            print('\nDo you add this paper?[y/n]')
            if yes_no(input()):
                os.system("wget -O ../bibs/%s_%s.bib https://aclweb.org/anthology/%s/%s/%s.bib"\
                   %('_'.join(title.split()),conference_year, page[:1], page[:3], page))

