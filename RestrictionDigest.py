# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:00:40 2020

@author: jenna
"""

#Given a DNA sequence and a list of restriction sites, digest the sequence.
#Print out length of fragments, export a file with each fragment on 1 line

#import modules
import sys
import re

#User inputs
file=sys.argv[1]
rEnzymes=sys.argv[2]

#Read in sequence
seq=open(file).read().rstrip("\n")

#Read in restriction enzmye sequences
AllSites=open(rEnzymes).read().rstrip("\n").split("\n")

#Convert ambiguous nt in restriction sites to list of possible nts (i.e., "Y" -->[CT])
#Creat dictionary with all IUPAC codes
IUPAC={"R" : "[AG]",
       "Y" : "[CT]",
       "S" : "[GC]",
       "W" : "[AT]",
       "K" : "[GT]",
       "M" : "[AC]",
       "B" : "[CGT]",
       "D" : "[AGT]",
       "H" : "[ACT]",
       "V" : "[ACG]",
       "N" : "[ACTG]"}

#Define function for getting re cut sites for a given restriction enzyme sequence
def GetDigestSites(seq, site):
    #Save where the cut site is ("*") and then remove it from the sequence
    cutSite=site.find("*")
    reSite=site.replace("*", "")
    
    #Lookup any ambiguous nt in IUPAC dictionary, replace nt
    reSite_IUPAC=''.join(IUPAC.get(s, s) for s in reSite)
    
    #find occurences of re sequence
    reSite_Loc=re.finditer(reSite_IUPAC, seq)
    
    #initialize list to get all actual cut sites
    reCut_Loc=[]
    
    #Get all cut sites (asterisk location)
    for match in reSite_Loc:
        run_start=match.start()
        reCut_Loc.append(run_start+cutSite)
    return(reCut_Loc)


AllCutSites=[]    
for site in AllSites:
    AllCutSites.append(GetDigestSites(seq, site))

#Collapse all sites into a single list
AllCutSites=sum(AllCutSites, [])


#Add to sites: the location of the first and final nts. Used for chopping first/last fragment. 
AllCutSites.append(len(seq))
AllCutSites.append(0)

#Order cut sites largest to smalles
AllCutSites.sort()
    
#For each cut site, cut fragment between each
Fragments=[]
for site in range(len(AllCutSites)-1):
    start=AllCutSites[site]
    end=AllCutSites[site+1]
    Fragments.append(seq[start:end])


        
#Print out the length of each fragment    
for fragment in Fragments:
	print("Fragment length: " + str(len(fragment)))
    
    
#Export each fragment out to file, one line per fragment
with open('DigestedFragments.txt', 'w') as f:
    for fragment in Fragments:
        f.write("%s\n" % fragment)
        
        
