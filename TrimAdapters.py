# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:43:21 2020

@author: jenna
"""

#For a file that contains several sequences (one per line):
    #-trim the adapter (14 bp) from the start
    #-print out the new length
    #-write a new file that contains all the adapter trimmed sequences

#import modules
import sys

#User inputs
file=sys.argv[1]
adapterLength=int(sys.argv[2])

#Open the file to be used
seq=open(file)

#initialize list for trimmed sequences
trimmedWrite=open("trimmed.txt", "w")

#Remove adapters, append to trimmedFiles. Prints out length of trimmed sequence.
for line in seq:
    trimmed=line[adapterLength:]
    print("Length of trimmed sequence: " + str(len(trimmed)))
    trimmedWrite.write(trimmed)    
    
trimmedWrite.close()
