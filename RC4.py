def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, n):
    i = 0
    j = 0
    key_stream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256])
    return key_stream

def rc4_cipher(key, plaintext):
    key_stream = prga(ksa(key), len(plaintext))
    ciphertext = bytes([plaintext[i] ^ key_stream[i] for i in range(len(plaintext))])
    return ciphertext



# Example usage
key = b"SecretKey"
plaintext = b"My name is Minh"

# Encryption
encrypted_text = rc4_cipher(key, plaintext)
print("Encrypted:", (encrypted_text))

# Decryption
decrypted_text = rc4_cipher(key, encrypted_text)
print("Decrypted:", decrypted_text.decode('utf-8'))
