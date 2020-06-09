# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:33:53 2020

@author: jenna
"""

#Given an input DNA sequence, calculate several standard metrics:
#AT content, GC content, complement
import sys

#User inputs
file=sys.argv[1]

#Read in the sequence to be used
fileObject=open(file)
seq=fileObject.read()

#1) Calculate the AT content of a sequence

#number of A and T occurences
AContent=seq.count("A")
TContent=seq.count("T")

#Calculate and print AT content
ATPercentContent=(AContent+TContent)/len(seq)*100
print("AT content:", str(ATPercentContent), "%")

#2) Calculate the GC content of a sequence

#number of G and C occurences
GContent=seq.count("G")
CContent=seq.count("C")

#Calculate and print AT content
GCPercentContent=(GContent+CContent)/len(seq)*100
print("GC content:", str(GCPercentContent), "%")

#3) Get the complement of a sequence

#Replace A with T, G with C, etc
seqASub=seq.replace("A", "t")
seqTSub=seqASub.replace("T", "a")
seqGSub=seqTSub.replace("G", "c")
seqCSub=seqGSub.replace("C", "g")

#Convert back to upper, print
complement=seqCSub.upper()
print("Complement:", complement)
