#!/data/apps/python/3.2.1/bin/python
import re, sys, getopt

file1 = str(sys.argv[1])
file2 = str(sys.argv[2])
print("Blast files are", file1, " ",file2)

out = "reciprocal_best_hits.txt"

# initiate a dictionary to hold the first file matches as keys and 
# queries as the value
m2q = {}

##-----------------------
## Get matches from first blast file
with open(file1) as f1:
	for line in f1:
		fields = line.split('\t')
		if fields[0] not in m2q:
			m2q[fields[0]] = fields[1]
			print("storing >", fields[0], "<,>", fields[1], "<")
f1.close

##-----------------------
## Parse second blast file and if the same matching pair is found, print out
o = open(out, "w")
with open(file2) as f2:
	for line in f2:
		fields = line.split('\t')
		if fields[1] in m2q:
			print("looking at >", fields[0], "<,>", fields[1], "<")
			if m2q[fields[1]] == fields[0]:
				o.write(fields[0]+"\t"+fields[1]+"\n")
				print("\trbh: ", fields[0], ",", fields[1])
				del m2q[fields[1]]
f1.close
