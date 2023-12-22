import rsa
import os


print("Signature Digital System")
file_path = input("Path your document: ")

if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]

def Create_Name(path):
    end_index = path.find(".")
    first_part = path[:end_index]

    # Lấy giá trị từ dấu "\" cuối đến dấu "." đầu tiên
    start_index = path.rfind("\\") + 1
    second_part = path[start_index:end_index]
    os.makedirs(second_part)
    return first_part,second_part
folder_path,file_name=Create_Name(file_path)



# Read PEM file for public key
public_file_path = os.path.join(folder_path, "public.PEM")
with open(public_file_path,"rb") as file:
    publicKey = rsa.PublicKey.load_pkcs1(file.read())
    

# Read file for verify
try:
    with open(file_path, 'rb') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error when read file")

# Reda signature to file
signitare_file_path = os.path.join(folder_path,"Signature")
with open(signitare_file_path, "rb") as file:
    signature = file.read()

try:    
    rsa.verify(content, signature, publicKey)
    print("Verify Successfully !!!")
except rsa.VerificationError:
    print("Verify Fail !!!")