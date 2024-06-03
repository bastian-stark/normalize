def revComp(seq):
    nucComps = {"A": "T", "T": "A", "G": "C", "C": "G"}
    newSeq = []
    for nuc in seq:
        for key in nucComps:
            if nuc == key:
                newSeq.append(nucComps[key])
    newSeq.reverse()
    newSeq2 = ''
    for line in newSeq:
        newSeq2 = newSeq2 + line
    return newSeq2

bedCountsFile = input("Enter name of file containing counts from BED file: ")
genomicCountsFile = input("Enter name of file containing total genomic counts: ")
bedCountsInfile = open(f"{bedCountsFile}.txt")
genomicCountsInfile = open(f"{genomicCountsFile}.txt")
outfile = open(f"{bedCountsFile}_normalized.txt", "w")
bedCounts = bedCountsInfile.readlines()
genCounts = genomicCountsInfile.readlines()

normalizedCounts = {}
for bedLine in bedCounts:
    bedLine = bedLine.split()
    if bedLine[0] not in normalizedCounts:
        normalizedCounts[bedLine[0]] = 0
    for genLine in genCounts:
        genLine = genLine.split()
        if genLine[0] == bedLine[0] or revComp(genLine[0]) == bedLine[0]:
            normalizedCounts[bedLine[0]] = round(float(bedLine[1])/float(genLine[1]), 25)

for key in normalizedCounts:
    outfile.write(key + '\t' + str(normalizedCounts[key]) + '\n')
