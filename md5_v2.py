def Calculate_MD5(message: str):
    # Mở file ở chế độ nhị phân và đọc nội dung của file
    data = message.encode()
    # Hàm hỗ trợ được sử dụng trong các phép toán
    def rotate_left_uint32(n: int, d: int) -> int:
        return (n << d) | (n >> (32 - d))

    # Số lần dịch trái cho mỗi vòng
    S = ([7, 12, 17, 22] * 4
        + [5, 9, 14, 20] * 4
        + [4, 11, 16, 23] * 4
        + [6, 10, 15, 21] * 4)

    # Phần nguyên nhị phân của (2**32 * abs(math.sin(i + 1))) for i in range(64)  (rad) được sử dụng như các hằng số
    K = [3614090360, 3905402710, 606105819, 3250441966,
         4118548399, 1200080426, 2821735955, 4249261313,
         1770035416, 2336552879, 4294925233, 2304563134,
         1804603682, 4254626195, 2792965006, 1236535329,
         4129170786, 3225465664, 643717713, 3921069994,
         3593408605, 38016083, 3634488961, 3889429448,
         568446438, 3275163606, 4107603335, 1163531501,
         2850285829, 4243563512, 1735328473, 2368359562,
         4294588738, 2272392833, 1839030562, 4259657740,
         2763975236, 1272893353, 4139469664, 3200236656,
         681279174, 3936430074, 3572445317, 76029189,
         3654602809, 3873151461, 530742520, 3299628645,
         4096336452, 1126891415, 2878612391, 4237533241,
         1700485571, 2399980690, 4293915773, 2240044497,
         1873313359, 4264355552, 2734768916, 1309151649,
         4149444226, 3174756917, 718787259, 3951481745]

    # Khởi tạo biến
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Tiền xử lý: thêm bit '1' và thêm các bit '0' cho đến khi độ dài là 56 (mod 64)
    data += b'\x80'
    while (len(data) % 64) != 56:
        data += b'\x00'

    # Thêm độ dài ban đầu của thông điệp trong bit (mod 2^64 == 8 Bytes) vào dữ liệu
    data += ((len(message) * 8) % (2 ** 64)).to_bytes(length=8,
                                                    byteorder='little')

    # Xử lý dữ liệu từng khối 512-bit liên tiếp
    chunks = [data[i:i + 64] for i in range(0, len(data), 64)]
    for chunk in chunks:

        # Chia thành 16 khối, mỗi khối 32-bit
        M = [int.from_bytes(chunk[i:i + 4], byteorder='little')
            for i in range(0, len(chunk), 4)]

        # Khởi tạo giá trị hash cho khối này
        A = a0
        B = b0
        C = c0
        D = d0

        # Thực hiện 4 vòng, mỗi vòng 16 phép toán
        for i in range(64):
            # vòng 1
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i

            # vòng 2
            elif 16 <= i <= 31:
                F = (B & D) | (~D & C)
                g = (5 * i + 1) % 16

            # vòng 3
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16

            # vòng 4
            elif 48 <= i <= 63:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            # Lưu kết quả phép toán (bọc biến như trong số nguyên 32-bit không dấu)
            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + rotate_left_uint32(F, S[i])) & 0xFFFFFFFF

        # Thêm giá trị hash của khối hiện tại vào kết quả cho đến nay (mod 2**32)
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    # Chuyển đổi giá trị từ số nguyên sang byte, lưu ý rằng tất cả các giá trị đều ở dạng little-endian!
    a0 = a0.to_bytes(length=4, byteorder='little')
    b0 = b0.to_bytes(length=4, byteorder='little')
    c0 = c0.to_bytes(length=4, byteorder='little')
    d0 = d0.to_bytes(length=4, byteorder='little')

    digest = a0 + b0 + c0 + d0

    return digest.hex()

if __name__ == '__main__':
    file_path = "sample.txt"

    try:
        with open(file_path, 'r') as file:
            
            file_data = file.read()
            md5_result = Calculate_MD5(file_data)
            print(f"MD5 hash of '{file_path}': {md5_result}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error calculating MD5 hash: {e}")

