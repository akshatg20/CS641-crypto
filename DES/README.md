# Decrypting the DES algorithm
This repository contains the implementation of decryption of a DES encryption system as part of our course CS641A.

### Preliminaries

We first ran an automated script to generate 100 pairs of plaintext-ciphertext to get an idea about the ciphertext-space. Upon further analysis of these 100 pairs, we figured out that the ciphertext space contained **English alphabets f to u**. So we realised that the ciphertext space contained exactly 16 alphabets, suggesting that they might be mapped from 0 to 16 as follows: 

***f - 0000
 g - 0001
 h - 0010
 ***
 
 
