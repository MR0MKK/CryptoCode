def initialize_S_T(key, N):
    S = list(range(8))
    T = key[:N]
    
    j = 0
    for i in range(8):
        j = (j + S[i] + T[i % N]) % 8
        S[i], S[j] = S[j], S[i]
    
    return S

def text_to_binary(text):
    binary_representation = ''.join(format(ord(char), '08b') for char in text)
    return binary_representation

def binary_to_text(binary_str):
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text

def tinyrc4(key, plaintext):
    N = len(key)
    S = initialize_S_T(key, N)
    
    keystream = []
    i = j = 0

    for _ in range(len(plaintext)):
        i = (i + 1) % 8
        j = (j + S[i]) % 8
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 8
        keystream.append(S[t])

    ciphertext = [int(plaintext[i]) ^ keystream[i] for i in range(len(plaintext))]
    return ciphertext

def main():
    key = [2, 1, 3]
    plaintext_str = "bag"

    plaintext_binary = text_to_binary(plaintext_str)
    print("Plaintext (binary):", plaintext_binary)

    ciphertext = tinyrc4(key, plaintext_binary)
    print("Ciphertext:", ''.join(map(str, ciphertext)))

    decrypted_text_binary = tinyrc4(key, ciphertext)
    decrypted_text_str = binary_to_text(''.join(map(str, decrypted_text_binary)))
    print("Decrypted Text:", decrypted_text_str)

if __name__ == "__main__":
    main()
