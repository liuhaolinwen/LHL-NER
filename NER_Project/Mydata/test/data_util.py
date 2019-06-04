#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import pandas as pd
import numpy as np
import re
    
tag2label = {
'location' :'LOC',
'person_name' :'NAME',
'org_name' :'ORG',
'company_name' :'ORG'}
def origin2tag():
    input_data = codecs.open('./origindata.txt','r','utf-8')
    output_data = codecs.open('./wordtag.txt','w','utf-8')
    count=0
    for line in input_data.readlines():
        line=line.strip()
        i=0  
        while i <len(line):
	        if line[i] == '{':
		        i+=2
		        #print line[0]
		        temp=""
		        while line[i]!='}':
			        temp+=line[i]
			       # print line[i]
			        i+=1
		        i+=2
		        word=temp.split(':')
		        #print word
		        sen = word[1]
		        tag = word[0]
		        #print word[0]
		        #print str(word[1])
		        if tag =='product_name':
		            for j in sen[0:len(sen)]:
		                output_data.write(j+' O'+"\n")
		        elif tag =='time':
		            for j in sen[0:len(sen)]:
		                output_data.write(j+' O'+"\n")
		        else:
		            label = tag2label[word[0]]
		            sen=sen.strip()
		            output_data.write(sen[0]+" B-"+label+"\n")
		            for j in sen[1:len(sen)-1]:
		                output_data.write(j+" M-"+label+"\n")
		            output_data.write(sen[-1]+" E-"+label+"\n")
		            count+=1
	        else:
		        output_data.write(line[i]+" O"+"\n")
		        i+=1
        output_data.write('\n')
    input_data.close()
    print count 
    output_data.close()


origin2tag()
print "finished tag"

