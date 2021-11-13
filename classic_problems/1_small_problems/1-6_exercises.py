""" Exercises
1. Write yet another function that solves for element n of the Fibonacci sequence, 
using a technique of your own design. Write unit tests that evaluate its correctness 
and performance relative to the other versions in this chapter.

2. You saw how the simple int type in Python can be used to represent a bit string. 
Write an ergonomic wrapper around int that can be used generically as a sequence of bits 
(make it iterable and implement __getitem__()). Reimplement CompressedGene, using the wrapper.

3. Write a solver for The Towers of Hanoi that works for any number of towers.

4. Use a one-time pad to encrypt and decrypt images.
"""

# exercise 1

def fib(n):
    fib_dict = {}
    fib_dict[0] = 0
    fib_dict[1] = 1
    for i in range(2, n+1):
        fib_dict[i] = fib_dict[n-1] + fib_dict[n-2]
    
    return fib_dict[n]

# exercise 2

# exercise 3

# exercise 4, take a unit8, grayscale image for example


import cv2
import numpy as np
from secrets import token_bytes
import matplotlib.pyplot as plt
from typing import Tuple


def encrypt(img: np.ndarray) -> Tuple[int, int]: 
    dummy: int = np.random.randint(low=0, high=255, size=img.shape, dtype=np.uint8)
    encrypted: int = img ^ dummy # XOR
    return dummy, encrypted


def decrypt(key1, key2) -> str:
    decrypted = key1 ^ key2 # XOR operation, but it's bits 

    return decrypted

if __name__ == "__main__":
    img = cv2.imread("/Users/kaiyi/Desktop/desktop.png")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key, encrypt_img = encrypt(img=img_gray)
    fig, ax = plt.subplots(1, 2, figsize=(16, 9))
    ax[0].imshow(img_gray, cmap="gray")
    ax[0].set_title("Origin")
    ax[1].imshow(encrypt_img, cmap="gray")
    ax[1].set_title("Encrypt")