from pyfinite import ffield

# Create a 0-16 map-set
bit2let = {'0000': 'f',
           '0001': 'g',
           '0010': 'h',
           '0011': 'i',
           '0100': 'j',
           '0101': 'k',
           '0110': 'l',
           '0111': 'm',
           '1000': 'n',
           '1001': 'o',
           '1010': 'p',
           '1011': 'q',
           '1100': 'r',
           '1101': 's',
           '1110': 't',
           '1111': 'u'}

exp_arr = [[-1]*128 for i in range(128)]

field = ffield.FField(7)

def binpow(no, pow):
    if exp_arr[no][pow] != -1:
        return exp_arr[no][pow]

    ans = 0
    if pow == 0:
        ans = 1
    elif pow == 1:
        ans = no
    elif pow % 2 == 0:
        sqrt_no = binpow(no, pow >> 1)
        ans = field.Multiply(sqrt_no, sqrt_no)
    else:
        sqrt_no = binpow(no, pow >> 1)
        ans = field.Multiply(sqrt_no, sqrt_no)
        ans = field.Multiply(no, ans)

    exp_arr[no][pow] = ans
    return ans

def add_vectors(v1, v2):
    ans = [0]*8
    for i, (e1, e2) in enumerate(zip(v1, v2)):
        ans[i] = int(e1) ^ int(e2)
    return ans

def scalar_mul(v, elem):
    ans = [0]*8
    for i, e in enumerate(v):
        ans[i] = field.Multiply(e, elem)
    return ans

def lin_transform(mat, elist):
    ans = [0]*8
    for row, elem in zip(mat, elist):
        val = [0]*8
        for i, (e1, e2) in enumerate(zip(scalar_mul(row, elem), ans)):
            val[i] = int(e1) ^ int(e2)
        ans = val
    return ans

def encrypt(plaintext, lin_mat, exp_mat):
    plaintext = [ord(c) for c in plaintext]
    ans = [[0 for j in range(8)] for i in range(8)]
    for idx, elem in enumerate(plaintext):
        ans[0][idx] = binpow(elem, exp_mat[idx])

    ans[1] = lin_transform(lin_mat, ans[0])

    for idx, elem in enumerate(ans[1]):
        ans[2][idx] = binpow(elem, exp_mat[idx])

    ans[3] = lin_transform(lin_mat, ans[2])

    for idx, elem in enumerate(ans[3]):
        ans[4][idx] = binpow(elem, exp_mat[idx])
    return ans[4]

# byte to string
def byte2str(b):
    binnum = '{:0>8}'.format(format(b, "b"))
    a = bit2let[binnum[0:4]], bit2let[binnum[4:8]]
    return a[0]+a[1]

# byte to hex
def byte2hex(st):
    char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
    return char

# block to hex
def block2hex(c):
    plainText = ""
    for i in range(0, len(c), 2):
        plainText += byte2hex(c[i:i+2])
    return plainText

def decrypt_pswd(pswd,linear_mat,exponent_mat):
    pswd_hex = block2hex(pswd)
    decrypted_pswd = ""
    for idx in range(8):
        for ans in range(128):
            inp = decrypted_pswd + byte2str(ans)+(16-len(decrypted_pswd)-2)*'f'
            if ord(pswd_hex[idx]) == encrypt(block2hex(inp), linear_mat, exponent_mat)[idx]:
                decrypted_pswd += byte2str(ans)
                break
    return decrypted_pswd