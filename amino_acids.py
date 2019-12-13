#!/usr/bin/python
 
Amino_acids_1 = ['A','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y']
Amino_acids_2 = ['A','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y']
Amino_acids_3 = ['A','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y']
for index in range(len(Amino_acids_1)):
    for index in range(len(Amino_acids_2)):
        for index in range(len(Amino_acids_3)):
   print 'Current Amino_acid_match :', Amino_acids_1[index],Amino_acids_2[index],Amino_acids_3[index]
 
print "Good bye!"
