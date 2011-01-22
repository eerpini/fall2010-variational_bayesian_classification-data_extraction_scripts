#!/usr/bin/python
# this script is being used to remove the permutations in the elements
# composing a compound. Expects the output of get_not_null.py as input
# Input : coutput.txt Output : with_permutations_resolved.txt
# The script also writes out the list of the labels to loutf (look for file name below)
# 
# NOTE : The output file needs to run through "sort -u" to remove the duplicates, 
# the script only converts all the permutations into the same order, does not remove
# the duplicates.

# but the output right now is only to make it more readable, I am modifying 
# the format which is being written by remove_permutations.py into a space 
# delimited format so that it is easier for generate_vector.py to process it
#
# I am suspecting the functionality of the code which writes the labels down into 
# another file, the line count for the file labels_with_permutations_resolved.txt 
# is the same as coutput.txt
import sys

if len(sys.argv)<2:
	print "Specify the file to process as an argumentn\n"
	sys.exit(0)

inf = file(sys.argv[1])
outf = file("without_permutations.txt","w")
loutf = file("labels_without_permutations.txt","w")
j=0.000
for line in inf:
	compositions,elements,label,weight=line.split(":")
	compositions=compositions[1:-1].split(";")
	#print elements[1:-1]
	elements=elements[1:-1].split(",")
	elements_sorted=sorted(elements[:-1])
	switch=0
	if(elements_sorted != elements[:-1]):
		#print elements_sorted, elements[:-1]
		switch=1
	if(switch==1):
		temp=compositions[0]
		compositions[0]=compositions[1]
		compositions[1]=temp
		temp=elements[0]
		elements[0]=elements[1]
		elements[1]=temp
		#commenting out the old way of writing the compositions
		#outf.write("("+compositions[0]+";"+compositions[1]+";"
		#	+compositions[2]+"):("+elements[0]+","
		#	+elements[1]+","+elements[2]+"):"
		#	+label+":"+weight.rstrip("\n")+"\n")
		outf.write(compositions[0]+" "+compositions[1]+" "
			+compositions[2]+" "+elements[0]+" "
			+elements[1]+" "+elements[2]+" "
			+label+" "+weight.rstrip("\n")+"\n")
		loutf.write(label+"\n")
		continue
	#outf.write(line)
	loutf.write(label+"\n")
	j=j+1
	print "progress "+str(j*100/12101310)+" %\r",


	
	

