""" << in Python
They are bit shift operator which exists in many mainstream programming languages, 
<< is the left shift and >> is the right shift, they can be demonstrated as the following table, 
assume an integer only take 1 byte in memory.

| operate | bit value | octal value |                       description                        |
| ------- | --------- | ----------- | -------------------------------------------------------- |
|         | 00000100  |           4 |                                                          |
| 4 << 2  | 00010000  |          16 | move all bits to left 2 bits, filled with 0 at the right |
| 16 >> 2 | 00000100  |           4 | move all bits to right 2 bits, filled with 0 at the left |

|= : in-place or

>>> s1 = {"a", "b", "c"}
>>> s2 = {"d", "e", "f"}

>>> # OR, | 
>>> s1 | s2
{'a', 'b', 'c', 'd', 'e', 'f'}
>>> s1                                                     # `s1` is unchanged
{'a', 'b', 'c'}

>>> # In-place OR, |=
>>> s1 |= s2
>>> s1                                                     # `s1` is reassigned
{'a', 'b', 'c', 'd', 'e', 'f'}


0b is the Python prefix for the representation of binary numbers
therefore 
>>> 0b01
1 
>>> 0b11
3
>>> 0b10000000000
1024

note: bin() in python helps you Convert an integer number (must) to a binary string

>>> bin(1024) 
'0b10000000000'
"""


# if gene info stored in str, it's an Unicode character which requires 8 bit per nucleotide
# in binary, onlt 2 bit, (e.g. "A" : 00, "T" : 11, "G" : 10, "C" : 01)  
# i.e. the info can be stored in bit string

class CompressedGene(object):
    def __init__(self, gene: str) -> None:
        # convetionally, methods start with _ are private methods
        self._compress(gene) 
    
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # start with sentinel, bit value is like 000001
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # shift left 2 bits 
            if nucleotide == "A": # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # change last two bits to 11
                self.bit_string |= 0b11 
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str: 
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11 # get just 2 relevant bits 
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T" 
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1] # [::-1] reverses string by slicing backward
        
    def __str__(self) -> str: # string representation for pretty printing 
        return self.decompress()
