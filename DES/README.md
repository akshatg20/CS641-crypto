# Decrypting the DES algorithm
This repository contains the implementation of decryption of a DES encryption system as part of our course CS641A.

### Preliminaries

We first ran an automated script to generate 100 pairs of plaintext-ciphertext to get an idea about the ciphertext-space. Upon further analysis of these 100 pairs, we figured out that the ciphertext space contained **English alphabets f to u**. So we realised that the ciphertext space contained exactly 16 alphabets, suggesting that they might be mapped from 0 to 16 as follows: 


_f-0000_<br />
_g-0001_<br />
_h-0010_<br />
_i−0011_<br />
_j−0100_<br />
_k−0101_<br />
_l−0110_<br />
_m−0111_<br />
_n−1000_<br />
_o−1001_<br />
_p−1010_<br />
_q−1011_<br />
_r−1100_ <br />
_s−1101_<br />
_t−1110_<br />
_u−1111_<br />

This was also consistent with the message given by the soul which stated the following - "two letters for one byte", i.e. **one letter is represented by 4 bits.**

### Encryption System and Method of Attack

The spirit mentions that the cryptosystem used is a 4-round or a 6-round DES. We assumed a **6-round DES encryption system.**</br>
To break this DES, we performed a known plaintext attack. The plaintexts were generated using the mapping explained above and consisted of alphabets from _f to u_.
