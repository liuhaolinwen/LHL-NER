#coding:utf-8
import codecs
import re
import pandas as pd
import numpy as np
import pdb
tag2label = {
'ns' :'LOC',
'nr' :'NAME',
'nt' :'ORG'}
def wordtag():
    count=0
    input_data = codecs.open('train1.txt','r','utf-8')
    output_data = codecs.open('wordtag.txt','w','utf-8')
    for line in input_data.readlines():
        #line=re.split('[，。；！：？、‘’“”]/[o]'.decode('utf-8'),line.strip())
        line = line.strip().split()
        if len(line)==0:
            continue
        for word in line:
            word = word.split('/')
            if word[1]!='o':
                if len(word[0])==1:
                    #pdb.set_trace()
                    #print word[1]
                    replace1 = tag2label[word[1].decode('utf-8')]
                    output_data.write(word[0]+" B-"+replace1+"\n")
                elif len(word[0])==2:
                    replace2 = tag2label[word[1].decode('utf-8')]
                    output_data.write(word[0][0]+" B-"+replace2+"\n")
                    output_data.write(word[0][1]+" E-"+replace2+"\n")
                    count+=1
                else:
                    replace3 = tag2label[word[1].decode('utf-8')]
                    output_data.write(word[0][0]+" B-"+replace3+"\n")
                    for j in word[0][1:len(word[0])-1]:
                        output_data.write(j+" M-"+replace3+"\n")
                    output_data.write(word[0][-1]+" E-"+replace3+"\n")
                    count+=1
            else:
                if word[0]=='“':
                    continue
                elif word[0]=='\xb8':
                    continue
                elif word[0]=='\xe2':
                    continue
                else:
                    for j in word[0]:
                        output_data.write(j+" O"+"\n")
        output_data.write('\n')
    input_data.close()
    output_data.close()
    print count
    print "finish taging the data"
wordtag()


