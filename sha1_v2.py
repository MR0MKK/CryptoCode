import struct

def Calculate_SHA1(message: str):

    data = message.decode()

    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    # Khởi tạo các biến
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Thêm padding
    message = bytearray(data.encode('utf-8'))
    original_length_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += struct.pack('>Q', original_length_bits)

    # Xử lý từng khối 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', block[j*4:j*4+4])[0]
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + w[j] & 0xFFFFFFFF
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Kết quả là giá trị hex của các biến h0, h1, h2, h3, h4
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)


if __name__ == '__main__':
    file_path = "sample.txt"

    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            sha1_result = Calculate_SHA1(file_data)
            print(f"SHA1 hash of '{file_path}': {sha1_result}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error calculating SHA-1 hash: {e}")
