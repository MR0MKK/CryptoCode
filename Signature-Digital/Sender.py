import rsa
import os
import shutil

    
print("Signature Digital System")
file_path = input("Path your document: ")

if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]


# Read file for sign
try:
    with open(file_path, 'rb') as file:
        content = file.read()
    print("Successfully !!!")
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error when read file")

# Create file name
def Create_Name(path):
    end_index = path.find(".")
    first_part = path[:end_index]

    # Lấy giá trị từ dấu "\" cuối đến dấu "." đầu tiên
    start_index = path.rfind("\\") + 1
    second_part = path[start_index:end_index]
    os.makedirs(second_part)
    shutil.copy2(path,first_part)
    return first_part,second_part
folder_path,file_name=Create_Name(file_path)

# Create keys of RSA
publicKey, privateKey = rsa.newkeys(2048)

# Create PEM file for public key
public_file_path = os.path.join(folder_path, "public.PEM")
with open(public_file_path,"wb") as file:
    file.write(publicKey.save_pkcs1("PEM"))
    
# Create PEM file for private key
# private_file_path = os.path.join(folder_path, "private.PEM")
with open("private.PEM","wb") as file:   
    file.write(privateKey.save_pkcs1("PEM"))

# Create signature
signature = rsa.sign(content, privateKey, "SHA-512")

# Write signature to file
signitare_file_path = os.path.join(folder_path,"Signature")
with open(signitare_file_path, "wb") as file:
    file.write(signature)

decode_file=os.path.join(folder_path,"Receiver.py")
shutil.copy2("D:\DESKTOP\RSA\Receiver.py",decode_file)

