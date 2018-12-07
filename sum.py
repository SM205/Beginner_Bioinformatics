file = input("Enter the full path to the FASTA file you want to use for this function\n")
sequence = open(file,"r")

info = sequence.readline()

line = sequence.readlines()

a=0
t=0
g=0
c=0

for nucleotides in line:
    for nucleotide in nucleotides:
        if "A" in nucleotide:
            a+=1
        elif "T" in nucleotide:
            t+=1
        elif "G" in nucleotide:
            g+=1
        elif "C" in nucleotide:
            c+=1
    

sequence.close()

print("The given sequence's information is as given below")
print(info)
print("The number of Adenine nucleotides is:" ,a)
print("The number of Tyrosine nucleotides is:",t)
print("The number of Guanine nucleotides is:",g)
print("The number of Cytosine nucleotides is:",c)
print("The total number of nucleotides in the given organism is:",(a+t+g+c))
