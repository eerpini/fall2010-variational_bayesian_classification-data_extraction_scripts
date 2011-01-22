#!/usr/bin/python
import sys

# we are not using this file for the extraction of the data anymore,
# instead we are now using the get_not_null.py file for getting the data

if len(sys.argv)<2:
	print "Specify the input file\n"
	sys.exit(0)

#file declarations for the input and output
inf = file(sys.argv[1])
outf = file("output.txt","w")
coutf = file("coutput.txt","w")
j=0.0
#reading in the lines
for line in inf:
	weight_index = line.find("weight")
	weight = line[weight_index+7:].rstrip("\n")
	line = line[:weight_index].rstrip()
	line=line[1:-1]
	#print weight 
	compositions,labels=line.split("=")
	compositions=compositions[1:-2].split(",")
	labels=labels[2:-1].split(",")
	elements=labels[-3:]
	compositions=compositions[:-3]
	labels = labels[:-3]
	#print compositions
	#print labels
	#print elements
	i=0
	while i<len(labels):
		outf.write(compositions[i].lstrip()+"("+elements[0].lstrip()+","+elements[1].lstrip()+","+elements[2].lstrip()+")("+labels[i].lstrip()+")("+weight+")\n");
		if(labels[i].lstrip() != "null"):
			coutf.write(compositions[i].lstrip()+"("+elements[0].lstrip()+","+elements[1].lstrip()+","+elements[2].lstrip()+")("+labels[i].lstrip()+")("+weight+")\n");
		i=i+1
	j=j+1
	print "progress "+str(j*100/878774)+" %\r",
			



