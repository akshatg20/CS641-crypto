import os
import random
import numpy as np

#des declarations
init_perm =  [[58, 50, 42, 34, 26, 18, 10, 2],
                       [60, 52, 44, 36, 28, 20, 12, 4],
                       [62, 54, 46, 38, 30, 22, 14, 6],
                       [64, 56, 48, 40, 32, 24, 16, 8],
                       [57, 49, 41, 33, 25, 17, 9, 1],
                       [59, 51, 43, 35, 27, 19, 11, 3],
                       [61, 53, 45, 37, 29, 21, 13, 5],
                       [63, 55, 47, 39, 31, 23, 15, 7]]

rev_init_perm =  [[40, 8, 48, 16, 56, 24, 64, 32],
                           [39, 7, 47, 15, 55, 23, 63, 31],
                           [38, 6, 46, 14, 54, 22, 62, 30],
                           [37, 5, 45, 13, 53, 21, 61, 29],
                           [36, 4, 44, 12, 52, 20, 60, 28],
                           [35, 3, 43, 11, 51, 19, 59, 27],
                           [34, 2, 42, 10, 50, 18, 58, 26],
                           [33, 1, 41, 9, 49, 17, 57, 25]]

rev_final_perm =  [[57, 49, 41, 33, 25, 17, 9, 1],
                         [59, 51, 43, 35, 27, 19, 11, 3],
                         [61, 53, 45, 37, 29, 21, 13, 5],
                         [63, 55, 47, 39, 31, 23, 15, 7],
                         [58, 50, 42, 34, 26, 18, 10, 2],
                         [60, 52, 44, 36, 28, 20, 12, 4],
                         [62, 54, 46, 38, 30, 22, 14, 6],
                         [64, 56, 48, 40, 32, 24, 16, 8]]

final_perm =  [[8, 40, 16, 48, 24, 56, 32, 64],
                     [7, 39, 15, 47, 23, 55, 31, 63],
                     [6, 38, 14, 46, 22, 54, 30, 62],
                     [5, 37, 13, 45, 21, 53, 29, 61],
                     [4, 36, 12, 44, 20, 52, 28, 60],
                     [3, 35, 11, 43, 19, 51, 27, 59],
                     [2, 34, 10, 42, 18, 50, 26, 58],
                     [1, 33, 9,  41, 17, 49, 25, 57]]

expansion = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

perm = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

perm_inv = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]

s_blocks = {
    1: [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    2: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    3: [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    4: [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    5: [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    6: [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    7: [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    8: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
}

par_bit_drop_tab = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

shift_lef_tab = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

key_comp_tab = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]


def apply_init_perm(n):
    if len(n) == 16:
        n = hex_to_binary(n)
    t = ""
    for i in range(len(n)):
        t += n[init_perm[i//8][i % 8]-1]
    return t


def apply_final_perm(n):
    if len(n) == 16:
        n = hex_to_binary(n)
    t = ""
    for i in range(len(n)):
        t += n[final_perm[i//8][i % 8]-1]
    return t


def apply_rev_init_perm(n):
    if len(n) == 16:
        n = hex_to_binary(n)
    t = ""
    for i in range(len(n)):
        t += n[rev_init_perm[i//8][i % 8]-1]
    return t


def apply_rev_final_perm(n):
    # print(n)

    if len(n) == 16:
        n = hex_to_binary(n)
    t = ""
    for i in range(len(n)):
        t += n[rev_final_perm[i//8][i % 8]-1]
    return t


def apply_perm(n):
    t = ""
    for i in range(len(n)):
        t += n[perm[i]-1]
    return t


def apply_inv_perm(n):
    t = ""
    for i in range(len(n)):
        t += n[perm_inv[i]-1]
    return t


def hex_to_binary(n):
    s = ""
    for c in n:
        if c.isalpha():
            c = ord(c.lower())-87
        s += "{:0>4b}".format(int(c))
    return s


def binary_to_hex(n):
    s = ""
    for i in range(0, len(n), 4):
        s += "{:x}".format(int(n[i:i+4], 2))
    return s


def binary_to_str(n):
    t = ""
    for i in range(0, len(n), 4):
        t += chr(ord('f') + int(n[i:i+4], 2))
    return t


def str_to_binary(n):
    t = ""
    for i in n:
        t += "{:0>4b}".format(ord(i) - 102)
    return t


def apply_expansion(n):
    t = ""
    if len(n) == 8:
        n = hex_to_binary(n)

    if len(n) == 32:
        for i in range(48):
            t += n[expansion[i]-1]
    return t


def apply_sbox(n, box):
    t = ""
    row = int(n[0]+n[5], 2)
    col = int(n[1:5], 2)
    t += "{0:0>4b}".format(s_blocks[box][row][col])
    return t


def bit_xor(a, b, l):
    t = ""
    for i in range(l):
        t += str(int(a[i]) ^ int(b[i]))
    return t


def lef_shift_key(n, shifts):
    if type(n) == list:
        while(shifts > 0):
            n.append(n.pop(0))
            shifts -= 1
        return n

def gen_input(diff, x):
    inputs = []
    plain = ""
    for i in range(x):
        plain = ""
        for j in range(16):
            plain += "".join(random.choices([c for c in ciphertxtstring]))

        t1 = str_to_binary(plain)
        t2 = bit_xor(t1, diff, 64)

        t1 = "".join(list(str(c) for c in t1))
        t2 = "".join(list(str(c) for c in t2))

        inputs.append(binary_to_str(t1))
        inputs.append(binary_to_str(t2))
    return inputs


def gen_in_out(no_of_input_pairs, characteristic):

    # generate input pairs and ciphertexts
    fin_per = apply_rev_init_perm(characteristic)  # inverse initial
    input_list = gen_input(fin_per, no_of_input_pairs)
    with open("xor_plaintexts.txt", "w") as f:
        f.write("turing_shuring\nTiGz5@#huJ&\n4\nread\n")
        for input in input_list:
            f.write(f'{input}\nc\n')
        f.write("back\nexit\n")

    os.system("./generate_xor_ciphertexts.sh")
    with open('xor_ciphertexts.txt', 'r') as f:
        output_list = [line.strip() for line in f.readlines()]

    if characteristic == characteristic1:
        with open("plaintext.txt", "w") as f:
            for i in input_list:
                f.write(f'{i}\n')
        
        with open("ciphertext.txt", "w") as f:
            for i in output_list:
                f.write(f'{i}\n')
                
    elif characteristic == "0020000800000400":
        with open("plaintext1.txt", "w") as f:
            for i in input_list:
                f.write(f'{i}\n')
        
        with open("ciphertext1.txt", "w") as f:
            for i in output_list:
                f.write(f'{i}\n')


def find_k6_of_sboxes(s_in_xor, inv_perm, ex_out, sboxes):
    keys = np.zeros((8, 64), dtype=int)
    for i in range(len(inv_perm)):
        for box in range(0, 8):
            t_s_in_xor = s_in_xor[i][box*6:box*6+6]
            t_s_out_xor = inv_perm[i][box*4:box*4+4]
            t_ex_out1 = ex_out[2*i][box*6:box*6+6]

            for a in range(0, 64):
                a1 = "{:0>6b}".format(a)
                a2 = bit_xor(a1, t_s_in_xor, 6)
                s_a1_xor_a2 = bit_xor(apply_sbox(a1, box+1), apply_sbox(a2, box+1), 4)

                if s_a1_xor_a2 == t_s_out_xor:
                    key = bit_xor(t_ex_out1, a1, 6)
                    keys[box][int(key, 2)] += 1

    k6_sbox = dict()
    freq = dict()
    for i in sboxes:
        k6_sbox["Sbox-"+str(i)] = "{:0>6b}".format(
            np.where(keys[i-1] == keys[i-1].max())[0][0])
        freq["Sbox-"+str(i)] = keys[i-1].max()
    return (k6_sbox, freq)


def encrypt(n, key56, rounds):
    n = apply_init_perm(n)
    k = [x for x in key56]
    for r in range(1, rounds+1):
        R = n[32:]
        L = n[:32]

        R1 = apply_expansion(R)

        left = k[0:28]
        right = k[28:]
        left = lef_shift_key(left, shift_lef_tab[r-1])
        right = lef_shift_key(right, shift_lef_tab[r-1])
        k = left + right
        t = ""
        for j in range(0, 48):
            t += k[key_comp_tab[j]-1]
        key48 = "".join(t)

        s_in = bit_xor(R1, key48, 48)
        s_out = ""
        for i in range(0, 48, 6):
            s_out += apply_sbox(s_in[i:i+6], i//6+1)

        p_out = apply_perm(s_out)
        n = R + bit_xor(p_out, L, 32)

    n = apply_final_perm(n)
    return n


def decryption(p, round_keys, rounds):
    p = apply_rev_final_perm(p)
    R = {6: p[32:]}
    L = {6: p[:32]}
    for r in range(rounds, 0, -1):
        R[r-1] = L[r]
        ex_out = apply_expansion(R[r-1])
        s_in = bit_xor(round_keys[r], ex_out, 48)
        s_out = ""
        for box in range(8):
            s_out += apply_sbox(s_in[box*6:box*6+6], box+1)
        p_out = apply_perm(s_out)
        L[r-1] = bit_xor(p_out, R[r], 32)
    return apply_rev_init_perm(L[0]+R[0])

with open('random_plaintexts.txt', 'w') as f:
    f.write('turing_shuring\nTiGz5@#huJ&\n4\nread\npassword\nc\n')
    for i in range(100):
        f.write(f"{''.join(random.choice(([c for c in 'abcdefghijklmnopqrstuvwxyz'])) for _ in range(16))}\nc\n")
    f.write('back\nexit\n')

os.system('./generate_ciphertext_space.sh')
with open('random_ciphertexts.txt', 'r') as f:
    ciphertxts = [line.strip() for line in f.readlines()]

encrypted_password = ciphertxts[0]    

freq = {}
cnt = 0
for char in ''.join(ciphertxts):
    cnt += 1
    if char in freq.keys():
        freq[char] += 1
    else:
        freq[char] = 1

for key , val in freq.items():
    freq[key] = round(val / cnt * 100, 1)

freq = dict(sorted(freq.items(), key = lambda item: item[0]))
print(f'Frequency analysis of Ciphertext space: {freq}')
ciphertxtstring = ''
for _ in freq.keys():
    ciphertxtstring += _

# Characteristics choosen for 6 Round DES with 1/16 probability
characteristic1 = "4008000004000000"
characteristic2 = "0020000800000400"

no_of_input_pairs = 10000

if not(os.path.exists("plaintext.txt") and os.path.exists("ciphertext.txt")):
    gen_in_out(no_of_input_pairs, characteristic1)
file = open("plaintext.txt", 'r')
inp_list = [x[:-1] for x in file.readlines()]
file = open("ciphertext.txt")
out_list = [x[:-1] for x in file.readlines()]

if not(os.path.exists("plaintext1.txt") and os.path.exists("ciphertext1.txt")):
    gen_in_out(no_of_input_pairs, characteristic2)
file = open("plaintext1.txt", 'r')
inp_list1 = [x[:-1] for x in file.readlines()]
file = open("ciphertext1.txt")
out_list1= [x[:-1] for x in file.readlines()]

binary_output_list = [str_to_binary(c) for c in out_list]
binary_output_list1 = [str_to_binary(c) for c in out_list1]

inv_fper = [apply_rev_final_perm(x) for x in binary_output_list]
inv_fper1 = [apply_rev_final_perm(x) for x in binary_output_list1]

expansion_output = [apply_expansion(x[0:32]) for x in inv_fper]
expansion_output1 = [apply_expansion(x[0:32]) for x in inv_fper1]

s_box_in_xor = [bit_xor(expansion_output[i], expansion_output[i+1], 48) for i in range(0, len(expansion_output), 2)]
s_box_in_xor1 = [bit_xor(expansion_output1[i], expansion_output1[i+1], 48) for i in range(0, len(expansion_output1), 2)]

in_xor = [bit_xor(inv_fper[i], inv_fper[i+1], 64) for i in range(0, len(inv_fper), 2)]
f_out = [x[32:]for x in in_xor[:120]]
in_xor1 = [bit_xor(inv_fper1[i], inv_fper1[i+1], 64) for i in range(0, len(inv_fper1), 2)]
f_out1 = [x[32:]for x in in_xor1[:120]]

inv_perm = [apply_inv_perm(x) for x in f_out]
inv_perm1 = [apply_inv_perm(x) for x in f_out1]


k6, freq_k6 = find_k6_of_sboxes(s_box_in_xor, inv_perm, expansion_output, sboxes=[2, 5, 6, 7, 8])
k6_1, freq_k6_1 = find_k6_of_sboxes(s_box_in_xor1, inv_perm1, expansion_output1, sboxes=[1, 2, 4, 5, 6])

if k6["Sbox-2"] != k6_1["Sbox-2"] or k6["Sbox-5"] != k6_1["Sbox-5"] or k6["Sbox-6"] != k6_1["Sbox-6"]:
    print('More pairs required. ')
else:
    partial_k6 = [k6_1["Sbox-1"], k6_1["Sbox-2"], "######", k6_1["Sbox-4"],k6_1["Sbox-5"], k6_1["Sbox-6"], k6["Sbox-7"], k6["Sbox-8"]]
    partial_k6 = "".join(partial_k6)

    partial_key56 = ["#"] * 56
    partial_key64 = ["#"] * 64
    k = par_bit_drop_tab.copy()
    round_keys = dict()
    for r in range(1, 7):
        left = k[0:28]
        right = k[28:]
        left = lef_shift_key(left, shift_lef_tab[r-1])
        right = lef_shift_key(right, shift_lef_tab[r-1])
        k = left + right
        t = ['#']*48
        for j in range(0, 48):
            t[j] = k[key_comp_tab[j]-1]
        round_keys[r] = t
    
    for i, b in enumerate(round_keys[6]):
        partial_key64[b-1] = partial_k6[i]
    for i in range(56):
        partial_key56[i] = partial_key64[par_bit_drop_tab[i]-1]
    print(f'Round key: {"".join(partial_key56)}')
    print(f'Key: {"".join(partial_key64)}')

# Apply brute-force for remaining 14 bits of 56bits of key
    unknown_bits = []
    for i, c in enumerate(partial_key56):
        if c == '#':
            unknown_bits.append(i)

    final_key = ""
    l = len(unknown_bits)
    for i in range(2**l):
        b = "{:0>14b}".format(i)
        temp_k = partial_key56.copy()
        for j in range(l):
            temp_k[unknown_bits[j]] = b[j]
        temp_k = "".join(temp_k)
        inp = str_to_binary(inp_list[0])

        if binary_to_str(encrypt(inp, temp_k, 6)) == out_list[0]:
            final_key = temp_k
        
    else:
        print("For characteristic =", characteristic1)
        for k in k6:
            print(k, "(6-bit key) = ", k6[k], "  frequency : ", freq_k6[k])

        print("For characteristic =", characteristic2)
        for k in k6_1:
            print(k, "(6-bit key) =",k6_1[k], "  frequency : ", freq_k6_1[k])

        print("\nPartial 56-bit key : ", "".join(partial_key56))
        print("\nFinal 56-bit key : ", final_key)

        print(f'Encrypted password: {encrypted_password}')

    # final_round_keys = gen_round_keys(final_key)

    final_round_keys = {}
    k = [x for x in final_key]
    for r in range(1, 7):
        left = k[0:28]
        right = k[28:]
        left = lef_shift_key(left, shift_lef_tab[r-1])
        right = lef_shift_key(right, shift_lef_tab[r-1])
        k = left + right
        t = ""
        for j in range(0, 48):
            t += k[key_comp_tab[j]-1]

        final_round_keys[r] = "".join(t)
    # Decrypt password using the obtained final_key
    d = decryption(str_to_binary(encrypted_password[:16]), final_round_keys, 6) + decryption(str_to_binary(encrypted_password[16:]), final_round_keys, 6)
    print(f"\n\nPassword in binary form: {d}")

    ans = ""
    for i in range(0, len(d), 8):
        s = d[i:i+8]
        ans += chr(int(s, 2))
    print(f"\nDecrypted password: {ans}")

    # Removing trailing 0s
    while ans[-1] == '0':
        ans = ans[:-1]
    print(f"\nFinal password: {ans}")
