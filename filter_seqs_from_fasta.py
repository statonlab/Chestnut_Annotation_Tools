#!/data/apps/python/3.2.1/bin/python
import re, sys, getopt
from Bio import SeqIO

list_file = str(sys.argv[1])
print("List file is ", list_file)

fasta_file = str(sys.argv[2])
print("Fasta file is ", fasta_file)

new_fasta_file = fasta_file+'.filtered'

# initiate a dictionary to hold the swiss prot entries as keys and 
# their descriptions as the value
idlist = []

##-----------------------
## Get id list
with open(list_file) as f:
	for line in f:
		line = line.strip()
		idlist.append(line)
		#print(line)
f.close

##-----------------------
## Turn list into a set for lookup
idset = set(idlist)

###-----------------------
## Iterate fasta fle

inhandle = open(fasta_file)
outhandle = open(new_fasta_file, "w")
count = 0

for record in SeqIO.parse(inhandle, "fasta") :
	id = record.id
	id = re.sub('probe:Soybean:', '', id)
	id = re.sub(':\d+:\d+;$', '', id)
	#print id
	if id not in idset:
		count += SeqIO.write(record, outhandle, "fasta")

inhandle.close()
outhandle.close()

print("%d sequences output" % count)
