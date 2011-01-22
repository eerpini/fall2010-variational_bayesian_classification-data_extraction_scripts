#!/usr/bin/python

import sys
import string 

if len(sys.argv) != 3:
	print "Usage : get_label_count.py without_permutations_unique.txt <label count threshold>"
	sys.exit(1)

label_file = file("labels_unique_sorted.txt");
labels=[]
for line in label_file :
	labels.append(line[1:-2])
labels.sort()
label_dict = {}
for i in labels:
	label_dict[i]=0

data_file = file("without_permutations_unique.txt")
outf = file("labels_all.txt","w")
for line in data_file :
	c1, c2, c3, e1, e2, e3, label, weight = line.split(" ")
	label = label[1:-1]
	if(label != ''):
		label_dict[label]=label_dict[label]+1

#for key in label_dict.keys():
#	print key+" "+str(label_dict[key])

items = label_dict.items()
items = [(v,k) for (k,v) in items]
items.sort()
items.reverse()
items = [(k,v) for (v,k) in items]
#print items
for (k,v) in items:
	#prints labels with counts greater than 5
	if v>=string.atoi(sys.argv[2]):
		print k+" "+str(v)

