LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Return Greatest Common Divisor of a and b
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# Return Inverse Module of a with mod m
def inverseMod(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# Return Affine Cipher with MODE encrypt or decrypt
def affine_cipher(message, MODE, key):
    message = message.upper()
    translated = ''
    modInverseOfKeyA = inverseMod(key[0], len(LETTERS))
    if modInverseOfKeyA == None:
        return None
    for symbol in message:
        if symbol in LETTERS:
            symIndex = LETTERS.find(symbol)
            if MODE.upper() == 'ENCRYPT':
                translated += LETTERS[(symIndex * key[0] + key[1]) % len(LETTERS)]
            elif MODE.upper() == 'DECRYPT':
                translated += LETTERS[(symIndex - key[1]) * modInverseOfKeyA % len(LETTERS)]
        else:
            translated += symbol
    return translated


import detectEnglish as detectEnglish

# Crack Affine Cipher
def affine_crack(cipher):
    
    for a in range(0, 26):
        if gcd(a, 26) == 1:
            for b in range(0, 26):            
                message = affine_cipher(cipher, 'DECRYPT', (a, b))
                if detectEnglish.isEnglish(message):
                    return (a, b, message)
            
    return (None, None)


message = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
key = (7, 2)
cipher = affine_cipher(message, 'ENCRYPT', key)

print('Plain text:  ' + message)
print('Cipher text: ' + cipher)

message = affine_crack(cipher)
print('Key = ({0}, {1})'.format(message[0], message[1]))
print('Plain text after crack:  ' + message[2])