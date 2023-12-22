import hashlib
 
def Calculate_MD5(file_path):
    # Tạo đối tượng hash MD5 
    md5_hash = hashlib.md5()
    try:
        # Mở file và cập nhật đối tượng hash với từng khối dữ liệu
        with open(file_path, 'rb') as file:
            # Tránh việc đọc toàn bộ file vào bộ nhớ
            chunk_size = 512  
            while chunk := file.read(chunk_size):
                md5_hash.update(chunk)

        # Lấy giá trị băm (hash) dưới dạng hex
        md5_hex = md5_hash.hexdigest()

        return md5_hex
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error calculating SHA-1 hash: {e}")
        
if __name__ == '__main__':
    # Sử dụng hàm Calculate_MD5 cho một file cụ thể

    file_path = "sample.txt"
    md5_result = Calculate_MD5(file_path)
    if md5_result:
        print(f"MD5 hash of '{file_path}': {md5_result}")