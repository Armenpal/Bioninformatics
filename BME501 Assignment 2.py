#BME501 Assignment 2
'''
Compares two dna sequences and lists the mutations
in the format F508G  meaning F was changed to G at
postion 508 in the amino acid sequence
CDSsrebf1.txt is the coding sequence for srebf1
PROsrebf1.txt is the amino acid sequence for srebf1 protein
mutant.txt is almost the same as CDSsrebf1 but with two bases changed.
'''
# opening the files.
#Note change the input files when comparing different sequences
infile1 = open("C://Users/Armen/Documents/NM_013437.4.txt")
infile2 = open("C://Users/Armen/Documents/5012.txt")
infile3 = open("C://Users/Armen/Documents/NM_001135703.2.txt")
# -----------------------------------------------------
# reading the nucleotide sequence for WT SREBF1
print(infile1.readline())
seq1 = infile1.read()
len1 = len(seq1) 
seq1 = seq1.replace('\n', '')
len1 = len(seq1) 
# --------------------------------------------
# reading the mutant file
print(infile3.readline())
mutant = infile3.read()
mutant = mutant.replace('\n', '')
#---------------------------------------
# reading the protein file
# which is used to check our codon dictionary
print(infile2.readline())
wtPRO = infile2.read()
wtPRO = wtPRO.replace('\n', '') 
#---------------------------------------------------------
# setting up the dictionary
letters = ('G', 'A', 'C', 'T') 
codes = []
for a in letters :
    for b in letters :
        for c in letters :
            codes.append(a + b + c)

aa = 'ggggeeddaaaavvvvrrsskknnttttmiiirrrrqqhhppppllllwxccxxyyssssllff'
aa = aa.upper()

codons = {}
for i in range(64) :
    codons[codes[i]] = aa[i]
# ------------------------------------------------------------
# making the protein from the WT SREBF1, which is seq1
protein = ''
for i in range(0, len(seq1), 3) :
    codon = seq1[i:i+3]
    aminoacid = codons[codon]
    protein += aminoacid
# -----------------------------------------------------------
# making the protein from the mutant SREBF1, which is mutant
mutantPRO = ''
for i in range(0, len(mutant), 3) :
    codon = mutant[i:i+3]
    aminoacid = codons[codon]
    mutantPRO += aminoacid
# --------------------------------------------------------
# quick check if WT and mutant are the same for the protein
if protein == mutantPRO :
    print ('The protein sequences are the same.')
else :
    print ('The protein sequences are different.')
# --------------------------------------------------------
# Printing the differences in the format XiY
# which means WT amino acid X at position i changed to mutant amino acid Y
print ('-------------------------')
print ('The mutations are:')

smCount = 0 #Silent Mutation Count
nonsmCount = 0 #Non-Silent Mutation Count

for i in range(len(protein)) :
     if protein[i] != mutantPRO[i] :
        nonsmCount = nonsmCount + 1
        print(protein[i] + str(i) + mutantPRO[i])
                      
for a in range(0,len(seq1),3) :
        if codons[seq1[a:a+3]] == codons[mutant[a:a+3]] :
            if seq1[a:a+3] != mutant[a:a+3] : 
                for x in range(a,a+3) :
                    if seq1[x] != mutant[x] :
                        print(codons[seq1[a:a+3]] + str(int(x/3)) +
                        codons[mutant[a:a+3]] + ' ' + 'silent mutation'
                         + ' ' + seq1[x] + str(x) + mutant[x])
                        smCount = smCount + 1

                   
print ('Number of Silent Mutations: ', smCount)
print ('Number of Non-Silent Mutations: ', nonsmCount)

        

