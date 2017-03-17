#!/usr/bin/env python
#
#  Easy way to extract data from XML MEDLINE files
#  Download Annual Baseline of MEDLINE @ https://www.nlm.nih.gov/databases/download/pubmed_medline.html
#  
#  parseMediline.py script which runs in parallel way using the maximum number of cpu cores
#  
#  Copyright 2017 Vasiliki Kordopati <vasokordopati@gmail.com>
#  

import re
import sys
import os
import os, os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from subprocess import call
from joblib import Parallel, delayed
import multiprocessing
import xml.etree.ElementTree as ET

AbstractTexts=[] #when there are mone than 1 <AbstractText> instances
inputs = range(892) # based on the number of medline XML files


def parseMEDLINE(i):
	
	i+=1
	print i
	if (i < 10):
		print '000'+str(i)
		filename = 'medline17n000'+str(i)
		print filename

	if (10 <= i < 100):
		print '00'+str(i)
		filename = 'medline17n00'+str(i)
		print filename

	if (i == 100) or (i > 100):
		print '0'+str(i)
		filename = 'medline17n0'+str(i)
		print filename
	
	tree = ET.parse(filename +'.xml')
	root = tree.getroot()

	#for each MEDLINE file you store the coresponding data new file with same filename
	with open(filename +'.txt', 'w') as f:
		f.write(' ArticleID \t Title \t Abstract \n')
		print filename + ' created'

	for pubmed_article in root.findall('PubmedArticle'):
		ArticleID = pubmed_article.find('MedlineCitation').find('PMID').text #print ArticleID
		if ArticleID is not None:
			Article = pubmed_article.find('MedlineCitation').find('Article')
		else:
			Article = ""
		Title = Article.find('ArticleTitle').text
		if Title is not None: 
			Title = Article.find('ArticleTitle').text
			#print 'Title found'
		else:
			Title = ""
		Abstract = Article.find('Abstract')
		if Abstract is not None:
			for AbstractText in Abstract.iter('AbstractText'):
				AbstractTexts.append(AbstractText.text)
				#print AbstractText

		else:
			AbstractText = ""
		try:
			line_to_write = ArticleID + '\t' + Title + '\t' + ' '.join(AbstractTexts) +'\n'
			print ArticleID + ' -> DONE'
			with open(filename +'.txt', 'a') as f:
				f.write(line_to_write)
				del AbstractTexts[:]
				f.close()
		except TypeError:
			line_to_write = ArticleID+'\n'
			print ArticleID + ' -> DONE'
			with open(filename +'.txt', 'a') as f:
				f.write(line_to_write)
				del AbstractTexts[:]
				f.close()
			continue

number_of_cores = multiprocessing.cpu_count()
output = Parallel(number_of_jobs=number_of_cores)(delayed(parseMEDLINE)(i) for i in inputs)
