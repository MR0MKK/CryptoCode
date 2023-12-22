import hashlib

def Calculate_SHA1(file_path):
    # Tạo đối tượng hash SHA-1
    sha1 = hashlib.sha1()

    try:
        # Mở file và cập nhật đối tượng hash với từng khối dữ liệu
        with open(file_path, 'rb') as file:
            # Tránh việc đọc toàn bộ file vào bộ nhớ
            buffer_size = 512
            while (data := file.read(buffer_size)):
                sha1.update(data)

        # Lấy giá trị băm (hash) dưới dạng hex
        hashed_value = sha1.hexdigest()

        return hashed_value

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error calculating SHA-1 hash: {e}")

if __name__ == '__main__':
    # Sử dụng hàm sha1_hash_file cho một file cụ thể
    file_path = "sample.txt"
    sha1_result = Calculate_SHA1(file_path)
    if sha1_result:
        print(f"SHA-1 hash of '{file_path}': {sha1_result}")
