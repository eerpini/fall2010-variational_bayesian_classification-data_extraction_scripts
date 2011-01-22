#this program simulates random assignment of class labels to the data
#and checks for errors, for example for 20 classess the expected error
#should be around 95%, since the classification is random, no training 
# is required, we can run the simulation directly on certain slices of test
# data.
# arg1 : label_count.txt arg2 : vector.txt arg3 : bin_size
# version 2: reads in the randomized vector directly from vector.txt
import sys 
import string
import random

if len(sys.argv) != 4 :
	print "<program> label_count.txt vector.txt bin_size"
	sys.exit(1)

bin_size = string.atoi(sys.argv[3])
if bin_size > 20:
	print "Error : the bin size cannot be greater than 20"
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
#another way of doing this is to directly read into label_selection_vector from the first column
#in vector.txt, this would also avoid the need to convert the predicted index etc, the 
#output of random.randint can be directly used as the label predicted since the labels are already 
#converted in vector.txt. But in this case label_selection_vector does not vary every time the classification
#is done
print num_labels
print num_selection_labels
print labels
total_count = 0.00
error_count = 0.00
#build label_selection_vector from vector.txt
for line in vector_file:
	temp_list = []
	temp_list = line.split()
	print temp_list[0]
	label_selection_vector.append(string.atoi(temp_list[0]))
if len(label_selection_vector) != num_selection_labels:
	print "Error reading the label vector from vector.txt"
	sys.exit(1)
print label_selection_vector
vector_file.seek(0)
#build the bin, if the predicted lable is in any of the labels in the bin
#then the prediction is true.
for line in vector_file:
	label_bin=[i+1 for i in range(0,bin_size)]
	total_count = total_count+1
	print str(total_count) + "  ",
	temp_list = []
	temp_list  = line.split()
	#get the integer representing the label from the vector
	# we can map it back to the real label if at all we need to 
	print temp_list[0],
	label_integer = string.atoi(temp_list[0])
	label_bin.append(label_integer)
	print "<<<\nLABEL BIN\n"+str(label_bin)+"\n>>>"
	if label_integer <= num_labels and label_integer > 0 :
		random_index = random.randint(1,num_selection_labels)-1
		predicted_label = label_selection_vector[random_index]
		print " <<Index : "+str(random_index) +"Label : "+str(predicted_label)+">>"
		if predicted_label not in label_bin:
	#		print label_bin.index(predicted_label)
			error_count = error_count+1
	else:
		print "Invalid label "+str(temp_list[0])+"found in the vector, quitting"
		sys.exit(1)
if error_count > total_count :
	print "Error occurred in the program, check again"
	sys.exit(1)
else:
	print "Error is "+str(error_count/total_count)

