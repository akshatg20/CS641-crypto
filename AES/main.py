from utils import *
import subprocess
import numpy as np

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i, "b"))
    numi = int(num[3]) + 2 * int(num[2]) + int(num[1]) * 4 + int(num[0])*8
    mapping[num] = chr(ord('f')+numi)


#known plaintext attack
file = open("plaintext.txt", "w+")
for i in range(8):
    for j in range(128):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + \
            mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        file.write(strr)
        file.write(" ")
    file.write("\n")
file.close()

# Create input file to interact with the shell
file = open("bash_input.txt", "w+")
file.write(f"{teamname}\n")
file.write(f"{password}\n")
file.write("5\n")
file.write("go\n")
file.write("wave\n")
file.write("dive\n")
file.write("go\n")
file.write("read\n")
file.write("password\n")
file.write("c\n")
for i in range(8):
    for j in range(128):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + \
            mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        file.write(strr)
        file.write("\n")
        file.write("c\n")
file.write("back\n")
file.write("exit")
file.close()

subprocess.run("bash script.sh",shell=True)

# Parse bash output
file = open('bash_output.txt', mode='r', encoding='utf-8-sig')
line = file.readlines()
text = []
for i in line:
    i = i.strip()
    text.append(i)
file.close()
encrypted_password = text.pop(0)
file = open("ciphertext.txt", "w+")
for i in range(1024):
    if i != 0 and i % 128 == 0:
        file.write("\n")
    file.write(text[i])
    file.write(" ")
file.close()

#Find possible values for diagonal and exponent matrices
possible_exponent_mat = [[] for i in range(8)]
possible_diag = [[[] for i in range(8)] for j in range(8)]

input_file = open("plaintext.txt", 'r')
output_file = open("ciphertext.txt", 'r')

for idx, (input_line, output_line) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    input_str = []
    output_str = []
    for hex_input in input_line.strip().split(" "):
        input_str.append(block2hex(hex_input)[idx])
    for hex_output in output_line.strip().split(" "):
        output_str.append(block2hex(hex_output)[idx])
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for inps, outs in zip(input_str, output_str):
                if ord(outs) != binpow(field.Multiply(binpow(field.Multiply(binpow(ord(inps), i), j), i), j), i):
                    flag = False
                    break
            if flag:
                possible_exponent_mat[idx].append(i)
                possible_diag[idx][idx].append(j)

# eliminate extra values
input_file = open("plaintext.txt", 'r')
output_file = open("ciphertext.txt", 'r')

for idx, (input_line, output_line) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    if idx > 6 :
        break
    input_str = []
    output_str = []
    for hex_input in input_line.strip().split(" "):
        input_str.append(block2hex(hex_input)[idx]) 
    for hex_output in output_line.strip().split(" "):
        output_str.append(block2hex(hex_output)[idx+1])
    for i in range(1, 128):
        for p1, e1 in zip(possible_exponent_mat[idx+1], possible_diag[idx+1][idx+1]):
            for p2, e2 in zip(possible_exponent_mat[idx], possible_diag[idx][idx]):
                flag = True
                for inp, outp in zip(input_str, output_str):
                    if ord(outp) != binpow(int(field.Multiply(binpow(field.Multiply(binpow(ord(inp), p2), e2), p2), i)) ^ int(field.Multiply(binpow(field.Multiply(binpow(ord(inp), p2), i), p1), e1)), p1):
                        flag = False
                        break
                if flag:
                    possible_exponent_mat[idx+1] = [p1]
                    possible_diag[idx+1][idx+1] = [e1]
                    possible_exponent_mat[idx] = [p2]
                    possible_diag[idx][idx] = [e2]
                    possible_diag[idx][idx+1] = [i]

for idx in range(6):
    of = idx + 2
    
    exponent_mat = [e[0] for e in possible_exponent_mat]
    lin_trans_mat = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            lin_trans_mat[i][j] = 0 if len(possible_diag[i][j]) == 0 else possible_diag[i][j][0]
    input_file = open("plaintext.txt", 'r')
    output_file = open("ciphertext.txt", 'r')
    for idx, (input_line, output_line) in enumerate(zip(input_file.readlines(), output_file.readlines())):
        if idx > (7-of):
            continue
        input_str = [block2hex(msg) for msg in input_line.strip().split(" ")]
        output_str = [block2hex(msg) for msg in output_line.strip().split(" ")]
        for i in range(1, 128):
            lin_trans_mat[idx][idx+of] = i
            flag = True
            for inps, outs in zip(input_str, output_str):
                if encrypt(inps, lin_trans_mat, exponent_mat)[idx+of] != ord(outs[idx+of]):
                    flag = False
                    break
            if flag:
                possible_diag[idx][idx+of] = [i]
    input_file.close()
    output_file.close()

# Replace [] with 0
lin_trans_mat = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lin_trans_mat[i][j] = 0 if len(possible_diag[i][j]) == 0 else possible_diag[i][j][0]

print("A^T:",end='')
for i in range(len(lin_trans_mat)):
    st = '\t'
    for j in range(len(lin_trans_mat[0])):
        st += str(lin_trans_mat[i][j]) + '\t'
    print(st)
st = '\n\nE:\t'
for i in exponent_mat:
    st += str(i) + '\t'
print(st)

password_1 = encrypted_password[:16] #"gsgfkrfrkpmfknlf"
password_2 = encrypted_password[16:] #"lmmmghmqkmfthulk"

final_pswd = block2hex(decrypt_pswd(password_1,lin_trans_mat,exponent_mat)) + block2hex(decrypt_pswd(password_2,lin_trans_mat,exponent_mat))
print(f'Decrypted Password: {final_pswd}')
print("Final Password:", final_pswd.strip("0"))
