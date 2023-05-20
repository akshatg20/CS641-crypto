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
To break this DES, we performed a known plaintext attack. The plaintexts were generated using the mapping explained above and consisted of alphabets from _f to u_. </br>
We moved forward with the following two  **iterative characteristics** that might give us the possible answer:

Characteristic 1 - (40080000,04000000) with probability = 1/16</br>
Characteristic 2 - (00200008,00000400) with probability = 1/16

We conducted our cryptanalysis using these two characteristics in parallel, so as to increase our chances of success. **(NOTE: The characteristics here have been represented in hexadecimal notation)**

We ran an automated script to attack the server with multiple plaintexts and got the needed corresponding ciphetexts. This was done for both the characteristics.

### Partial Key Generation

Each of the two characteristic would let us find 30 bits of _K<sub>6</sub>_, which is the notation for the round key for the 6th round, corresponding to the 5 S-boxes. But as 3 of the S-boxes (_S<sub>2</sub>,S<sub>5</sub>,S<sub>6</sub>_) are common for both the characteristics, we only get **42 bits** of the key. 

The other **14 bits** of the **56-bit key** are found using brute force (explained later).

Using the mapping given at the start, we converted the ciphertexts corresponding to the plaintext pairs into **binary notation of 64 bits**.

Then, we applied the reverse final permutation on them and divided them into two halves to get the values of _L<sub>6</sub>_ and _R<sub>6</sub>_. We then apply expansion on _R<sub>5</sub>_.

Since the XOR  of the output of the expansion box is equal to the XOR  of the input of the S-boxes, we know the XOR of the inputs of the S-boxes also.

We do not know the value of _L<sub>5</sub>_. However, we do know that the XOR of the outputs of some of the S-boxes equals zero, for each characteristic, as specified above. We can use this to find the output XORs of the 6th round (denoted by X') as:

```math
r' \oplus e' = r' \oplus D' \oplus c' = X'
``` 

Where _D′_ is XOR output after permutation in the 4th round, _c′_ is XOR input to expansion in the 3rd round and _e′_ is XOR input to expansion.</br>
Since we know that _D′_ has some S-boxes with zero XOR values, we can determine the XOR outputs of those corresponding bits after permutation in the 6th round. Now, we applied the inverse permutation on this XOR value to get the corresponding output of the S-boxes of the 6th round with some probability.

Now, for each of these five S-boxes, we **iterate over all possible keys** and calculate the inputs as the XOR of the expansion box's output and the key. Then, we apply the respective S-box to each of them and obtain the S-box outputs. 

Finally, we determine whether the  XOR of these outputs equals the **expected** value. We **repeat** this process for **numerous pairs of plaintexts** and select the key that produces the proper XOR output value of the S-boxes the **greatest number of times.**

Utilising this, **30 bits** of the key can be determined (using the 5 S-boxes) by utilising one of the characteristic.

Using the second characteristic, we identify **12 more bits** (**using the two new S-boxes**) and check whether the 18 bits of the key corresponding to the three S-boxes shared by the two characteristics are identical. If it is not identical, we must increase the number of plaintext pairs and locate the optimal key once more. 

We continue to increase the number of pairs until we find a key that satisfies the S-boxes shared by both characteristics. Following are the keys generated with corresponding frequencies:

For characteristic: (40080000,04000000)

Sbox-2 (6-bit key) =  110011  frequency : 41</br>
Sbox-5 (6-bit key) =  111101  frequency : 23</br>
Sbox-6 (6-bit key) =  110000  frequency : 42</br>
Sbox-7 (6-bit key) =  010101  frequency : 30</br>
Sbox-8 (6-bit key) =  110110  frequency : 26

For characterstic: (00200008,00000400)

Sbox-2 (6-bit key) =  101101  frequency : 18</br>
Sbox-5 (6-bit key) =  110011  frequency : 15</br>
Sbox-6 (6-bit key) =  000111  frequency : 33</br>
Sbox-7 (6-bit key) =  111101  frequency : 20</br>
Sbox-8 (6-bit key) =  110000  frequency : 39

We therefore calculated the **Partial Key** as follows: 
['#', '1', '1', '#', '#', '1', '#', '#', '0', '1', '0', '1', '1', '#', '1', '0', '0', '#', '#', '1', '1', '#', '1', '1', '0', '0', '0', '#', '0', '0', '1', '0', '0', '1', '1', '#', '1', '1', '1', '1', '1', '0', '0', '0', '#', '1', '1', '#', '0', '1', '1', '1', '#', '0', '0', '1']
