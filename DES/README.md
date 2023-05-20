# Decrypting the DES algorithm
This repository contains the implementation of decryption of a DES encryption system as part of our course CS641A.

### Preliminaries

We first ran an automated script to generate 100 pairs of plaintext-ciphertext to get an idea about the ciphertext-space. Upon further analysis of these 100 pairs, we figured out that the ciphertext space contained **English alphabets f to u**. So we realised that the ciphertext space contained exactly 16 alphabets, suggesting that they might be mapped from 0 to 16 as follows: 


_f-0000_

_g-0001_

_h-0010_

_i−0011_

_j−0100_

_k−0101_

_l−0110_

_m−0111_

_n−1000_

_o−1001_

_p−1010_

_q−1011_

_r−1100_ 

_s−1101_

_t−1110_

_u−1111_
