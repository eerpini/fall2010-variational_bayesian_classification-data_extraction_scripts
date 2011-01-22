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
temp_label_selection_vector = []
label_selection_vector = []
counts = []
for line in label_file:
	label, count = line.split()
	for i in range(string.atoi(count)):
		temp_label_selection_vector.append(label)
	labels.append(label)
	counts.append(string.atoi(count))
num_labels = len(labels)
num_selection_labels = len(temp_label_selection_vector)
#we need to randomize the repetitions of labels in the label_selection_vector further
#this is done in a very dumb way right now and may take a long time
#another way of doing this is to directly read into label_selection_vector from the first column
#in vector.txt, this would also avoid the need to convert the predicted index etc, the 
#output of random.randint can be directly used as the label predicted since the labels are already 
#converted in vector.txt
temp_len = len(temp_label_selection_vector)
while len(label_selection_vector) < num_selection_labels:
	temp = random.randint(1,temp_len)-1
	label_selection_vector.append(temp_label_selection_vector[temp])
	del temp_label_selection_vector[temp]
	temp_len = len(temp_label_selection_vector)
if len(label_selection_vector) != num_selection_labels:
	print "Error occurred while trying to randomize the vector\n randomized vector is not of the same length\n"
	sys.exit(1)
print num_labels
print num_selection_labels
print labels
print label_selection_vector
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
		random_index = random.randint(1,num_selection_labels)-1
		predicted_label = label_selection_vector[random_index]
		predicted_converted_label = labels.index(predicted_label)+1
		print " <<Index : "+str(random_index) +"Label : "+str(predicted_label)+" Converted Label : "+str(predicted_converted_label)+">>"
		if predicted_converted_label != label_integer:
			error_count = error_count+1
	else:
		print "Invalid label "+str(temp_list[0])+"found in the vector, quitting"
		sys.exit(1)
if error_count > total_count :
	print "Error occurred in the program, check again"
	sys.exit(1)
else:
	print "Error is "+str(error_count/total_count)

