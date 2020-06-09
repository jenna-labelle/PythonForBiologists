# PythonForBiologists
## Exercises from Dr. Martin Jones' Python For Biologists book, all converted to command-line executable python scripts


`SequenceMetrics.py`: Given an input DNA sequence, prints standard sequence data (AT content, GC content, complement

`SpliceSequence.py`: Given an input DNA sequence + file with exon splice sites (start,end), writes out file with all exons spliced together

`TrimAdapters.py`: Given DNA sequences (1 per line) + length of adapters, writes out file of adapter trimmed sequences

`RestrictionDigest.py`: Given a DNA sequence + restriction enzyme sites (ambiguous bases allowed, cut deliminated by "\*"), performs a restriction enzyme digest with all enzymes, prints out fragment lengths, and writes out all fragments (1 per line) to a file

`Translate_CalculateResiduePercentage.py`: Given DNA sequences (1 per line) + codon table (.csv format) + desired residues, converts DNA to amino acids using the 1st ORF, prints out percentage of each amino acid chain that's composed of the given residues, and writes all amino acid sequences to a file (1 per line)
