# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:16:11 2020

@author: jenna
"""

#Given sequences (1 per line) and table of codons, translate DNA sequence into protein
#calculate percentage of sequence that is composed of given amino acid(s)

#import modules
import sys

#User inputs
file=sys.argv[1]
codons=sys.argv[2]
residues=sys.argv[3]


#read in aa codes, add to dictionary
aaInput=open("codons.csv")
codons={}
for aa in aaInput:
    split=aa.split(",")
    residue=split[1].rstrip("\n")
    codons[str(split[0])]=str(residue)
    
#Read in residues
residues=open(residues).read().rstrip("\n").split("\n")

#Function for translating DNA to amino acids
    #Starts at FIRST methione, continues in frame until the first stop codon
def translate_dna(seq, codonDict):
    seq=seq.upper()
    aaSeq=""
    
    #Get occurrence of first M, start appending aas there
    Start=0
    for nt in range(0,len(seq)-2):
        codon=seq[nt:nt+3]
        aa=codonDict.get(codon, "X")
        if aa=="M":
            Start=nt
            break
    
    #Loop through all triplets, starting at the site of the first methione ("Start")
    for triplet in range(Start,len(seq)-2,3):
        codon=seq[triplet:triplet+3]
        aa=codonDict.get(codon, "X")
        aaSeq=aaSeq+aa
        
        #Stop once you get to a "*"
        if codonDict.get(codon, "X")=="*":
            return(aaSeq)
            break
    return(aaSeq)

#function that takes as input a protein string + list of residues 
#outputs the % of the protein that those residues make up (defaults given)
def getAAPercentage_list(aaSeq, residues=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    totaln=0
    for residue in residues:
        n=aaSeq.count(residue.upper())
        totaln=totaln+n
    percentn=totaln/len(aaSeq) *100
    return(round(int(percentn), 0))

#Translate all, print out percentage
AllTranslated=[]
for line in open(file):
    aa=translate_dna(line, codons)
    AllTranslated.append(aa)
    print(getAAPercentage_list(aa, residues), "% of sequence composed of given resiudes")

#Export each amino acid sequence out to file, one line per fragment
with open('TranslatedSequence.txt', 'w') as f:
    for aa in AllTranslated:
        f.write("%s\n" % aa)
    
