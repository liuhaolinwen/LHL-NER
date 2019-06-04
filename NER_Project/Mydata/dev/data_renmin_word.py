# -*- coding: UTF-8 -*-

import codecs
import re
import pdb
import pandas as pd
import numpy as np
import collections
tag2label = {
'ns' :'LOC',
'nr' :'NAME',
'nt' :'ORG'}
punc = "！？＂：；［］＿、〃〝〞–—‘’‛“”„‟﹏."
punc = punc.decode("utf-8")
def originHandle():
    with open('./renmin.txt','r') as inp,open('./renmintag.txt','w') as outp:
        for line in inp.readlines():
            line = line.split('  ')
            #从1开始前面的时间信息丢弃
            i = 1
            while i<len(line)-1:
                #带有中括号的数据处理
                if line[i][0]=='[':
                    outp.write(line[i].split('/')[0][1:])#将[后面的所有字符写入
                    #print line[i].split('/')[0][1:]
                    #pdb.set_trace()
                    i+=1
                    while i<len(line)-1 and line[i].find(']')==-1:
                        if line[i]!='':
                            outp.write(line[i].split('/')[0])
                        i+=1
                    outp.write(line[i].split('/')[0].strip()+'/'+line[i].split('/')[1][-2:]+' ')
                #if str(i) == '8':
                 #    pdb.set_trace()
                #if str(i) == '9':
                 #   pdb.set_trace()
                elif line[i][0]=='\xe4':
                    i+=1
                elif line[i][0]=='\xb8':
                    i+=1
                elif line[i][0]=='\xe2':
                    i+=1
                #带有符合条件的字符串nr处理
                elif line[i].split('/')[1]=='nr':
                    word = line[i].split('/')[0] 
                    i+=1
                    if i<len(line)-1 and line[i].split('/')[1]=='nr':
                        outp.write(word+line[i].split('/')[0]+'/nr ')           
                    else:
                        outp.write(word+'/nr ')
                        continue
                #其他情况直接写入
                else:
                    outp.write(line[i]+' ')
                i+=1
            #处理完一行换行
            outp.write('\n')
def originHandle2():
    with codecs.open('./renmintag.txt','r','utf-8') as inp,codecs.open('./renmindata.txt','w','utf-8') as outp:
        count=0                                                                                                                       
        for line in inp.readlines():
            line = line.split(' ')
            i = 0
            while i<len(line)-1:
                if line[i]=='':
                    i+=1
                    continue
                word = line[i].split('/')[0]
                #pdb.set_trace()
                #word = re.sub(ur"[%s]+" u'\u0020-\u007f\u2000-\u206f\u3000-\u303f\uff00-uffef', "", word)
                tag = line[i].split('/')[1]
                if tag=='nr' or tag=='ns' or tag=='nt':
                    outp.write(word[0]+" B-"+tag2label[tag]+"\n")
                    for j in word[1:len(word)-1]:
                        if j!=' ':
                            outp.write(j+" M-"+tag2label[tag]+"\n")
                    outp.write(word[-1]+" E-"+tag2label[tag]+"\n")
                    count+=1
                else:
                    for wor in word:
                        outp.write(wor+' O'+'\n')
                i+=1
    print count



originHandle()
originHandle2()
print "data tag finished"
