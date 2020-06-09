# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:48:13 2020

@author: jenna
"""

#For a file that contains a single DNA sequence + file with exon coordinates separated by commas:
    #extract the exons
    #concatenate
    #write to file

#import modules
import sys

#User inputs
file=sys.argv[1]
exonCoords=sys.argv[2]

#read in the sequences
seq=open(file).read().rstrip("\n")

#open the exon coordinates
exonFile=open(exonCoords)

#initialize string for exons
exons=""

#for each exon position, get sequence at that position
for position in exonFile:
    start=int(position.split(",")[0])-1
    end=int(position.split(",")[1])
    exon=seq[start:end]
    exons=exons+exon

#write exons out
exonsOut=open("exonsSeq.txt", "w")
exonsOut.write(exons)
exonsOut.write("\n")
exonsOut.close()
