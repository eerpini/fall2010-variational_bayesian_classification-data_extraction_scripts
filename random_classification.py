#this program simulates random assignment of class labels to the data
#and checks for errors, for example for 20 classess the expected error
#should be around 95%, since the classification is random, no training 
# is required, we can run the simulation directly on certain slices of test
# data.
# arg1 : label_count.txt arg2 : vector.txt

import sys 
import string
import random

if len(sys.argv) != 3 :
	print "<program> label_count.txt vector.txt"
	sys.exit(1)

label_file = file(sys.argv[1])
vector_file = file(sys.argv[2])
labels = []
counts = []
for line in label_file:
	label, count = line.split()
	labels.append(label)
	counts.append(string.atoi(count))
num_labels = len(labels)
total_count = 0.00
error_count = 0.00
for line in vector_file:
	total_count = total_count+1
	print str(total_count) + "  ",
	temp_list = []
	temp_list  = line.split()
	#get the integer representing the label from the vector
	# we can map it back to the real label if at all we need to 
	print temp_list[0],
	label_integer = string.atoi(temp_list[0])
	if label_integer <= num_labels and label_integer > 0 :
		#since the prediction is from the length of the numbers, there is no need to convert
		#the prediction into a integer (as in a converted label), but in the case of truly random
		#classification this is required. cf. truly_random_classification.py
		prediction = random.randint(1,num_labels)
		print "  "+str(prediction)
		if prediction != label_integer:
			error_count = error_count+1
	else:
		print "Invalid label "+str(temp_list[0])+"found in the vector, quitting"
		sys.exit(1)
if error_count > total_count :
	print "Error occurred in the program, check again"
	sys.exit(1)
else:
	print "Error is "+str(error_count/total_count)

