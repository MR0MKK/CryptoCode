import hashlib

def Calculate_SHA256(file_path):
    # Tạo đối tượng hash SHA-256
    sha256 = hashlib.sha256()

    try:
        # Mở file và cập nhật đối tượng hash với từng khối dữ liệu
        with open(file_path, 'rb') as file:
            # Tránh việc đọc toàn bộ file vào bộ nhớ
            buffer_size = 512
            while (data := file.read(buffer_size)):
                sha256.update(data)

        # Lấy giá trị băm (hash) dưới dạng hex
        hashed_value = sha256.hexdigest()

        return hashed_value

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error calculating SHA-256 hash: {e}")

if __name__ == '__main__':
    # Sử dụng hàm sha256_hash_file cho một file cụ thể
    file_path = "sample.txt"
    sha256_result = Calculate_SHA256(file_path)

    if sha256_result:
        print(f"SHA-256 hash of '{file_path}': {sha256_result}")

