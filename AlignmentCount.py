#!/usr/bin/python
import math
'''
  The purpose of this program, which is not complete, since we were
developing it in class, is to calculate Sij = log2(Mij/Eij), for one
pair of amino acids, i and j.  Sij is one value in the substitution matrix.
Calculate also Sii and Sjj.
'''
infile = open("C://Users/Armen/Documents/Alignments.txt")
countAM = 1 #Count for amino acid A and M pairing
countAA= 1 #Count for amino acid A and A pairing
countMM = 1 #Count for amino acid M and M pairing
countA = 1 #Count for the number of amino acid A in the file
countM = 1 #Count for the number of amino acid M in the file
lines = list(infile)
for i in range(0, len(lines), 4) :
  a = lines[i]
  b = lines[i+1]
  c = lines[i+2]
  d = lines[i+3]
  print (a)
  print (b)
  print (c)
  print (d)
  print ('-----------------')
  if len(d) > 5 :
   print (d, ' trouble at ', str(i))

for j in range(len(d)) :
  print('AAAAAAA')
  if (a[i] == 'A' and c[i] == 'M') or (a[i] == 'M' and c[i] == 'A') :
        print (a[j], b[j], c[j])
        countAM = countAM + 1
  if(b[j] == 'A' and d[j] == 'M') or (b[j] == 'M' and d[j] == 'A') :
         print(b[j], d[j])
         countAM = countAM + 1
  if(a[j] == 'A' and c[j] == 'A') :
        print(a[j],c[j])
        countA += 2
  if(a[j] == 'M' and c[j] == 'M') :
        print(a[j], c[j])
        countM += 2
     #if(a[j] == 'A' and c[j] != '-' and c[j] != 'A') :
      # countA += 1
     #if(c[j] == 'A' and a[j] != '-' and a[j] != 'A') :
      #  countA += 1
     #if(a[j] == 'M' and c[j] !='-' and c[j] != 'M') :
      #  countM += 1
     #if(a[j] == 'A' and c[j] == 'A') or (c[j] == 'A' and d[j] == 'A') :
      # countA += 1


print('countAM = ', countAM)
print('countAA = ', countAA)
print('countMM = ', countMM)
print('countA = ', countA)
print('countM = ', countM)


n = 264 * 10
M_AM = countAM/float(n)
M_AA = countAA/float(n)
M_MM = countMM/float(n)
pA = float(countA)/ float(2*n)
pM = float(countM)/ float(2*n)
E_AM = 2 * (pA) * (pM)
E_AA =(pA) * (pA)
E_MM =(pM) * (pM)
S_AM = math.log(M_AM/E_AM,2)
S_AA = math.log(M_AA/E_AA,2)
S_MM = math.log(M_MM/E_MM,2)

print('Saa = ', S_AA)
print('Smm = ', S_MM)
print('Sam = ', S_AM)
