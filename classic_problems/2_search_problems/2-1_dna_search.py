"""In computer programming, an enumerated type 
(also called enumeration, enum, or factor in the R programming language, and a categorical variable in statistics) 
is a data type consisting of a set of named values called elements, members, enumeral, or enumerators of the type
"""

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # type alias for codons 
Gene = List[Codon] # type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def str_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon) # add codon to gene
    return gene

my_gene: Gene = str_to_gene(gene_str)

# Linear search, O(n), loop every element in a search space

def linear_srch(gene: Gene, key_coden: Codon) -> bool:
    for codon in gene:
        if codon == key_coden:
            return True
        return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G) 
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T) 
print(linear_srch(my_gene, acg)) # True
print(linear_srch(my_gene, gat)) # False

# binary search, O(nlog n), only performed if it is sorted

def binary_srch(gene: Gene, key_coden: Codon) -> bool:
    """Gene must be sorted for doing so
    """
    temp_gene = sorted(gene)
    low = 0
    high = len(temp_gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if temp_gene[mid] < key_coden:
            low = mid + 1
        elif temp_gene[mid] > key_coden:
            high = mid - 1
        else:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G) 
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T) 
print(binary_srch(my_gene, acg)) # True
print(binary_srch(my_gene, gat)) # False