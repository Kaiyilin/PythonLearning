"""A one-time pad is a way of encrypting a piece of data by combining it 
with meaningless random dummy data in such a way 
that the original cannot be reconstituted 
without access to both the product and the dummy data.

ie. one time pad results in 2 keys that can be separated 
and then recombined to re-create the original data

Three criteria for dummy data to generate unbreakable encryption:
1. same length as the original data : too short might have observable patterns
2. truly random : for computers, unfortunately this answer is not
3. completely secret : if not the attacker has a clue

for pseudo-random data we can use token_ bytes() from the secrets module

XOR (exclusive or) True table
when both input are false return false
when one input is true and the other is false return tre
when both input are true return false

A B | Y
_______
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0

for 2 8 bit data

a: 00101011 -> 43
b: 10110101 -> 181

a ^ b -> 10011110 -> 158

you can type 0b10110101 ^ 0b00101011 in python promt
which will returns 158 for you

so if we let c = 10011110
what about c ^ b?
c: 10011110
a: 00101011

c ^ a -> 10110101

you're right is exactly b and vice versa if c ^ b!


so, to summarise the below code, we want to encypted a message with one-pad

in random_key
    we need a funtion to generate a random token with same bytes of length 
    as your input the convert it to integer

in encrypt
    we encode the message (str) to bytes
    generate the dummy data (another key) using random key function
    make the byes of msg to int
    encypted the msg in int using XOR with dummy

in decode
    re-generate the int, 
    convert it to bytes
    decode the string in bytes

"""

from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it 
    # the method int.from_bytes() is used to convert form bytes to int
    # from_bytes() method will take 7 bytes 
    # (7 bytes * 8 bits = 56 bits) and convert them into a 56-bit integer.
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]: 
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes)) 
    original_key: int = int.from_bytes(original_bytes, "big") # swith the info to int, the "big" means it's the byte-ordering used to store data.
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted

def decrypt(key1, key2) -> str:
    decrypted = key1 ^ key2 # XOR operation, but it's bits 

    # the int is converted to bytes using int.to_bytes()
    # It was necessary to add 7 to the length of the decrypted data 
    # before using integer-division (//) to divide by 8 
    # to ensure that we “round up,” to avoid an off-by-one error.
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big") 
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!") 
    result: str = decrypt(key1, key2) 
    print(result)