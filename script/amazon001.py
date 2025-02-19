# -*- coding: utf-8 -*-
# Get movie with this kind of name:
# ^xxxx: xxxxx xxx xxxx (1984)$

import re

names = []
years = []

op = open('amazon001', 'w') 

with open('data/amazon000', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\t', line);
        if len(parts) != 4:
            print 'err:', line
            exit(-1)
        pid = (int)(parts[0])
        aid = parts[1].strip()
        name = parts[2].strip()
        name = re.sub('\[VHS\]', '', name)
        name = re.sub('\([\s\S]+\)', '', name)
        name = re.sub('\[[\s\S]+\]', '', name)
        name = re.sub('&amp;', '&', name)
        name = re.sub('[ ]+', ' ', name)
        name = name.strip().lower()
        cate = parts[3].strip()
            
        if re.search("^[0-9a-zA-Z :,&\'?!+\-./_=$%]+$", name):
            op.write("{}\t{}\t{}\t{}\n".format(pid, aid, name, cate));
        else:
            print name
