#!/usr/bin/python 


import sys

if len(sys.argv)<2:
	print "Usage list_elements <file containing group information(groups.txt)>\n"
	sys.exit(1)

groups_file = file(sys.argv[1])
elements_file = file("elements.txt", "w")

# we will initialize the list with O since we know that has to
# be present

elements=["O"]
for line in groups_file :
	if line.split(" ")[0] == "group":
		continue
	e1,e2,e3= line.split(" ")
	#e2 = e2.split(" ")[0]
	# we will iterate over only the first two elements since we
	# know that the third one is always O
	for element in (e1,e2):
		if elements.count(element)<1:
			elements.append(element)
groups_file.close()
elements.sort()
for element in elements :
	elements_file.write(element+"\n")
elements_file.close()



