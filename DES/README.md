# Decrypting the DES algorithm
This repository contains the implementation of decryption of a DES encryption system as part of our course CS641A.

### Preliminaries

We first ran an automated script to generate 100 pairs of plaintext-ciphertext to get an idea about the ciphertext-space. Upon further analysis of these 100 pairs, we figured out that the ciphertext space contained **English alphabets f to u**. So we realised that the ciphertext space contained exactly 16 alphabets, suggesting that they might be mapped from 0 to 16 as follows: 


_f-0000_
g-0001
h-0010
i−0011
j−0100 
k−0101 
l−0110 
m−0111 
n−1000 
o−1001 
p−1010 
q−1011 
r−1100 
s−1101 
t−1110 
u−1111
