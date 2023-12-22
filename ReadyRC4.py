import codecs
# Hàm khởi tạo
def KSA(key):
    key_length = len(key)
    # Khởi tạo mảng S
    S = list(range(256))  # [0,1,2, ... , 255]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Hoán vị
    return S

# Hàm sinh số
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Hoán vị 
        K = S[(S[i] + S[j]) % 256]
        yield K

# Hàm sinh khóa
def get_keystream(key):

    S = KSA(key)
    return PRGA(S)

# Plaintext XOR Keystream = Ciphertext
def encrypt_logic(key, text):
    key = [ord(c) for c in key]
    keystream = get_keystream(key)
    res = []
    for c in text:
        val = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)


def encrypt(key, plaintext):
    plaintext = [ord(c) for c in plaintext]
    return encrypt_logic(key, plaintext)


def decrypt(key, ciphertext):
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = encrypt_logic(key, ciphertext)
    return codecs.decode(res, 'hex_codec').decode('utf-8')


def main():

    key = 'meow'  # plaintext
    plaintext = 'minhkingkong'  # plaintext
    ciphertext = encrypt(key, plaintext)
    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)

    decrypted = decrypt(key, ciphertext)
    print('decrypted:', decrypted)

    if plaintext == decrypted:
        print('OKOKOK')
    else:
        print('Ko the xay ra')



if __name__ == '__main__':
    main()